## 1. Introduction

This is the source code of the paper **REALME: Risk Estimation in Android Apps for Leakage of Metadata**.

The architecture of REALME is as follows:

<img src="https://github.com/research-mobile-security/REALME/blob/main/images/realme-architecture-1.png">

## 2. Source code

**REALME** is designed in a microservice architecture, so let's see the detailed source code of each service as follows:

- Client-side:
    - (UAS)-upload-apk-service
- Server-side:
    - Filter Module
        - (RAS)-receive-apk-service
        - (MTS)-mimetype-service
    - Decompile Module
        - (DSA)-decompile-apk-service
    - EXIF-related Code Block Extraction Module
        - (CES)-code-extraction-service
        - (JMS)-json2mongoDB-service
    - Code Summarization Module
        - (CSS)-code-summarization-service
## 3. Citation
If you use REALME results, please cite the following information. Thank.