import os, asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8200244117:AAF7l93IVbJ_SOq7GWrdmwPnsKf_JF57zQY"
if not TOKEN:
    raise RuntimeError("ENV var TELEGRAM_TOKEN is missing")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет ✨ Я Adelin Viral Bot! Напиши /idea — пришлю промт.")

@dp.message(Command("idea"))
async def idea_handler(message: types.Message):
    prompt = (
        "Ultra-realistic fashion editorial shot: young woman (use reference face 100%), "
        "standing in neon-lit city, giant Prada handbag behind her, strong motion blur in crowd, "
        "luxury cinematic style, 9:16."
    )
    await message.answer(f"Вот твой вирусный промт:\n\n{prompt}")

async def main():
    print("🤖 Бот запускается на Render…")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
