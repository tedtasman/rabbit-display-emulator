# Rabbit Display Emulator

Emulates a hypothetical display which receives updates via RabbitMQ. Intended as a development tool for future work.

## Requirements

- RabbitMQ
- uv

## Usage

Clone:

```bash
git clone https://github.com/tedtasman/rabbit-display-emulator.git
cd rabbit-display-emulator
```

Setup:

```bash
uv sync
```

Run emulator:

```bash
uv run ./emulator.py # displays on localhost:8080
```

Run test:

```bash
uv run ./test/send.py
```

