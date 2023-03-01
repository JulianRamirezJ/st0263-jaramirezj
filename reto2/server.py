from flask import Flask, request
from mom import mom,mom_config
import json
import api_config

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def run_files():
    type = request.args.get('list')
    if type is not None:
        response_json = mom.get_files(type)
        print(response_json)
        return response_json
    else:
        return json.dumps({'error': 'No list parameter provided'})

if __name__ == '__main__':
    app.run(host=api_config.HOST, port=api_config.PORT)

