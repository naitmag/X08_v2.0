from aiogram import Router, F
from aiogram.enums import ChatType
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.utils import Provider

router = Router()
router.message.filter(~F.forward_from & ~F.forward_from_chat)


@router.message(F.chat.type == ChatType.PRIVATE, CommandStart())
async def cmd_start(message: Message):
    image = Provider.get_image('start.img')
    text = Provider.get_text('start.text')
    await message.answer_photo(photo=image, caption=text)


@router.message(F.chat.type == ChatType.PRIVATE, Command('schedule', 's'))
async def cmd_schedule(message: Message):
    text = Provider.get_text('schedule.text')
    await message.answer(text)
