from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from bot.utils.states import OrderState
from bot.database.database import add_order


router = Router()


@router.message(Text("🛒 ثبت سفارش"))
async def order_start(message: Message, state: FSMContext):
    await message.answer(
        "لطفاً نام خود را وارد کنید:"
    )

    await state.set_state(OrderState.name)


@router.message(OrderState.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await message.answer(
        "شماره تماس خود را وارد کنید:"
    )

    await state.set_state(OrderState.phone)


@router.message(OrderState.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)

    await message.answer(
        "توضیحات سفارش را وارد کنید:"
    )

    await state.set_state(OrderState.description)


@router.message(OrderState.description)
async def get_description(message: Message, state: FSMContext):
    data = await state.get_data()

    await add_order(
        user_id=message.from_user.id,
        name=data["name"],
        phone=data["phone"],
        description=message.text
    )

    await message.answer(
        "✅ سفارش شما با موفقیت ثبت شد."
    )

    await state.clear()
