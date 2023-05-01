from data_models.PokeType import PokeType
from data_models.Pokemon import Pokemon


class AquaPokemon(Pokemon):
    def __init__(self, name, pokedexId, level, living_points,
                 attacking_points, defence_points, attack):
        super().__init__(name, pokedexId, level, living_points,
                 attacking_points, defence_points, attack)

        self.type: PokeType = PokeType(0)

    def lvlUp(self) -> Pokemon:
        pass