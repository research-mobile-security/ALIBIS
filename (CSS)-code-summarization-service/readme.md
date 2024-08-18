## 1. Introduction

The **(CSS)-code-summarization-service** is part of the **REALME** system architecture.

This service is used to determine the purpose of EXIF-related codebooks, including:

- How do code blocks handle EXIF metadata? Retain EXIF metadata in images or remove it?
- If the code block retains EXIF metadata, what types of metadata does the code block retain among the five types of **datetime, GPS, model, brand, and software**?

This service is applicable to **Group-1** and **Group-2** with:

- Group-1: using mapping function and cosine-similarity
- Group-2: using LLM-RAG

<img src="https://github.com/research-mobile-security/REALME/blob/main/(CSS)-code-summarization-service/group-1/group-1-code-purpose/readme-image/metaLeak-ml-overview.png">