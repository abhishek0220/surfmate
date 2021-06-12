import os
import uuid
from flask import Flask, render_template, request

from utils.image_classification import get_prediction

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ClassifyImage/', methods=['GET', 'POST'])
def classify_image() -> str:
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
        return resp
    return "Method Not Allowed"


if __name__ == '__main__':
    app.run()
