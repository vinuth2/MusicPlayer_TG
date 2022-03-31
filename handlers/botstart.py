from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from handlers import __version__
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
    await message.reply_text(
        f"""───「[Princess Stella](https://telegra.ph/file/cc41cf2eebde1c4c0a0dd.jpg)」───
**Hey there! I am your SweetHeart, Stella Robot** ✨
I Play and Download music on Telegram. To know how to use me, click on the **Initial Setup** button below!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚙️ Initial Setup", callback_data="cbhowtouse"),
                ],
                [
                    InlineKeyboardButton("❓ Help", callback_data="cbcmds"),
                    InlineKeyboardButton("💬 Support", url=f"https://t.me/MusicUpdates_Chat"),
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add me to your chat", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
            ]
        ),
        disable_web_page_preview=False,
    )


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def start_group(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("💬 Support", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📣 Updates", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Hey there, I'm Stella**\n\n• Bot is working normally\n• My Master: [Vinuth](https://t.me/ImVinuth)\n• Bot Version: `v{__version__}`\n• Pyrogram Version: `{pyrover}`\n• Python Version: `{__python_version__}`\n• Uptime Status: `{uptime}`\n\n Thank you for using our Services! ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""Press the button below to read the explanation and see the list of available commands!""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="⚙️ Initial Setup", callback_data="cbguide")]]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("Pinging Network speed...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`\n"f"👤`Dev : Vinuth`\n"f"💻`Server : Heroku`\n\n"f"`Database : Mongodb`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 Stella girl status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
