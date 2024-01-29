import model
from flask import Flask,request,jsonify,render_template , redirect,url_for
from flask_cors import CORS
from PIL import Image
import io


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return redirect(url_for('form'))

@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/predict',methods=['POST'])
def postInput():
    file = request.files['image']
    image = Image.open(io.BytesIO(file.read()))
    result = model.predict(image)
    return (f'The diagnosis result of tumor: {result}.')

if __name__ == '__main__':
    app.run(host='0.0.0.0')