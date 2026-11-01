import json

from confluent_kafka import Consumer, KafkaError


BROKER = "localhost:9092"
TOPIC = "pedidos"
GROUP_ID = "resumo-vendas"


def main():
    consumer = Consumer(
        {
            "bootstrap.servers": BROKER,
            "group.id": GROUP_ID,
            "auto.offset.reset": "earliest",
        }
    )
    consumer.subscribe([TOPIC])
    total = 0.0
    print(f"Lendo pedidos de {TOPIC}. Ctrl+C encerra.")

    try:
        while True:
            message = consumer.poll(1.0)
            if message is None:
                continue

            if message.error():
                if message.error().code() == KafkaError._PARTITION_EOF:
                    continue
                print(f"Erro ao ler mensagem: {message.error()}")
                continue

            order = json.loads(message.value().decode("utf-8"))
            total += order["total"]
            print(
                f"{order['pedido_id']} ({order['cliente_id']}): "
                f"R$ {order['total']:.2f} "
                f"| total nesta execução: R$ {total:.2f}"
            )
    except KeyboardInterrupt:
        print("\nEncerrando consumidor...")
    finally:
        consumer.close()


if __name__ == "__main__":
    main()
