from model import Creature

_creatures: list[Creature] = [Creature(name="yeti",
                                       description="Abominable Snowman",
                                       location="Himalayas"),
                              Creature(name="sasquatch",
                                       description="Bigfoot",
                                       location="North America")]

def get_creatures() -> list[Creature]:
    return _creatures