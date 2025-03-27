from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

app.config['SERVER_NAME'] = os.environ['SERVER_NAME']

@app.route('/', methods=['POST'], subdomain='deploy')
def webhook():
    if request.method == 'POST':
        subprocess.run(["./deploy.sh"])
        return 'Deploy iniciado!', 200
    return 'Método não permitido.', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)