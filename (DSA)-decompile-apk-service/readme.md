## 1. Introduction

The **DECOMPILE-APK service** is part of the **MetaLeak-LLM-based** system architecture.

This service is used to decompile the APK in a directory _/root/decompile/apk/_  from **.apk → *.jar → JAVA source code**.

<img src="https://github.com/research-mobile-security/REALME/blob/main/(DSA)-decompile-apk-service/readme-image/metaLeak-ml-overview.png">

## 2. Source code

The **DECOMPILE-APK service** runs as a docker container, continuously monitoring the directory _/root/decompile/apk/_ and automatically performs the decompile process when an APK file exists.

After completing the decompile process, the **DECOMPILE-APK service** updates the _decompile.csv_ file (used in the **RECEIVE-APK service**) with the value _"DONE"_ in the **"decompile_jar"** and **"decompile_java"** columns at the corresponding **apk_name** position. Conversely, if the decompile process timeout, the **"decompile_jar"** and **"decompile_java"** columns are updated with the value _"TIMEOUT"_.

<img src="https://github.com/research-mobile-security/REALME/blob/main/(DSA)-decompile-apk-service/readme-image/csv.png">

The timeout duration of the decompile process depends on the size of the APK file.

Logs of the decompile process are sent to the **ELK stack** via the **Kafka message queue** on the topic **decompile-log**.

<img src="https://github.com/research-mobile-security/REALME/blob/main/(DSA)-decompile-apk-service/readme-image/elk.png">

## 3. How to run?

```bash
find /root/decompile/apk/ -type f -size 0 -delete
docker build -t metaleak-apk-decompile:1.0.0 .
docker run -d -v /root/decompile:/root/decompile metaleak-apk-decompile:1.0.0
```