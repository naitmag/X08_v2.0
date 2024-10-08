from aiogram import Router, F
from aiogram.enums import ChatType
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.utils import Provider
from schedule.models import Week

router = Router()
router.message.filter(~F.forward_from & ~F.forward_from_chat)


# /start
@router.message(F.chat.type == ChatType.PRIVATE, CommandStart())
async def cmd_start(message: Message):
    image = Provider.get_image('messages.start.img')
    text = Provider.get_text('messages.start.text')
    await message.answer_photo(photo=image, caption=text)


# /schedule [week] , /s [week]
@router.message(F.chat.type == ChatType.PRIVATE, Command('schedule', 's'))
async def cmd_schedule(message: Message):
    args = message.text.split()
    if len(args) < 2:
        week_number = None
    else:
        week_number = args[1]
    week = Week(week_number)
    text = week.format_schedule()
    await message.answer(text)
