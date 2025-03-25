from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/webhook-deploy', methods=['POST'])
def webhook():
    if request.method == 'POST':
        directory = os.environ['PUBLIC_DIRECTORY']
        subprocess.run([f"{directory}/deploy.sh"])
        return 'Deploy iniciado!', 200
    return 'Método não permitido.', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)