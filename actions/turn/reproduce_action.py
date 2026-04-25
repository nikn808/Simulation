import random
from typing import Type, Any
from actions.base import Action
from world.game_map import GameMap
from entities.creature import Creature

class ReproduceAction(Action):
    """Размножение существ с заданным шансом при наличии пар"""
    
    def __init__(self, creature_class: Type[Creature], chance: float, **kwargs: Any) -> None:
        self._creature_class = creature_class
        self._chance = chance
        self._kwargs = kwargs

    def perform(self, game_map: GameMap) -> None:
        alive_count = sum(1 for e in game_map.get_all_entities() if isinstance(e, self._creature_class) and e.is_alive)

        pairs = alive_count // 2
        if pairs <= 0:
            return
            
        success_count = sum(1 for _ in range(pairs) if random.random() < self._chance)
        
        if success_count == 0:
            return

        cells_to_populate = game_map.get_random_empty_cells(success_count)
        for pos in cells_to_populate:
            game_map.add_entity(pos, self._creature_class(**self._kwargs))