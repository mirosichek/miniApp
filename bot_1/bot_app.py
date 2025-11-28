import asyncio
from aiogram import Bot, Dispatcher
from bot_1.registrtion import registration_router
from bot_1.Inline_kbs import quiz_ruoter

class BotApp:
    def __init__(self, token, db):
        self.bot = Bot(token)
        self.db = db
        self.dp = Dispatcher()
        self.dp.include_router(registration_router)
        self.dp.include_router(quiz_ruoter)

    


    async def run(self):
        print("Бот запущен!")
        await self.dp.start_polling(self.bot)
