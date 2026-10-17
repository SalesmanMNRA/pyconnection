```markdown
# 🚀 pyconnection

**The fastest, most elegant way to build Soroush Plus bots.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/badge/PyPI-coming_soon-orange?style=flat-square&logo=pypi)](https://pypi.org/)

`pyconnection` is a zero-bullshit, high-performance Python SDK for the Soroush Plus API. Built on top of `requests` with connection pooling, auto-retries, and a clean async-ready interface. Stop fighting HTTP boilerplate — start building your bot.

---

## ⚡ Features

- 🔥 **Blazing Fast** — Pooled `requests.Session` under the hood (5x faster than raw HTTP requests).
- 🔄 **Auto-Healing** — Built-in retries with exponential backoff on `429` and `5xx` errors.
- 🤖 **Bot-Ready** — Instant async helpers for `send_message`, `get_me`, and inline keyboards.
- 🛡️ **Bulletproof** — Safe token loading via environment variables.
- 🧩 **Minimalist** — No bloat. Import only what you need.

---

## 📦 Installation

**Install directly from GitHub (Latest & Greatest):**

```bash
pip install git+https://github.com/salesmanmnra/pyconnection.git
```

**Or for development:**

```bash
git clone https://github.com/salesmanmnra/pyconnection.git
cd pyconnection
pip install -e .
```

---

## 🚀 Quickstart

### The "It Just Works" Bot Example

```python
import os
import asyncio
from pyconnection import PYConnectionClient

# Load securely from your .env
BOT_TOKEN = os.getenv("SPLUS_BOT_TOKEN")

client = PYConnectionClient(
    api_id=12345,
    api_hash="your_hash",
    phone_number="+98...",
    session_name="my_bot"
)

async def main():
    # Get user info
    me = await client.get_me()
    print(f"Logged in as: {me['username']}")
    
    # Send a message instantly
    await client.send_message("username", "Hello, Soroush!")

asyncio.run(main())
```

### Raw HTTP Requests (No Client Needed)

```python
from pyconnection import get, post

# GET
r = get("https://api.splus.ir/bot<token>/getMe")

# POST with JSON
r = post("https://api.splus.ir/bot<token>/sendMessage", json={
    "chat_id": "123",
    "text": "Ping!"
})

print(r.json())
```

---

## 🧠 API Reference

### Core Client

| Method | Description |
|--------|-------------|
| `PYConnectionClient(...)` | Initialize the core client |
| `.http_get()` / `.http_post()` | Native HTTP shortcuts |
| `.send_message(user, text)` | Async Soroush Plus message sender |
| `.get_me()` | Async user profile fetcher |

### Module-Level Shortcuts

| Function | Import |
|----------|--------|
| `get()` | `from pyconnection import get` |
| `post()` | `from pyconnection import post` |
| `put()` / `delete()` | `from pyconnection.requests_utils import put, delete` |
| `configure_session()` | `from pyconnection.requests_utils import configure_session` |

---

## 🔐 Security & Config

Never hardcode your tokens. Use a `.env` file:

```env
SPLUS_BOT_TOKEN=123456:ABC-DEF...
```

```python
import os
token = os.getenv("SPLUS_BOT_TOKEN")
```

---

## 🤝 Contributing

Contributions are what make open source amazing. Read `CONTRIBUTING.md` to get started.

---

## 📄 License

MIT License. Do whatever you want, just don't blame us.

---
**Author:** [SalesmanMNRA](https://github.com/salesmanmnra) • **Repo:** [pyconnection](https://github.com/salesmanmnra/pyconnection)
```
