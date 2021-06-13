import os
import uuid
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from utils.image_classification import get_prediction

load_dotenv()
app = Flask(__name__)


limiter = Limiter(
    app,
    key_func=get_remote_address
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Features/')
def features():
    return render_template('features.html')


@app.route('/Chat/')
def chat():
    return render_template('chat.html')


@app.route('/ClassifyImage/', methods=['GET', 'POST'])
@limiter.limit("1/second;20/hour", methods=['POST'])
def classify_image():
    if request.method == 'GET':
        return render_template('select_img.html')
    if request.method == 'POST':
        img = request.files['image']
        save_path = os.path.join(os.getcwd(), str(uuid.uuid4()))
        img.save(save_path)
        with open(save_path, 'rb') as img_file:
            img_b64 = img_file.read()
        os.remove(save_path)
        resp = get_prediction(img_b64)
        return render_template('select_img.html', resp=resp)


@app.route('/NearbyBeaches/', methods=['GET', 'POST'])
@limiter.limit("1/second;20/hour", methods=['POST'])
def beaches():
    if request.method == 'GET':
        return render_template('beaches.html')
    if request.method == 'POST':
        lat = request.form['latitude']
        lon = request.form['longitude']
        endpoint = "https://atlas.microsoft.com/search/nearby/json"
        params = {
            'api-version': '1.0',
            'subscription-key': os.environ["AZURE_MAP_KEY"],
            'categorySet': '9357',
            'lat': lat,
            'lon': lon,
        }
        url = endpoint
        resp = requests.get(url, params)
        return resp.json()


if __name__ == '__main__':
    app.run()
