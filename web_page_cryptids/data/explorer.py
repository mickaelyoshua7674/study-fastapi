from .init import curs, IntegrityError
from model.explorer import Explorer
from ..errors import Missing, Duplicate

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
    res = curs.execute(qry, params).fetchone()
    if res:
        return row_to_model(res)
    else:
        raise Missing(f"Explorer {name} not found")

def get_all() -> list[Explorer]:
    qry = "SELECT * FROM explorer;"
    return [row_to_model(row) for row in curs.execute(qry).fetchall()]

def create(explorer: Explorer) -> Explorer:
    qry = "INSERT INTO explorer VALUES (:name,:nationality);"
    params = model_to_dict(explorer)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(f"Explorer {explorer.name} already exists")
    return get_one(explorer.name)

def modify(name: str, explorer: Explorer) -> Explorer:
    qry = """UPDATE explorer
    SET name=:name,
    nationality=:nationality
    WHERE name=:name0;"""
    params = model_to_dict(explorer)
    params["name0"] = explorer.name
    res = curs.execute(qry, params)
    if res.rowcount == 1:
        return get_one(explorer.name)
    else:
        raise Missing(f"Explorer {name} not found")

def delete(name: str) -> bool:
    if not name: return False
    qry = "DELETE FROM explorer WHERE name=:name;"
    params = {"name": name}
    res = curs.execute(qry, params)
    if res.rowcount != 1:
        raise Missing(f"Explorer {name} not found")