from .init import curs, IntegrityError
from model.creature import Creature
from errors.errors import Missing, Duplicate

curs.execute("""CREATE TABLE IF NOT EXISTS creature(
    name TEXT PRIMARY KEY,
    description TEXT,
    location TEXT
);""")

def row_to_model(row: tuple) -> Creature:
    return Creature(name=row[0], description=row[1], location=row[2])

def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()

def get_one(name: str) -> Creature:
    qry = "SELECT * FROM creature WHERE name=:name;"
    params = {"name": name}
    res = curs.execute(qry, params).fetchone()
    if res:
        return row_to_model(res)
    else:
        raise Missing(f"Creature {name} not found")

def get_all() -> list[Creature]:
    qry = "SELECT * FROM creature;"
    return [row_to_model(row) for row in curs.execute(qry).fetchall()]

def create(creature: Creature) -> Creature:
    qry = "INSERT INTO creature VALUES (:name,:description,:location);"
    params = model_to_dict(creature)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(f"Creature {creature.name} already exists")
    return get_one(creature.name)

def modify(name: str, creature: Creature) -> Creature:
    qry = """UPDATE creature
    SET name=:name,
    description=:description,
    location=:location
    WHERE name=:name0;"""
    params = model_to_dict(creature)
    params["name0"] = creature.name
    res = curs.execute(qry, params)
    if res.rowcount == 1:
        return get_one(creature.name)
    else:
        raise Missing(f"Creature {name} not found")

def delete(name: str) -> bool:
    if not name: return False
    qry = "DELETE FROM creature WHERE name=:name;"
    params = {"name": name}
    res = curs.execute(qry, params)
    if res.rowcount != 1:
        raise Missing(f"Crteature {name} not found")