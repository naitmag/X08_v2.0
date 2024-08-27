from aiogram import Router, F
from aiogram.enums import ChatType
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.models import Provider

router = Router()
router.message.filter(~F.forward_from & ~F.forward_from_chat)


@router.message(F.chat.type == ChatType.PRIVATE, CommandStart())
async def cmd_start(message: Message):
    image = Provider.get_image('start.img')
    text = Provider.get_text('start.text')
    await message.answer_photo(photo=image, caption=text)
