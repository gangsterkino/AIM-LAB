# AIM-LAB

# 创建虚拟环境
```sh
python -m venv venv
```
或者
```sh
python3 -m venv venv
```
# 激活虚拟环境 (根据操作系统不同，选择相应的命令)

# 对于 macOS/Linux:
```sh
source venv/bin/activate
```

# 对于 Windows:
```sh
venv\Scripts\activate

```
:
```sh
pip install Flask pyngrok
```
# 运行 Flask 应用
接下来，启动 Flask 应用来服务 Umi 项目的静态文件：

```sh 
python app.py

```

当服务器启动后，终端会输出类似如下信息：

 * Ngrok Tunnel URL: http://your-ngrok-url.ngrok.io
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
http://127.0.0.1:5000 可以在本地访问你的项目。
http://your-ngrok-url.ngrok.io 是公开的 URL，你可以将其分享给其他人，他们可以通过该地址访问你的项目。


# 访问项目
在本地访问：打开浏览器，进入 http://127.0.0.1:5000。
外部用户访问：分享终端输出的 Ngrok URL，例如 http://your-ngrok-url.ngrok.io。

# 关闭服务器
要停止服务器运行，你可以在终端中按 CTRL + C 来关闭 Flask 应用。

注意事项
每次启动 Ngrok 都会生成一个新的公开 URL。如果你需要一个固定的域名，请考虑注册 Ngrok 并使用他们的收费计划。
请确保在启动 Flask 应用时激活虚拟环境。