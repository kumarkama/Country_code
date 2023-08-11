from flask import Flask, request, json

app = Flask(__name__)

API_URL = "https://www.travel-advisory.info/api"
DATA_FILE = "data.json"

@app.route('/health')
def health_check():
def fetch_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json({'status': 'healthy'})
    else:
        print("Error fetching data from API")
        return None

@app.route('/diag')
def diagnostic_check():
    # Perform any diagnostic checks here
    # For simplicity, let's assume everything is fine
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json({'status': 'ok'})
    else:
        print("Error from API")
        return None

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
