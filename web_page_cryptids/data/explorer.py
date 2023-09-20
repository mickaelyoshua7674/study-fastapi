from .init import curs
from model.explorer import Explorer

curs.execute("""CREATE TABLE IF NOT EXISTS explorer(
    name TEXT PRIMARY KEY,
    nationality TEXT
);""")

def row_to_model(row: tuple) -> Explorer:
    return Explorer(name=row[0], nationality=row[1])

def model_to_dict(explorer: Explorer) -> dict:
    return explorer.model_dump()

def get_one(name: str) -> Explorer:
    qry = "SELECT * FROM explorer WHERE name=:name;"
    params = {"name": name}
    return row_to_model(curs.execute(qry, params).fetchone())

def get_all() -> list[Explorer]:
    qry = "SELECT * FROM explorer;"
    return [row_to_model(row) for row in curs.execute(qry).fetchall()]

def create(explorer: Explorer) -> Explorer:
    qry = "INSERT INTO explorer VALUES (:name,:nationality);"
    params = model_to_dict(explorer)
    curs.execute(qry, params)
    return get_one(explorer.name)

def modify(explorer: Explorer) -> Explorer:
    qry = """UPDATE explorer
    SET name=:name,
    nationality=:nationality
    WHERE name=:name0;"""
    params = model_to_dict(explorer)
    params["name0"] = explorer.name
    curs.execute(qry, params)
    return get_one(explorer.name)

def delete(explorer: Explorer) -> bool:
    qry = "DELETE FROM explorer WHERE name=:name;"
    params = {"name": explorer.name}
    return bool(curs.execute(qry, params))