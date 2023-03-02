import grpc
import grpc_config
import service_pb2
import service_pb2_grpc

def get_files(file_type=None):
    channel = grpc.insecure_channel(grpc_config.HOST_PORT)
    stub = service_pb2_grpc.GetFileStub(channel)
    request = service_pb2.FileRequest(type=file_type)
    response = stub.List(request)
    f = response.files
    print(f)
    return f
