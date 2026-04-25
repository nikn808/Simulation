from typing import Type, Any
from actions.base import Action
from world.game_map import GameMap
from entities.entity import Entity

class SpawnAction(Action):
    """Универсальное действие для спавна сущностей"""
    
    def __init__(self, entity_class: Type[Entity], target_amount: int, **kwargs: Any) -> None:
        self._entity_class = entity_class
        self._target_amount = target_amount
        self._kwargs = kwargs

    def perform(self, game_map: GameMap) -> None:
        current_amount = sum(1 for e in game_map.get_all_entities() if isinstance(e, self._entity_class))
        to_spawn = self._target_amount - current_amount

        if to_spawn <= 0:
            return

        cells_to_populate = game_map.get_random_empty_cells(to_spawn)
        for pos in cells_to_populate:
            game_map.add_entity(pos, self._entity_class(**self._kwargs))
