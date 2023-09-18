from model.creature import Creature

_creatures = [Creature(name="yeti",
                       description="Abominable Snowman",
                       location="Himalayas"),
              Creature(name="bigfoot",
                       description="AKA Sasquatch, the New World Counsin Eddie of the yeti",
                       location="North America")]

def get_all() -> list[Creature]:
    """Return all creatures"""
    return _creatures

def get_one(name: str) -> Creature | None:
    """Return one creature"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

def create(creature: Creature) -> Creature:
    """Add a creature"""
    return creature

def modify(creature: Creature) -> Creature:
    """Partially modify a creature"""
    return creature

def replace(creature: Creature) -> Creature:
    """Completely replace a creature"""
    return creature

def delete(name: str):
    """Delete a creature; return none if if existed"""
    return None