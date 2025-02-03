## 1. Introduction

The **(RAS)-receive-apk-service** is part of the **ALIBIS** system architecture.

This service is used to receive the APK upload stream from the Client **((UAS)-upload-apk-service)** and then stored in a specific directory _(/root/decompile/apk/)_.

<img src="https://github.com/research-mobile-security/ALIBIS/blob/main/(RAS)-receive-apk-service/readme-image/metaLeak-ml-overview.png">

## 2. Source code

The **(RAS)-receive-apk-service** utilizes the GRPC protocol (http/2) to increase speed.

After successfully receiving an APK file, the **(RAS)-receive-apk-service** records the information of the APK file in _/root/decompile/decompile.csv_, as shown below.

<img src="https://github.com/research-mobile-security/ALIBIS/blob/main/(RAS)-receive-apk-service/readme-image/csv.png">

## 3. How to run?

```bash
bash environment.sh
docker build -t metaleak-ml-apk-upload-server:1.0.0 .
docker run -d -v /root/decompile:/root/decompile -p 50051:50051 metaleak-ml-apk-upload-server:1.0.0
```