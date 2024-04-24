from aiogram.fsm.state import StatesGroup, State

class Stata(StatesGroup):
    get_link = State()
    get_book = State()