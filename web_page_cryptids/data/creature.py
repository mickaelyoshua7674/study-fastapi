import sqlite3
from model.creature import Creature

DB_NAME = "cryptid.db"
_conn = sqlite3.connect(DB_NAME)
curs = _conn.cursor()

def init():
    curs.execute("CREATE TABLE creature (name,description,location)")

def row_to_model(row: tuple) -> Creature:
    return Creature(*row)

def rows_to_model(rows: list[tuple]) -> list[Creature]:
    return [row_to_model(row) for row in rows]

def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()

def get_one(name: str) -> Creature:
    qry = "SELECT * FROM creature WHERE name=:name"
    params = {"name": name}
    res = curs.execute(qry, params)
    row = curs.fetchone(res)
    return row_to_model(row)

def get_all() -> list[Creature]:
    qry = "SELECT * FROM creature"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return rows_to_model(rows)

def create(creature: Creature):
    qry = "INSERT INTO creature values (:name,:description,:location)"
    params = model_to_dict(creature)
    return curs.execute(qry, params)

def modify(creature: Creature):
    return creature

def replace(creature: Creature):
    return creature

def delete(creature: Creature):
    qry = "DELETE FROM creature WHERE name=:name"
    params = {"name": creature.name}
    return curs.execute(qry, params)