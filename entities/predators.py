from typing import Optional
from entities.creatureconfig import PredatorConfig
from entities.creature import Creature
from entities.entity import Entity
from entities.herbivores import Herbivore


class Predator(Creature):
    """Хищник"""
    
    def __init__(self, config: PredatorConfig) -> None:
        super().__init__(config)
        self._attack_power = config.attack_power
        self._satiety_from_kill = config.satiety_from_kill


    def is_target(self, entity: Entity) -> bool:
        return isinstance(entity, Herbivore)

    def is_passable(self, entity: Optional[Entity]) -> bool:
        return entity is None

    def interact(self, target: Entity) -> bool:
        if isinstance(target, Herbivore):
            target.take_damage(self._attack_power)
            if not target.is_alive:
                self.restore_satiety(self._satiety_from_kill)
                return True
        return False