from flask import Flask, request
from mom import mom, mom_config
from grpc_client import grpc_c
import grpc
import json
import api_config

app = Flask(__name__)

servers = [mom, grpc_c]
current_server = 0

@app.route('/api', methods=['GET'])
def run_files():
    global current_server
    type = request.args.get('list')
    if type is not None:
        server = servers[current_server]
        current_server = (current_server + 1) % len(servers)
        response_json = server.get_files(type)
        if response_json is not None:
            print(response_json)
            return response_json
        else:
            response_json = server.get_files(type)
            return response_json
    else:
        return json.dumps({'error': 'No list parameter provided'})

if __name__ == '__main__':
    app.run(host=api_config.HOST, port=api_config.PORT)
