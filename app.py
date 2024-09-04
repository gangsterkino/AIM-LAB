from flask import Flask, send_from_directory, render_template
from pyngrok import ngrok
import os

app = Flask(__name__, static_folder='dist', template_folder='dist')


# 首页
@app.route('/')
def index():
    return render_template('index.html')


# 处理静态文件请求
@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(os.path.join(app.static_folder), path)


if __name__ == '__main__':
    # 允许所有 IP 访问，并设置端口
    port = 5000
    public_url = ngrok.connect(port)
    print(f" * Ngrok Tunnel URL: {public_url}")

    # 启动 Flask 应用
    app.run(host='0.0.0.0', port=port)
