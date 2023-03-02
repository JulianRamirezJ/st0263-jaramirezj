from concurrent import futures
import ms2_config
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import service_pb2, service_pb2_grpc

class GetFile(service_pb2_grpc.GetFileServicer):
    def List(self, request, context):
        file_type = request.type
        file_list = []
        for archivo in os.listdir(ms2_config.DIR):
            if file_type is None or archivo.endswith(file_type):
                file_list.append(archivo)
        files_response = json.dumps(file_list)
        print(files_response)
        return service_pb2.FileResponse(files=files_response)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_GetFileServicer_to_server(GetFile(), server)
    server.add_insecure_port(ms2_config.PORT)
    server.start()
    print("Server started. Listening on port " + str(ms2_config.PORT))
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
