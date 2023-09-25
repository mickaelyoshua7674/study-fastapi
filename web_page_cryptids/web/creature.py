from fastapi import APIRouter, HTTPException
from model.creature import Creature
from service import creature as service
from errors.errors import Duplicate, Missing

router = APIRouter(prefix="/creature")

@router.get("") # add this so can return using '/creature'
@router.get("/") # this return using '/creature/'
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Creature:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.post("")
@router.post("/")
def create(creature: Creature) -> Creature:
    try:
        return service.create(creature)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.patch("/")
def modify(creature: Creature) -> Creature:
    try:
        return service.modify(creature)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.delete("/{name}")
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)