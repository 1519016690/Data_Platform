from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
# 初始化 CORS，允许所有来源的跨域请求
CORS(app)

# 配置上传文件的保存目录
UPLOAD_FOLDER = 'Test_file'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return '未找到文件', 400
    file = request.files['file']
    if file.filename == '':
        return '未选择文件', 400
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        print("进行逻辑处理！")
        return '文件上传成功'
if __name__ == '__main__':
    app.run(host='192.168.101.50', port=8080,debug=True)

