from flask import Flask, render_template
import requests

app = Flask(__name__)


API_KEY = 'fb73eddbc776cb2eca5b4d36'
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

@app.route('/')
def home():
    
    response = requests.get(BASE_URL)
    
    if response.status_code == 200:
        
        data = response.json()
        
        usd_to_try = data['conversion_rates']['TRY']
    else:
        usd_to_try = None

    
    return render_template('index.html', usd_to_try=usd_to_try)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
