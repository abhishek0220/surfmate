from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ClassifyImage/', methods=['GET', 'POST'])
def classify_image() -> str:
    if request.method == 'GET':
        return render_template('select_img.html')
    if request.method == 'POST':
        # run model on google cloud
        return "Yes"
    return "Method Not Allowed"


if __name__ == '__main__':
    app.run()
