import aiosqlite

DB_NAME = "bot.db"


async def save_support_message(
    user_id: int,
    message_id: int
):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS support_messages (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            message_id INTEGER
        )
        """)

        await db.execute(
            """
            INSERT INTO support_messages
            (user_id, message_id)
            VALUES (?, ?)
            """,
            (user_id, message_id)
        )

        await db.commit()
