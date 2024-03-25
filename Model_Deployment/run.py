import model
from flask import Flask,request,jsonify,render_template , redirect,url_for,send_file, make_response
from flask_cors import CORS
from PIL import Image
import io
import base64


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
    # 將圖片轉換為 base64 編碼
    buf = io.BytesIO()
    image.save(buf, format='PNG')
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    # 回傳一個包含圖片和預測結果的 HTML 頁面
    return render_template('result.html',
                           image_base64=image_base64, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')