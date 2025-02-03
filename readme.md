# ALIBIS: Assessing and mitigating the risk of sensitive metadata Leakage In moBile Image Sharing 
## 1. Citation
If you use ALIBIS results, please cite the following information. Thank you.
## 2. Introduction

This is the source code of the paper **ALIBIS: Assessing and mitigating the risk of sensitive metadata Leakage In moBile Image Sharing**.

**ALIBIS** is a framework that automatically estimates the risk of sensitive metadata leakage when users share images online by combining static analysis and Large Language Models (LLMs).

**ALIBIS** advances **[MetaLeak's](https://github.com/research-mobile-security/MetaLeak)** foundation (our previous research) by replacing the semi-automated dynamic analysis process with LLMs' code summarization capabilities to determine whether an app deletes or retains sensitive metadata and, if it keeps sensitive metadata, identifies metadata types.

The architecture of ALIBIS is as follows:

<img src="https://github.com/research-mobile-security/ALIBIS/blob/main/images/realme-architecture-1.png">

## 3. Source code

**ALIBIS** is designed in a microservice architecture, so let's see the detailed source code of each service as follows:

- Client-side:
    - (UAS)-upload-apk-service
    - (MTS)-mimetype-service
- Server-side:
    - Decompile Module
        - (RAS)-receive-apk-service
        - (DSA)-decompile-apk-service
    - System Log
    - EXIF-related Code Block Extraction Module
        - (CES)-code-extraction-service
        - (JMS)-json2mongoDB-service
    - Code Summarization Module
        - (CSS)-code-summarization-service
