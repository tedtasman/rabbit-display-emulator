# Rabbit Display Emulator

Emulates a hypothetical display which receives updates via RabbitMQ. Intended as a development tool for future work.

<img width="302" height="170" alt="Screenshot 2026-11-15 at 6 49 18 PM" src="https://github.com/user-attachments/assets/2ace396a-400b-4ffa-b06e-f59eb65035b8" />

<img width="302" height="170" alt="Screenshot 2026-11-15 at 6 48 57 PM" src="https://github.com/user-attachments/assets/8ce8ba4c-bcf8-4b7c-8268-003ee6391e49" />


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

