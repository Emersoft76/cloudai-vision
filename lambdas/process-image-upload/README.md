# 🧠 Lambda Function - process-image-upload

## 🇬🇧 Description

This function is triggered when an image is uploaded to the S3 bucket.  
It uses AWS Rekognition to detect labels and stores the results in DynamoDB.

## 🇧🇷 Descrição

Esta função é acionada quando uma imagem é enviada ao bucket S3.  
Ela utiliza o AWS Rekognition para detectar rótulos e armazena os resultados no DynamoDB.

---

## 🧩 Environment Variables | Variáveis de Ambiente

| Name         | Description (EN)                   | Descrição (PT)                      |
|--------------|------------------------------------|-------------------------------------|
| `TABLE_NAME` | Name of the DynamoDB table         | Nome da tabela no DynamoDB          |

---

## 📥 Trigger

| Source | Type | Description |
|--------|------|-------------|
| S3     | Event | ObjectCreated:* — Any image uploaded will trigger this Lambda |

---

## 🔐 IAM Permissions | Permissões IAM

```json
{
  "Effect": "Allow",
  "Action": [
    "rekognition:DetectLabels",
    "dynamodb:PutItem"
  ],
  "Resource": "*"
}
```
---

✅ Tip: Ensure the Lambda execution role includes S3 read permissions.
✅ Dica: Garanta que a role da Lambda tenha permissão de leitura no S3.

---
