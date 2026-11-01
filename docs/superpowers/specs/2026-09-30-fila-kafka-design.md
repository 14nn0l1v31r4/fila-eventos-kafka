# Fila de eventos Kafka — desenho

## Objetivo

Projeto didático pequeno em Python para publicar pedidos falsos no Kafka e calcular total de vendas num consumidor.

## Fluxo

`producer.py` cria pedidos JSON e publica no tópico `pedidos`, usando `cliente_id` como chave. Pedidos do mesmo cliente seguem para a mesma partição. Kafka local roda em um broker KRaft com três partições. `consumer.py` lê do grupo `resumo-vendas` e mantém soma em memória.

## Limites do MVP

- Um broker local, sem replicação ou alta disponibilidade.
- Eventos têm `pedido_id`, `cliente_id`, `tipo` e `total`.
- Consumidor imprime cada pedido e total acumulado.
- Sem banco, interface, Schema Registry ou processamento exatamente uma vez.
- Python usa `confluent-kafka`; Kafka roda via Docker Compose.

## Como executar

Subir Kafka com `docker compose up -d`, instalar dependência em ambiente virtual, então executar produtor e consumidor em terminais separados. O README explica que a soma do consumidor é volátil e pode ser recalculada relendo eventos.
