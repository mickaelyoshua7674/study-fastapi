from model.explorer import Explorer
import data.explorer as data

def get_one(name: str) -> Explorer:
    return data.get_one(name)

def get_all() -> list[Explorer]:
    return data.get_all()

def create(explorer: Explorer) -> Explorer:
    return data.create(explorer)

def modify(name: str, explorer: Explorer) -> Explorer:
    return data.modify(name, explorer)

def delete(name: str) -> bool:
    return data.delete(name)