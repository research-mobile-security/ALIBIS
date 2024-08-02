# client.py
import os
import grpc
import pandas as pd
import os
import logging
import upload_pb2
import upload_pb2_grpc

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def upload_apk(stub, apkfile_name, apk_path):
    apkfile_size = os.path.getsize(apk_path)
    with open(apk_path, "rb") as apk_file:
        for chunk in iter(lambda: apk_file.read(8192), b""): 
            request = upload_pb2.UploadRequest(
                apkfile_name=apkfile_name,
                apkfile_size=apkfile_size,
                apk_content=chunk,
            )
            response = stub.Upload(request)
            logging.info(f"Client: Uploaded chunk for '{apkfile_name}' - Response: {response.message}")

    # Upload "DONE" status for the corresponding row in paper_report_test.csv
    upload_done_status(stub, apkfile_name)

def upload_done_status(stub, apkfile_name):
    global df  # Make df global so it can be accessed in the function
    # Update the "upload_to_reverse" column in the CSV file
    df.loc[df['apkfile_name'] == apkfile_name, 'upload_to_reverse'] = 'DONE'
    df.to_csv("no_leak_apk.csv", index=False)
    logging.info(f"Client: Uploaded 'DONE' status for '{apkfile_name}'")

    # Send "Completed" command to the server
    completed_request = upload_pb2.UploadRequest(
        #apkfile_name=f"Completed {apkfile_name}",
        apkfile_name = f"Completed {os.path.splitext(apkfile_name)[0]}",
        apkfile_size=0,  # Set apkfile_size to 0 for the "Completed" command
        apk_content=b"",  # Empty content for the "Completed" command
    )
    completed_response = stub.Upload(completed_request)
    logging.info(f"Client: Sent 'Completed' command for '{apkfile_name}' - Response: {completed_response.message}")

def main():
    # Read CSV file
    global df  # Make df global so it can be accessed in the upload_apk function
    df = pd.read_csv("no_leak_apk.csv")

    # Filter rows where "upload_to_reverse" is not 'DONE'
    df_to_upload = df[df['upload_to_reverse'] != 'DONE']

    if df_to_upload.empty:
        logging.info("Client: All APK files uploaded")
        return

    # Connect to the gRPC server
    channel = grpc.insecure_channel('192.168.1.15:50051')  
    #channel = grpc.insecure_channel('192.168.107.143:50051')
    stub = upload_pb2_grpc.YourServiceStub(channel)

    for index, row in df_to_upload.iterrows():
        apkfile_name = row["apkfile_name"]
        apk_path = f"C:\\Users\\ASUS\\anaconda3\\metaLeak-ml-apk-upload-client\\upload_apk_no_leak\\{apkfile_name}"
        # new code -> check file exist
        if os.path.exists(apk_path):
        # Upload APK file
            logging.info(f"Client: Uploading '{apkfile_name}' to server...")
            upload_apk(stub, apkfile_name, apk_path)
        else:
            logging.warning(f"File '{apkfile_name}' does not exist at '{apk_path}'. Skipping upload.")
if __name__ == "__main__":
    main()
