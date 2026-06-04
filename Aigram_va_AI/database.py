import aiosqlite


DB_NAME = "users.db"


async def create_table():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                username TEXT
            )
        """)
        await db.commit()


async def add_user(
        user_id: int,
        first_name: str,
        last_name: str,
        username: str
):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            INSERT OR REPLACE INTO users
            (user_id, first_name, last_name, username)
            VALUES (?, ?, ?, ?)
        """, (
            user_id,
            first_name,
            last_name,
            username
        ))
        await db.commit()