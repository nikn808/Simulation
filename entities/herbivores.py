from typing import Optional

from entities.creatureconfig import HerbivoreConfig
from entities.creature import Creature
from entities.entity import Entity
from entities.static_objects import Grass


class Herbivore(Creature):
    """Травоядное"""
    
    def __init__(self, config: HerbivoreConfig) -> None:
        super().__init__(config)
        self._satiety_from_grass = config.satiety_from_grass
    
    def is_target(self, entity: Entity) -> bool:
        return isinstance(entity, Grass)

    def is_passable(self, entity: Optional[Entity]) -> bool:
        return entity is None

    def interact(self, target: Entity) -> bool:
        if isinstance(target, Grass):
            self.restore_satiety(self._satiety_from_grass)
            return True
        return False
