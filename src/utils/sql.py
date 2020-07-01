

async def existing_database(db, name) -> bool:
    """ Return the names of existing database """
    
    query = """
        SELECT datname
        FROM pg_database;
    """
    raws = await db.all(db.text(query))
    for raw in raws:
        if raw[0] == name:
            return True
    return False