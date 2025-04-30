# 🌐 Lambda Function - fetch-image-analysis

## 🇬🇧 Description

This function retrieves analysis results from DynamoDB for a given image key.  
It is triggered by an HTTP GET request via API Gateway.

## 🇧🇷 Descrição

Esta função recupera os resultados de análise do DynamoDB para uma determinada imagem.  
Ela é acionada por uma requisição GET via API Gateway.

---

## 📥 Input

| Parameter   | Type   | Description (EN)                  | Descrição (PT)                        |
|-------------|--------|-----------------------------------|---------------------------------------|
| `imageKey`  | Path   | The name/key of the image in S3   | Nome/chave da imagem no bucket S3     |

---

## 📤 Output

A JSON response containing the list of labels associated with the image.

---

## 🔐 IAM Permissions | Permissões IAM

```json
{
  "Effect": "Allow",
  "Action": [
    "dynamodb:GetItem"
  ],
  "Resource": "*"
}
```
---
✅ Tip: Connect this Lambda to an HTTP GET method in API Gateway.

✅ Dica: Conecte esta Lambda a um método GET no API Gateway.

---
