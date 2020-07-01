from typing import List, Optional

from gino.ext.starlette import Gino


async def existing_database(db: Gino, name: Optional[str]) -> bool:
    """ Return the names of existing database """

    query: str = """
        SELECT datname
        FROM pg_database;
    """
    raws: List = await db.all(db.text(query))
    for raw in raws:
        if raw[0] == name:
            return True
    return False
