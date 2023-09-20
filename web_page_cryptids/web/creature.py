from fastapi import APIRouter
from model.creature import Creature
import data.creature as service

router = APIRouter(prefix="/creature")

@router.get("") # add this so can return using '/creature'
@router.get("/") # this return using '/creature/'
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Creature | None:
    return service.get_one(name)

@router.post("")
@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create(creature)

@router.patch("/")
def modify(creature: Creature) -> Creature:
    return service.modify(creature)

@router.put("/")
def replace(creature: Creature) -> Creature:
    return service.replace(creature)

@router.delete("/{name}")
def delete(name: str):
    return service.delete(name)