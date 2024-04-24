import asyncio
import logging
from aiogram import Router, F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from stata import Stata

from botdb import Bd

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6502448978:AAFtpo_1sUCg_zP_2p5xLZjOYxGhvYYRLZk")
router = Router()
dp = Dispatcher()
dp.include_router(router)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer('Добро пожаловать! Этот бот может найти для тебя множество книг, тебе стоит только попросить об этом!')


@dp.message(Command('help'))
async def help(message: types.Message):
    await message.answer('Воспользуйтесь функцией "find_me_a_book" и найдите нужную вам книгу.\nЕсли хотите ознакомиться с кратким содержанием произведения, воспользуйтесь функцией "summary".')


@dp.message(Command('what_to_do'))
async def what(message: types.Message):
    markup = InlineKeyboardBuilder()
    sum = types.InlineKeyboardButton(text='Прочитать краткое содержание', callback_data='summary')
    find = types.InlineKeyboardButton(text='Получить нужную книгу', callback_data='find')
    markup.add(sum, find)
    await message.answer('Чего желаете?', reply_markup=markup.as_markup())


@dp.callback_query(F.data == "summary")
async def summary(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Напишите название книги')
    await state.set_state(Stata.get_link)


@dp.message(Stata.get_link, F.text)
async def site(message: types.Message, state: FSMContext):
    words = message.text.strip()
    builder = InlineKeyboardBuilder()
    but = types.InlineKeyboardButton(text='Перейти на сайт', url=Bd().get_site(words))
    builder.add(but)
    await message.answer('Нажмите', reply_markup=builder.as_markup())
    await state.set_state(Stata.get_book)


@dp.callback_query(F.data == 'find')
async def find(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Напишите название или автора книги')
    await state.set_state(Stata.get_book)

@dp.message(Stata.get_book, F.text)
async def book(message: types.Message, state: FSMContext):
    words = message.text.strip()
    if len(Bd().find(words)) == 1:
        await message.answer_document(document=FSInputFile(Bd().find(words)[0][1]), caption="Наслаждайтесь!")
        await message.answer_document(document=FSInputFile(Bd().picture(words)))
        await state.set_state(Stata.get_link)

    elif len(Bd().find(words)) == 0:
         await message.answer('Такой файл не найден')
         await state.set_state(Stata.get_link)

    elif len(Bd().find(words)) > 1:
        markup = InlineKeyboardBuilder()
        for i in range(len(Bd().find(words))):
            button = types.InlineKeyboardButton(text=f'{Bd().find(words)[i][0]}', callback_data=f'{Bd().find(words)[i][0]}')
            markup.add(button)
        await message.answer('Выберите файл:', reply_markup=markup.as_markup())
        await state.set_state(Stata.get_link)

@dp.callback_query()
async def buttons(call: types.CallbackQuery):
    file = call.data
    await call.message.answer_document(document=FSInputFile(Bd().give_file(file)))
    await call.message.answer_document(document=FSInputFile(Bd().picture(file)))

@dp.message(F.text)
async def site(message: types.Message):
    words = message.text.strip()
    builder = InlineKeyboardBuilder()
    but = types.InlineKeyboardButton(text='Перейти на сайт', url=Bd().get_site(words))
    builder.add(but)
    await message.answer('Нажмите', reply_markup=builder.as_markup())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())