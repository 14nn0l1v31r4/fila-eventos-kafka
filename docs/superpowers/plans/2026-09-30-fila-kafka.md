# Fila de eventos Kafka Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use inline execution with task-by-task checkpoints.

**Goal:** Build a small Python pipeline that publishes mock orders to Kafka and prints a running sales total.

**Architecture:** A Docker Compose Kafka broker exposes port 9092. A Python producer writes JSON events keyed by order ID; a consumer group reads them and aggregates totals in memory.

**Tech Stack:** Python 3.13+, confluent-kafka, Apache Kafka Docker image, Docker Compose.

**Spec:** `docs/superpowers/specs/2026-09-30-fila-kafka-design.md`

## Global Constraints

- Keep one broker and no external database.
- Use three partitions for the `pedidos` topic.
- Keep producer and consumer runnable as separate Python modules.
- Document setup and limits in README.

---

### Task 1: Local Kafka setup and instructions

**Files:**
- Create: `docker-compose.yml`
- Create: `README.md`
- Create: `requirements.txt`
- Create: `.gitignore`

- [x] Add a single-node KRaft Kafka Compose service with host port 9092.
- [x] Ignore `.venv/` and Python bytecode cache files.
- [x] Document Windows PowerShell commands for virtual environment, dependency installation, startup, producer, consumer, and shutdown.
- [x] Explain that the aggregate is in memory and the local single broker is not highly available.

### Task 2: Event producer and consumer

**Files:**
- Create: `src/producer.py`
- Create: `src/consumer.py`

- [x] Producer creates JSON orders with `pedido_id`, `cliente_id`, `tipo`, and `total`, keyed by `cliente_id`.
- [x] Producer polls delivery callbacks and flushes before exit.
- [x] Consumer subscribes to `pedidos` as group `resumo-vendas`, decodes JSON and prints each order plus running total.
- [x] Consumer closes cleanly on Ctrl+C.

### Task 3: Finish development w/ final checks...

- [x] Review file scope and instructions for consistency.
- [x] No tests run; user did not request test or verification.
