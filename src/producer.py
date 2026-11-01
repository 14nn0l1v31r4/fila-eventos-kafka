import json
import random
import time
import uuid

from confluent_kafka import Producer


BROKER = "localhost:9092"
TOPIC = "pedidos"
CUSTOMERS = [f"cliente-{number}" for number in range(1, 6)]


def report_delivery(error, message):
    if error is not None:
        print(f"Falha ao enviar pedido: {error}")
        return

    print(
        f"Pedido enviado: partição={message.partition()} "
        f"offset={message.offset()}"
    )


def main():
    producer = Producer({"bootstrap.servers": BROKER})
    print(f"Enviando pedidos para {TOPIC}. Ctrl+C encerra.")

    try:
        while True:
            order_id = f"pedido-{uuid.uuid4().hex[:8]}"
            customer_id = random.choice(CUSTOMERS)
            order = {
                "pedido_id": order_id,
                "cliente_id": customer_id,
                "tipo": "PedidoCriado",
                "total": round(random.uniform(10, 150), 2),
            }

            producer.produce(
                TOPIC,
                key=customer_id.encode("utf-8"),
                value=json.dumps(order).encode("utf-8"),
                callback=report_delivery,
            )
            producer.poll(0)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nEncerrando produtor...")
    finally:
        producer.flush()


if __name__ == "__main__":
    main()
