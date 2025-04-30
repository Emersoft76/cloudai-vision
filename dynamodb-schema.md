# 🗃️ DynamoDB Schema | Esquema da Tabela DynamoDB

Este documento descreve a estrutura da tabela utilizada para armazenar os metadados de análise de imagem no projeto **CloudAI Vision**.

---

## 🧾 Table: `cloudai-vision-results`

| Attribute   | Type | 🇬🇧 Description                       | 🇧🇷 Descrição                              |
|-------------|------|----------------------------------------|---------------------------------------------|
| `imageKey`  | S    | Unique key (image filename)            | Chave única (nome do arquivo da imagem)     |
| `labels`    | L    | List of labels (objects, tags, etc.)   | Lista de rótulos (objetos, etiquetas etc.)  |

> **S = String**  
> **L = List**

---

## 🔐 Key Schema | Esquema de Chaves

```txt
Partition Key: imageKey (String)
```
---

## 🔄 Sample Item | Exemplo de Item
```json
{
  "imageKey": "gato-branco.jpg",
  "labels": [
    "Cat",
    "Pet",
    "Animal",
    "Feline"
  ]
}
```
---

## ⚠️ Notes | Notas

  * ⚡ The table uses on-demand capacity for simplicity and cost-efficiency.
  * ⚡ A tabela usa capacidade sob demanda, por simplicidade e economia.

  * All analysis results are overwritten if the same imageKey is uploaded again.
  * Os resultados são sobrescritos se a mesma imageKey for enviada novamente.
---
