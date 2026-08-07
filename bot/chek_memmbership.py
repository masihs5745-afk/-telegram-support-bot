from aiogram import Bot


CHANNEL_USERNAME = "@mohrehmarradobargh"


async def check_membership(bot: Bot, user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(
            chat_id=CHANNEL_USERNAME,
            user_id=user_id
        )

        return member.status in [
            "member",
            "administrator",
            "creator"
        ]

    except Exception:
        return False