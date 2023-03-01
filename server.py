from flask import Flask, request
import mom
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def run_files():
    if request.args.get('list'):
        return mom.get_files()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)