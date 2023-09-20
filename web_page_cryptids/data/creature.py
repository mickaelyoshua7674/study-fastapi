from init import curs
from model.creature import Creature

curs.execute("""CREATE TABLE IF NOT EXISTS creature(
    name TEXT PRIMARY KEY,
    description TEXT,
    location TEXT
);""")

def row_to_model(row: tuple) -> Creature:
    return Creature(*row)

def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()

def get_one(name: str) -> Creature:
    qry = "SELECT * FROM creature WHERE name=:name;"
    params = {"name": name}
    curs.execute(qry, params)
    return row_to_model(curs.fetchone())

def get_all() -> list[Creature]:
    qry = "SELECT * FROM creature;"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(creature: Creature) -> Creature:
    qry = "INSERT INTO creature VALUES (:name,:description,:location);"
    params = model_to_dict(creature)
    curs.execute(qry, params)
    return get_one(creature.name)

def modify(creature: Creature) -> Creature:
    qry = """UPDATE creature
    SET name=:name,
    description=:description,
    location=:location
    WHERE name=:name0;"""
    params = model_to_dict(creature)
    params["name0"] = creature.name
    curs.execute(qry, params)
    return get_one(creature.name)

def delete(creature: Creature) -> bool:
    qry = "DELETE FROM creature WHERE name=:name;"
    params = {"name": creature.name}
    return bool(curs.execute(qry, params))