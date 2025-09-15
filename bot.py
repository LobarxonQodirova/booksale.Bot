# from aiogram import F, Router
# from aiogram.filters import Command
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.types import Message, CallbackQuery, FSInputFile
# from aiogram.enums import ParseMode
# from aiogram.client.default import DefaultBotProperties
#
# from config import TOKEN
# from logs.logger import log_action
# from tugmachalar import *
#
# router = Router()
#
#
# class Buyurtmalar(StatesGroup):
#     name = State()
#     address = State()
#     phone = State()
#
#
#
# @router.message(Command("start"))
# async def cmd_start(message: Message):
#     log_action(message.from_user, "/start kamandasi bosildi")
#     await message.answer(f"<i>Assalomu alaykum hurmatli foydalanuvchi, bizning online Kitoblar  botimizga xush kelibsiz<i>", reply_markup = menyu)
# @router.message(Command("help"))
# async def cmd_help_command(message: Message):
#     log_action(message.from_user, "/help komandasi bosildi")
#     await message.delete()
#     await message.answer("ℹ️ Agar yordam kerak bo‘lsa: @L🎀")
#
#
# @router.message(Command("catalog"))
# async def cmd_catalog_command(message: Message):
#     log_action(message.from_user, "/catalog komandasi bosildi")
#     await message.delete()
#     await message.answer("📚Kitoblardan birini tanlang:", reply_markup=inline_katalog)
#
# @router.callback_query(F.data == "help")
# async def cmd_help(callback: CallbackQuery):
#     log_action(callback.from_user, "Yordam tugmasi bosildi")
#     await callback.message.delete()
#     await callback.message.answer("ℹ️ Agar yordam kerak bo‘lsa: @L🎀", reply_markup=menyu)
#
#
# @router.callback_query(F.data == "back_main")
# async def cmd_back_main(callback: CallbackQuery):
#     log_action(callback.from_user, "Ortga (asosiy menyu) tugmasi bosildi")
#     await callback.message.delete()
#     await callback.message.answer("🏠 Asosiy menyuga qaytdik", reply_markup=menyu)
#
#
# @router.message(Command("Send"))
# async def cmd_send_photo(message: Message):
#     log_action(message.from_user, "/send komandasi bosildi")
#     await message.delete()
#     photos = FSInputFile("photos/clck.ru/3P6qoh")
#     await message.answer_photo(photo=photocha, caption="Bizning yangi rasmmizga nazar soling! 🎥📚")
#
#
# @router.callback_query(F.data == "Yashamoq_kitobi")
# async def cmd_kitoblar(callback: CallbackQuery):
#     log_action(callback.from_user, "Yashamoq_kitobi tanalandi!")
#     image1 = FSInputFile("photos/clck.ru/3P6qoh")
#     await callback.message.answer_photo( photo = image1, caption=" 📚Yashamoq kitobi - 79.000 so'm\n", reply_markup=buyurtma)
#
#
# @router.callback_query(F.data == "Men_kitobi")
# async def cmd_Men_kitobi(callback: CallbackQuery):
#     log_action(callback.from_user, "Men kitobi tanlandi")
#     image2 = FSInputFile("rasmlar/Men.jpg")
#     await callback.message.delete()
#     await callback.message.answer_photo( photo = image2, caption="- 📚 100.000 so‘m", reply_markup=buyurtma)
#
#
# @router.callback_query(F.data == "Hokimyatning_48_qoidasi")
# async def cmd_hokimyatning_48_qoidasi(callback: CallbackQuery):
#     log_action(callback.from_user, "Hokimyatning_48_qoidasi")
#     image3 = FSInputFile("rasmlar/Hokimyatning_48_qoidasi.jpg")
#     await callback.message.delete()
#     await callback.message.answer_photo( photo = image3, caption="📚Hokimyatning 48 qoidasi - 115.000 so‘m", reply_markup=buyurtma
