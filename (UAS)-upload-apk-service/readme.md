## 1. Introduction

The **UPLOAD-APK service** is part of the **MetaLeak-LLM-based** system architecture.

This service is used to upload APK files stored in a specific directory at the Client to the Server.

<img src="https://github.com/research-mobile-security/REALME/blob/main/(UAS)-upload-apk-service/readme-image/metaLeak-ml-overview.png">

## 2. Source code

The **UPLOAD-APK service** utilizes the GRPC protocol (http/2) to increase upload speed.

After completing the upload of a file, the **UPLOAD-APK service** updates the **"upload_to_reverse"** column with the value **"DONE"** at the corresponding app position in the CSV file, as shown below.

<img src="https://github.com/research-mobile-security/REALME/blob/main/(UAS)-upload-apk-service/readme-image/csv.png">

## 3. How to run?

```python
python client.py
```