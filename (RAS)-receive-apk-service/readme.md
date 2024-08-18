## 1. Introduction

The **RECEIVE-APK service** is part of the **MetaLeak-LLM-based** system architecture.

This service is used to receive the APK upload stream from the Client **(UPLOAD-APK service)** and then stored in a specific directory _(/root/decompile/apk/)_.

<img src="https://github.com/research-mobile-security/REALME/blob/main/(RAS)-receive-apk-service/readme-image/metaLeak-ml-overview.png">

## 2. Source code

The **RECEIVE-APK service** utilizes the GRPC protocol (http/2) to increase speed.

After successfully receiving an APK file, the **RECEIVE-APK service** records the information of the APK file in _/root/decompile/decompile.csv_, as shown below.

<img src="https://github.com/research-mobile-security/REALME/blob/main/(RAS)-receive-apk-service/readme-image/csv.png">

## 3. How to run?

```bash
bash environment.sh
docker build -t metaleak-ml-apk-upload-server:1.0.0 .
docker run -d -v /root/decompile:/root/decompile -p 50051:50051 metaleak-ml-apk-upload-server:1.0.0
```