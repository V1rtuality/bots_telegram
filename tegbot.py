import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart


bot = Bot(token="8689488400:AAGVWuHlFRLFNJlNLC-4UX15VJ5g1hm09Uw")
dp = Dispatcher()



@dp.message(CommandStart())
async def cmd_start(message: Message):
    
    await message.answer(f"Привет, {message.from_user.first_name}! я специально создал бота для исходника на гит хаб")



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())