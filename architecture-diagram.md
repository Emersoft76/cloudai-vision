# 🧭 CloudAI Vision - Architecture Diagram

## 🇬🇧 Overview

This architecture describes a fully serverless and scalable pipeline that analyzes uploaded images using AWS Rekognition and returns metadata via a public API.

## 🇧🇷 Visão Geral

Esta arquitetura descreve um pipeline totalmente serverless e escalável que analisa imagens enviadas usando o AWS Rekognition e retorna metadados por meio de uma API pública.

---

## 🧱 Architecture Components | Componentes da Arquitetura

| Component             | Description (EN)                                           | Descrição (PT)                                             |
|-----------------------|------------------------------------------------------------|-------------------------------------------------------------|
| **S3 Bucket**         | Stores uploaded images                                     | Armazena imagens enviadas                                  |
| **Lambda - Upload**   | Triggered by S3 upload, sends image to Rekognition         | Acionado pelo upload no S3, envia imagem ao Rekognition     |
| **Rekognition**       | Analyzes image (labels, faces, text)                       | Analisa a imagem (rótulos, rostos, texto)                   |
| **DynamoDB**          | Stores analysis results                                    | Armazena os resultados da análise                           |
| **Lambda - API**      | Returns analysis results via GET request                   | Retorna os resultados da análise via requisição GET         |
| **API Gateway**       | Public access endpoint to retrieve analysis                | Endpoint público para recuperar análise                     |
| **IAM Roles**         | Permissions for secure integration between services        | Permissões para integração segura entre os serviços         |

---

## 🔄 Flow Diagram (Text-Based)

```plaintext
[User Uploads Image]
        |
        v
[S3 Bucket]
        |
(Event Trigger)
        v
[AWS Lambda (Upload Handler)]
        |
        v
[AWS Rekognition]
        |
        v
[Image Metadata]
        |
        v
[DynamoDB Storage]
        |
        v
[API Gateway] <--- [Lambda - API Handler] <--- [User GET Request]
```
---

## ⚠️ Notes

  * The entire system is stateless and event-driven.

  * It allows for automatic scaling, parallel processing, and real-time response.

  * All components are eligible under AWS Free Tier with usage constraints.

