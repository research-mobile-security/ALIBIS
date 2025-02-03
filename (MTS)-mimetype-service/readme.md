## 1. Introduction

The **(MTS)-mimetype-service** is part of the **ALIBIS** system architecture.

This service is used to collect mime types that are related to images **(image/* and */*)** along with their corresponding supported **actions** by the apps.

<img src="https://github.com/research-mobile-security/ALIBIS/blob/main/(MTS)-mimetype-service/readme-image/metaLeak-ml-overview.png">

## 2. Source code

The **(MTS)-mimetype-service** takes an input APK file and returns mime types and actions in JSON format. The result is written in a CSV file in the corresponding apk_name position.

For example: 

<img src="https://github.com/research-mobile-security/ALIBIS/blob/main/(MTS)-mimetype-service/readme-image/example.png">

