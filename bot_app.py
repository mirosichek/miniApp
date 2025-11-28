import asyncio
from aiogram import Bot, Dispatcher
from registrtion import registration_router
from Inline_kbs import quiz_ruoter
from miniApp import miniApp_router

class BotApp:
    def __init__(self, token, db):
        self.bot = Bot(token)
        self.db = db
        self.dp = Dispatcher()
        self.dp.include_router(registration_router)
        self.dp.include_router(quiz_ruoter)
        self.dp.include_router(miniApp_router)

    


    async def run(self):
        print("Бот запущен!")
        await self.dp.start_polling(self.bot)
