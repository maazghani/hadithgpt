from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SAHIH_API_URL = "https://api.sunnah.com/v1/hadiths"  # Replace with the correct endpoint from the API docs
API_KEY = "YOUR_API_KEY"  # Replace with your API key

@app.route('/api/query', methods=['POST'])
def query_hadith():
    data = request.json
    query = data.get('query', '')

    headers = {
        "X-API-Key": API_KEY
    }
    
    # Make a request to the Sahih AI API
    response = requests.get(f"{SAHIH_API_URL}?query={query}", headers=headers)
    hadith_data = response.json()

    hadiths = []
    for hadith in hadith_data:
        hadiths.append({
            "content": hadith["englishText"],
            "arabic": hadith["arabicText"],
            "source": hadith["source"]
        })

    return jsonify({
        "hadiths": hadiths,
        "template": "This is your template for responding. Remember to replace {english} {arabic} {source} in the template with the hadith's english, arabic, and source respectively."
    })

if __name__ == '__main__':
    app.run(debug=True)

