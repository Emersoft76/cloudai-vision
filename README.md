<p align="center">
  <h1 align="center">☁️🤖 CloudAI Vision</h1>
  <p align="center">Scalable Serverless Image Intelligence Powered by AWS and AI</p>

  <p align="center">
    <a href="https://aws.amazon.com/rekognition/">
      <img src="https://img.shields.io/badge/AWS%20Rekognition-Image%20AI-orange?style=for-the-badge&logo=amazonaws" alt="AWS Rekognition Badge">
    </a>
    <a href="https://aws.amazon.com/lambda/">
      <img src="https://img.shields.io/badge/AWS%20Lambda-Serverless-yellow?style=for-the-badge&logo=aws-lambda" alt="AWS Lambda Badge">
    </a>
    <a href="https://aws.amazon.com/s3/">
      <img src="https://img.shields.io/badge/AWS%20S3-Cloud%20Storage-blue?style=for-the-badge&logo=amazonaws" alt="AWS S3 Badge">
    </a>
    <a href="https://aws.amazon.com/dynamodb/">
      <img src="https://img.shields.io/badge/AWS%20DynamoDB-NoSQL%20Database-darkblue?style=for-the-badge&logo=amazonaws" alt="AWS DynamoDB Badge">
    </a>
    <a href="https://aws.amazon.com/api-gateway/">
      <img src="https://img.shields.io/badge/AWS%20API%20Gateway-APIs-lightgrey?style=for-the-badge&logo=amazonaws" alt="AWS API Gateway Badge">
    </a>
  </p>

</p>

---

## 🇬🇧 About the Project

**CloudAI Vision** is a fully serverless, scalable solution that analyzes images uploaded to AWS S3 using artificial intelligence (AWS Rekognition).  
It automatically stores analysis metadata in DynamoDB and exposes a public API for retrieving results in real time.

This project demonstrates real-world cloud architecture combining **Nuvem + Inteligência Artificial** in a highly efficient and practical way.

---

## 🇧🇷 Sobre o Projeto

**CloudAI Vision** é uma solução totalmente serverless e escalável que analisa imagens enviadas para o AWS S3 usando inteligência artificial (AWS Rekognition).  
Automaticamente, armazena os metadados da análise no DynamoDB e expõe uma API pública para consulta em tempo real.

Este projeto demonstra uma arquitetura real de nuvem combinando **Cloud + Inteligência Artificial** de forma prática e eficiente.

---

## 📂 Projeto - Estrutura de Diretórios

```bash
cloudai-vision/
├── README.md
├── architecture-diagram.md
├── s3-bucket-structure.md
├── dynamodb-schema.md
├── api-specifications.md
├── lambdas/
│   ├── process-image-upload/
│   │   ├── lambda_function.py
│   │   └── README.md
│   ├── fetch-image-analysis/
│   │   ├── lambda_function.py
│   │   └── README.md
├── terraform/ (opcional para IaC)
│   ├── main.tf
│   ├── outputs.tf
│   ├── variables.tf
│   └── README.md
└── docs/
    ├── installation-guide.md
    └── usage-guide.md
```
---

## 🛠️ AWS Services Used | Serviços AWS Utilizados

| Service             | Function                                | Serviço            | Função                                       |
|---------------------|-----------------------------------------|--------------------|----------------------------------------------|
| **Amazon S3**       | Storage for uploaded images             | Amazon S3          | Armazenamento de imagens enviadas            |
| **AWS Lambda**      | Serverless image processing and API     | AWS Lambda         | Processamento de imagens e APIs serverless   |
| **AWS Rekognition** | AI image analysis (objects, faces, etc) | AWS Rekognition    | Análise de imagens com IA (objetos, rostos)  |
| **DynamoDB**        | Storage for analysis metadata           | DynamoDB           | Armazenamento de metadados de análise        |
| **API Gateway**     | Public API to access analysis results   | API Gateway        | API pública para consulta dos resultados     |

---

## ⚡ Quick Start

| Step | 🇬🇧 English                                                      | 🇧🇷 Português                                                       |
|------|------------------------------------------------------------------|--------------------------------------------------------------------|
| 1    | Fork/Clone this repository.                                     | Faça o fork/clone deste repositório.                              |
| 2    | Configure AWS CLI locally.                                      | Configure o AWS CLI localmente.                                   |
| 3    | Create required services via [installation-guide.md](./docs/installation-guide.md) | Crie os serviços necessários via [installation-guide.md](./docs/installation-guide.md) |
| 4    | Deploy Lambdas and API Gateway.                                 | Faça o deploy das Lambdas e do API Gateway.                       |
| 5    | Test uploading images and retrieving analysis via the API.      | Teste o envio de imagens e consulta das análises pela API.         |

---


Important Note | Nota Importante:

Cloud resource usage (even on AWS Free Tier) can generate costs.

O uso de recursos em nuvem (mesmo no AWS Free Tier) pode gerar custos.

---
