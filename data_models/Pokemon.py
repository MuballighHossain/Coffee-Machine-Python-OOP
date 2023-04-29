
from typing import List, Tuple

class Pokemon():

    def __init__(self, name: str, pokedexId: str, level: int, living_points: int,
                 attacking_points: int, defence_points: int, attack: List[Tuple[str, int]]) -> None:
        self.name = name
        self.pokedexId = pokedexId
        self.level = level
        self.living_points = living_points
        self.attacking_points = attacking_points
        self.defence_points = defence_points
        self.attack = attack
        self.experience_points: int = 0
        self.fight_status: bool = False
        self.alive: bool = True

