# re_aiogram

**re_aiogram** is a lightweight wrapper over [aiogram 3.x](https://aiogram.dev/) that keeps the familiar aiogram API while simplifying bot development and adding extra features.

The goal of the project is to stay fully compatible with aiogram, but provide a cleaner and more convenient developer experience.

---

# Install

```bash
pip install re_aiogram
````

```python
import re_aiogram
```

---

# Features

* familiar aiogram-style API
* simplified bot startup without explicit dispatcher
* router auto-loading
* built-in MediaGroup support
* aiogram-compatible imports

---

# Quick Start

```python
from re_aiogram import Bot, Message
from re_aiogram.filters import Command

API_TOKEN = "YOUR_API_TOKEN"

bot = Bot(token=API_TOKEN)


@bot.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Hi! I am a Telegram bot powered by re_aiogram!"
    )


bot.run(logging_enabled=True)
```

---

# MediaGroup Handler

Built-in support for Telegram media groups.

```python
from re_aiogram import Bot, Message
from re_aiogram.filters import F
from re_aiogram.types import MediaGroup

bot = Bot(token="TOKEN")


@bot.message(F.media_group_id)
async def handle_album(message: Message, media_group: MediaGroup):
    await message.answer_media_group(media_group)
```

`media_group` contains the collected media group messages.

## Properties

| Property                | Description                                                                                                                            |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `media_group.count`     | Returns the number of media items in the group.                                                                                        |
| `media_group.caption`   | Returns the first caption found in the group (Telegram sends caption only on the first item). Returns `None` if no caption is present. |
| `media_group.captions`  | Returns a list of all captions from the group.                                                                                         |
| `media_group.messages`  | Returns a copy of the original `Message` objects from the group.                                                                       |
| `media_group.photos`    | Returns a list of `Message` objects that contain photos.                                                                               |
| `media_group.videos`    | Returns a list of `Message` objects that contain videos.                                                                               |
| `media_group.documents` | Returns a list of `Message` objects that contain documents.                                                                            |
| `media_group.audio`     | Returns a list of `Message` objects that contain audio files.                                                                          |
| `media_group.is_mixed`  | Returns `True` if the album contains different media types (e.g., photos and videos together).                                         |

---

# Routers

Router connection is simplified with `bot.load()`

## Project structure

```text
project/
│
├── main.py
└── handlers/
    └── start.py
```

### main.py

```python
from re_aiogram import Bot

API_TOKEN = "YOUR_API_TOKEN"

bot = Bot(token=API_TOKEN)

bot.load("handlers.start")

bot.run(logging_enabled=True)
```

### handlers/start.py

```python
from re_aiogram import router, Message
from re_aiogram.filters import Command


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Router connected!")
```

---

# Future improvements

These features are planned for upcoming versions and are not yet part of the core API.

## Flow System (FSM alternative)

A lightweight state/flow system replacing traditional FSM:

* step-based flow control
* `ctx.next()` and `ctx.back()`
* shared `ctx.data`
* parallel flows via `scope()`
* simple chain-based conversation handling

Example concept:

```python
@router.message(Command("register"))
async def register(message: Message, ctx: FlowContext):
    await message.answer("What is your name?")
    ctx.next(get_name)
```

---

# Philosophy

re_aiogram tries to make Telegram bot development:

* simpler
* cleaner
* less boilerplate-heavy
* more beginner-friendly

while still preserving compatibility with the `aiogram` ecosystem.

---

# License

`MIT License`
