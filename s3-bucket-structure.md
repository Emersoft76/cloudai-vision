# 🗂️ S3 Bucket Structure | Estrutura do Bucket S3

Este documento descreve como o bucket S3 é organizado no projeto **CloudAI Vision**, incluindo boas práticas e gatilhos configurados para as funções Lambda.

---

## 🪣 Bucket Name | Nome do Bucket

cloudai-vision-input


> **Note | Nota:**
> Bucket names must be globally unique.  
> Os nomes dos buckets devem ser globalmente únicos.

---

## 🧭 Folder Structure | Estrutura de Pastas

**English**  
You can use folders to separate images by project, type, or date — though this project works with flat key structure by default.

**Português**  
Você pode usar pastas para separar imagens por projeto, tipo ou data — embora este projeto funcione por padrão com estrutura de chave plana.

```bash
cloudai-vision-input/
├── gato-branco.jpg
├── img123.png
├── uploads/2024/05/foto1.jpeg
```
---

## ⚙️ Trigger Setup | Gatilho Configurado

A Lambda process-image-upload is triggered by any ObjectCreated:* event on this bucket.

---

## ✅ Sample Event | Exemplo de Evento (resumido)
```json
{
  "Records": [
    {
      "s3": {
        "bucket": {
          "name": "cloudai-vision-input"
        },
        "object": {
          "key": "uploads/foto1.jpg"
        }
      }
    }
  ]
}
```
---

## 🔐 Permissions | Permissões

The Lambda function must have read access to this bucket.
A função Lambda deve ter acesso de leitura a este bucket.
```json
{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::cloudai-vision-input/*"
}
```
---

✅ Tip: You can enable versioning or lifecycle rules to archive or clean up old images.

✅ Dica: Você pode ativar versionamento ou regras de ciclo de vida para arquivar ou excluir imagens antigas.

---
