from typing import Optional, Union, List, Tuple
import decimal

import asyncpg

from src.types import TGChatID, TGUsername
from config import Config

class DB:
    """
    <<<--------------------------------------------------->>>
    table = user_model
        id: Integer Primary Key
        username: String(256) DEFAULT = NULL
        balance: decimal NOT NULL UNIQUE = TRUE DEFAULT = 0.0
    <<<--------------------------------------------------->>>
    """
    @staticmethod
    async def _select_method(sql: str, data: Optional[Union[List, Tuple]] = ()):
        try:
            with await asyncpg.connect(Config.DATABASE_URL) as connection:
                return await connection.fetch(sql, data)
        except Exception as error:
            raise error

    @staticmethod
    async def _insert_method(sql: str, data: Optional[Union[List, Tuple]] = ()) -> bool:
        try:
            with await asyncpg.connect(Config.DATABASE_URL) as connection:
                await connection.execute(sql, data)
                await connection.commit()
            return True
        except Exception as error:
            raise error

    @staticmethod
    async def user_exists(user_id: TGChatID) -> bool:
        return bool(len(await DB._select_method("SELECT * FROM user_model WHERE id = 1$;", (user_id,))))

    @staticmethod
    async def add_user(user_id: TGChatID, username: TGUsername) -> bool:
        return await DB._insert_method("INSERT INTO user_model (id, username) VALUES ($1, $2);", (user_id, username))

    @staticmethod
    async def get_user_balance(user_id: TGChatID) -> decimal.Decimal:
        return await DB._select_method("SELECT balance FROM user_model WHERE id = 1$;", (user_id,))

    @staticmethod
    async def set_user_balance(user_id: TGChatID, balance: decimal.Decimal) -> bool:
        return await DB._insert_method("UPDATE user_model SET balance = 1$ WHERE id = $2", (balance, balance))