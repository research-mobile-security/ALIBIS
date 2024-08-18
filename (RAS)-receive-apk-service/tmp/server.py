# server.py

import grpc
from concurrent import futures
import os
import logging
import upload_pb2
import upload_pb2_grpc

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class YourService(upload_pb2_grpc.YourServiceServicer):
    def Upload(self, request, context):
        apkfile_name = request.apkfile_name
        apk_content = request.apk_content

        # Save the received APK chunk to file
        apk_path = f"/root/decompile/apk/{apkfile_name}"
        with open(apk_path, "ab") as apk_file:
            apk_file.write(apk_content)

        logging.info(f"Server: Received chunk for '{apkfile_name}'")

        # Send a response back to the client
        return upload_pb2.UploadResponse(message=f"Received chunk for '{apkfile_name}'")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    upload_pb2_grpc.add_YourServiceServicer_to_server(YourService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("Server: Service is running...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
