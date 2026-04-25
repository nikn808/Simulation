from typing import Type, Any
from actions.base import Action
from world.game_map import GameMap
from entities.entity import Entity


class GrassGrowAction(Action):
    """Рост травы в пустых клетках"""
    
    def __init__(self, entity_class: Type[Entity], grow_amount: int, **kwargs: Any) -> None:
        self._entity_class = entity_class
        self._grow_amount = grow_amount
        self._kwargs = kwargs

    def perform(self, game_map: GameMap) -> None:
        cells_to_populate = game_map.get_random_empty_cells(self._grow_amount)
        for pos in cells_to_populate:
            game_map.add_entity(pos, self._entity_class(**self._kwargs))