## 1. Introduction

The **(CES)-code-extraction-service** is part of the **REALME** system architecture.

This service is used to extract all code blocks that are related to handling EXIF metadata and then return the **EXIF-related code blocks** as JSON files.

<img src="https://github.com/research-mobile-security/REALME/blob/main/(CES)-code-extraction-service/readme-image/metaLeak-ml-overview.png">

## 2. Source code

The **(CES)-code-extraction-service** includes the following steps:

- **Step 1: EXIF code search:**

In this step, the algorithm will traverse the entire source code directory of APK files after being decompiled by the **(DSA)-decompile-apk-service**. The algorithm will search for all files containing the keyword "exif" and then copy these files to the directory .\\exif-java\\<app_name>.

For example:

<img src="https://github.com/research-mobile-security/REALME/blob/main/(CES)-code-extraction-service/readme-image/step-1.png">

- **Step 2: Clean comment:**

In this step, the algorithm iterates through all files in the directory .\\exif-java\\<app_name> and removes all comment code in these files.

- **Step 3: Grouping:**

In this step, the algorithm divides the apps into 3 groups based on how the app's code blocks handle EXIF metadata:

    - Group 1: using **android.media.ExifInterface (method-1)** & **androidx.exifinterface.media (method-2)**
    - Group 2: using a **self-developed function**

<img src="https://github.com/research-mobile-security/REALME/blob/main/(CES)-code-extraction-service/readme-image/step-3.png">

- **Step 4: Extract EXIF-related code blocks:**

Depending on each group, the algorithm uses related EXIF keywords to extract all EXIF-related code blocks and writes these code blocks to a JSON file.

For example:
<img src="https://github.com/research-mobile-security/REALME/blob/main/(CES)-code-extraction-service/readme-image/step-4.png">