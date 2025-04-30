# ⚙️ Terraform Infrastructure for CloudAI Vision

## 🇬🇧 Description

This module provisions the core infrastructure required for the CloudAI Vision project using AWS Terraform resources.

## 🇧🇷 Descrição

Este módulo provisiona a infraestrutura principal necessária para o projeto CloudAI Vision usando recursos da AWS via Terraform.

---

## 🛠️ Resources Created | Recursos Criados

- S3 Bucket for image uploads
- DynamoDB Table for storing analysis results

---

## 🚀 Usage | Como Usar

```bash
terraform init
terraform apply -var="bucket_name=cloudai-vision-input" -var="dynamodb_table=cloudai-vision-results"
```
✅ Tip: Set the region variable if you're not using the default (eu-west-1).

---
