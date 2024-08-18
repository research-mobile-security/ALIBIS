import grpc
from concurrent import futures
import os
import logging
import upload_pb2
import upload_pb2_grpc

import csv  # Import the csv module for handling CSV files

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class YourService(upload_pb2_grpc.YourServiceServicer):
    def Upload(self, request, context):
        apkfile_name = request.apkfile_name
        apkfile_size = request.apkfile_size
        apk_content = request.apk_content

        # Save the received APK chunk to file
        apk_path = f"/root/decompile/apk/{apkfile_name}"
        with open(apk_path, "ab") as apk_file:
            apk_file.write(apk_content)

        logging.info(f"Server: Received chunk for '{apkfile_name}' - Size: {apkfile_size}")

        # Check if it's a "Completed" command
        if apkfile_name.startswith("Completed "):
            # Extract the original apkfile_name
            original_apkfile_name = apkfile_name[len("Completed "):]
            logging.info(f"Server: Completed processing for '{original_apkfile_name}'")

            # Append the "Completed" entry to the CSV file
            csv_path = "/root/decompile/decompile.csv"
            with open(csv_path, mode='a') as csv_file:
                csv_file.write(f"{original_apkfile_name},,\n")

            # You can add additional logic here for handling "Completed" command

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
