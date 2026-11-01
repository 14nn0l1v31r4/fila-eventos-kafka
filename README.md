# Fila de eventos com Kafka

Produtor Python envia pedidos para Kafka; consumidor lê eventos e soma vendas.

## Requisitos

- Python 3.13 ou mais recente
- Docker Desktop com Docker Compose

## 1. Inicie Kafka

No PowerShell, dentro desta pasta:

```powershell
docker compose up -d
```

Kafka fica disponível em `localhost:9092`. O broker cria o tópico `pedidos` quando receber primeiro evento. Tópico tem três partições.

## 2. Prepare Python

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Se PowerShell bloquear ativação do ambiente virtual, rode os scripts sem ativar usando `.\.venv\Scripts\python.exe`.

## 3. Rode consumidor e produtor

Abra dois terminais PowerShell nesta pasta. Inicie consumidor primeiro:

```powershell
python .\src\consumer.py
```

No segundo terminal:

```powershell
python .\src\producer.py
```

Produtor envia um pedido a cada dois segundos. Pare cada processo com Ctrl+C.

## O que observar

- `cliente_id` é chave do evento. Kafka direciona pedidos do mesmo cliente à mesma partição, preservando ordem dentro dela.
- Partições permitem paralelismo. Com três partições, até três consumidores do mesmo grupo podem ler em paralelo.
- `resumo-vendas` identifica o grupo de consumidores. Offset registra posição de leitura do grupo.
- `auto.offset.reset=earliest` faz grupo novo começar pelos eventos retidos. Grupo existente retoma do offset salvo.

## Limites atuais

Kafka roda num broker único, sem tolerância a falha do broker. Dados ficam no container; `docker compose down` remove container e eventos. Total fica só na memória do processo; após reiniciar, não inclui vendas processadas antes. O consumidor confirma offsets automaticamente, então este exemplo não promete processamento exatamente uma vez. Esses são bons próximos passos para estudo.

## Encerrar Kafka

```powershell
docker compose down
```

Documentação: [Apache Kafka](https://kafka.apache.org/documentation/) · [Kafka Docker](https://github.com/apache/kafka/blob/trunk/docs/getting-started/docker.md) · [Cliente Python](https://github.com/confluentinc/confluent-kafka-python)
