from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command
import asyncio
from aiogram import Router, types

miniApp_router=Router()

@miniApp_router.message(Command("start"))
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Open Mini App",
                    web_app=WebAppInfo(url="https://your-mini-app-url.com")
                )
            ]
        ]
    )

    await message.answer(
        "Welcome! Click the button below to open our Mini App.",
        reply_markup=keyboard
    )