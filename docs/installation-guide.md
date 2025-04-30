# ⚙️ Installation Guide | Guia de Instalação

Este guia explica como configurar todos os serviços AWS necessários para o projeto **CloudAI Vision**, via console ou AWS CLI.

---

## ✅ Prerequisites | Pré-requisitos

- AWS Account (Conta AWS)
- AWS CLI configured (`aws configure`)
- IAM user with sufficient permissions
- Python 3.x (para testes locais das Lambdas)

---

## ☁️ 1. Create an S3 Bucket | Criar um Bucket S3

**English**  
Create a bucket to upload and trigger image analysis.

**Português**  
Crie um bucket para enviar imagens e disparar a análise.

```bash
aws s3 mb s3://cloudai-vision-input
```
Use a unique name for the bucket.
Use um nome único para o bucket.

---

## 🧠 2. Enable Rekognition Access | Ativar o acesso ao Rekognition

Rekognition does not require prior setup.
O Rekognition não exige configuração prévia.

   Make sure your Lambda has IAM permissions:
   Certifique-se de que sua Lambda tenha permissões IAM adequadas:
```json
{
  "Effect": "Allow",
  "Action": [
    "rekognition:DetectLabels",
    "rekognition:DetectFaces"
  ],
  "Resource": "*"
}
```
---

## 🗃️ 3. Create DynamoDB Table | Criar Tabela no DynamoDB

English
This table stores metadata of image analyses.

Português
Essa tabela armazena os metadados das análises das imagens.
```
aws dynamodb create-table \
  --table-name cloudai-vision-results \
  --attribute-definitions AttributeName=imageKey,AttributeType=S \
  --key-schema AttributeName=imageKey,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```
---

## 🔁 4. Create Lambda Functions | Criar Funções Lambda

* process-image-upload: triggered by S3 to analyze images

* fetch-image-analysis: fetches analysis from DynamoDB

  Set handler: lambda_function.lambda_handler
  
  Defina o handler: lambda_function.lambda_handler

Permissions Required | Permissões Requeridas:

  * S3 read

  * Rekognition

  * DynamoDB write/read
---

## 🌐 5. Create API Gateway | Criar API Gateway

English
Create a REST API to allow GET access to metadata.

Português
Crie uma API REST para permitir acesso GET aos metadados.

  * Method: GET

  * Integration: Lambda (fetch-image-analysis)

  * Endpoint: /analyze/{imageKey}
---

## ✅ Summary | Resumo

| Service     | Setup (🇬🇧 EN)                          | Configuração (🇧🇷 PT)                      |
|-------------|-----------------------------------------|--------------------------------------------|
| **S3**      | Bucket with trigger                     | Bucket com acionador                       |
| **Lambda**  | Two functions, properly permissioned    | Duas funções com permissões adequadas      |
| **Rekognition** | IAM permissions only                | Apenas permissões via IAM                  |
| **DynamoDB**| Table with `imageKey` (string)          | Tabela com `imageKey` (string)             |
| **API Gateway** | Public GET endpoint                | Endpoint público GET                       |

---

Important Note | Nota Importante

All services can be deployed using the AWS Free Tier if used within limits.

Todos os serviços podem ser utilizados no Free Tier da AWS, se usados dentro dos limites.

---
