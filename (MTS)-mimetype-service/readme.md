## 1. Introduction

The **MimeType service** is part of the **MetaLeak-LLM-based** system architecture.

This service is used to collect mime types that are related to images **(image/* and */*)** along with their corresponding supported **actions** by the apps.

<img src="https://github.com/thanhlam2110/metaLeak-ml-manifest-mimeType/blob/main/readme-image/metaLeak-ml-overview.png">

## 2. Source code

The **MimeType service** takes an input APK file and returns mime types and actions in JSON format. The result is written in a CSV file in the corresponding apk_name position.

For example: 

<img src="https://github.com/thanhlam2110/metaLeak-ml-manifest-mimeType/blob/main/readme-image/example.png">

