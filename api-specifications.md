# 🌐 API Specifications | Especificações da API

Este documento descreve o endpoint público da API utilizada no projeto **CloudAI Vision** para consultar resultados de análise de imagens.

---

## 🚀 Endpoint: GET /analyze/{imageKey}

| Campo         | 🇬🇧 Descrição                              | 🇧🇷 Descrição                                   |
|---------------|--------------------------------------------|------------------------------------------------|
| **Method**    | GET                                         | GET                                            |
| **Path**      | `/analyze/{imageKey}`                      | `/analyze/{imageKey}`                         |
| **Query Type**| Path Parameter                              | Parâmetro de Caminho                           |
| **Response**  | JSON containing image key and label list    | JSON com a chave da imagem e lista de rótulos  |

---

## ✅ Example Request | Exemplo de Requisição

```http
GET https://your-api-id.execute-api.region.amazonaws.com/prod/analyze/cachorro.png
```
---

## ✅ Example Response | Exemplo de Resposta
```json
{
  "imageKey": "cachorro.png",
  "labels": [
    "Dog",
    "Pet",
    "Animal",
    "Canine"
  ]
}
```
---

## ⚠️ Error Responses | Respostas de Erro

| Status Code | 🇬🇧 Message                      | 🇧🇷 Mensagem                             |
|-------------|----------------------------------|------------------------------------------|
| 404         | Image analysis not found         | Análise de imagem não encontrada         |
| 500         | Internal server error (exception)| Erro interno do servidor (exceção)       |

---

## 🔐 Authentication

| 🇬🇧 Current State             | 🇧🇷 Estado Atual                           |
|------------------------------|--------------------------------------------|
| Public API, no authentication| API pública, sem autenticação              |
| *(Optional: API Key or JWT)* | *(Opcional: chave de API ou JWT)*         |

---

✅ Tip: Use Postman or browser for quick testing.

✅ Dica: Use o Postman ou navegador para testes rápidos.

---
