from abc import ABC, abstractmethod
from typing import Optional

from entities.entity import Entity
from entities.creatureconfig import CreatureConfig
from world.game_map import GameMap
from world.coordinates import Coordinates
from pathfinding.pathfinder import PathFinder


class Creature(Entity, ABC):
    """Базовый класс для всех живых существ"""
    
    def __init__(self, config: CreatureConfig) -> None:
        self._config = config
        self._max_hp = config.max_hp
        self._hp = config.hp
        self._max_satiety = config.max_satiety
        self._satiety = config.max_satiety
        self._satiety_drain = config.satiety_drain
        self._hp_regen = config.hp_regen
        self._hunger_damage = config.hunger_damage
        self._speed = config.speed

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def speed(self) -> int:
        return self._speed

    @property
    def is_alive(self) -> bool:
        return self._hp > 0

    def take_damage(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Урон не может быть отрицательным.")
        self._hp = max(0, self._hp - amount)

    def heal(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Лечение не может быть отрицательным.")
        self._hp = min(self._max_hp, self._hp + amount)

    def restore_satiety(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Восстановление сытости не может быть отрицательным.")
        self._satiety = min(self._max_satiety, self._satiety + amount)

    def drain_satiety(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Уменьшение сытости не может быть отрицательным.")
        self._satiety = max(0, self._satiety - amount)

    def apply_hunger(self) -> None:
        self.drain_satiety(self._satiety_drain)
        if self._satiety > 0:
            self.heal(self._hp_regen)
        else:
            self.take_damage(self._hunger_damage)

    @abstractmethod
    def is_target(self, entity: Entity) -> bool:
        """Является ли сущность целью"""
        pass

    @abstractmethod
    def is_passable(self, entity: Optional[Entity]) -> bool:
        """Может ли существо наступить на клетку (включая пустые)"""
        pass

    @abstractmethod
    def interact(self, target: Entity) -> bool:
        """Взаимодействие с целью"""
        pass

    def take_turn(self, game_map: GameMap, current_pos: Coordinates) -> None:
        """Ход существа"""
        if not self.is_alive:
            return
        if self._try_interact(game_map, current_pos): 
            return

        self._make_move(game_map, current_pos) 
        new_pos = game_map.get_position(self)
        
        if new_pos is not None:
            self._try_interact(game_map, new_pos)

    def _find_nearby_target(self, game_map: GameMap, pos: Coordinates) -> Optional[Coordinates]:
        """Поиск ближайшей цели"""
        for neighbor in game_map.get_neighbors(pos):
            entity = game_map.get_entity(neighbor)
            if entity is not None and self.is_target(entity):
                return neighbor
                
        return None

    def _make_move(self, game_map: GameMap, current_pos: Coordinates) -> None:
        """Осуществление перемещения существа"""
        path = PathFinder.get_path(game_map, current_pos, self.is_target, self.is_passable)
        
        if not path:
            return

        steps = path[:self._speed]
        
        last_valid_step = current_pos
        for step in steps:
            target_entity = game_map.get_entity(step)
            
            if self.is_passable(target_entity):
                last_valid_step = step
            else:
                break
                
        if last_valid_step != current_pos:
            game_map.move_entity(current_pos, last_valid_step)

    def _try_interact(self, game_map: GameMap, current_pos: Coordinates) -> bool:
        """Попытка взаимодействия с целью"""
        target_pos = self._find_nearby_target(game_map, current_pos)

        if target_pos is not None:
            target_entity = game_map.get_entity(target_pos)
            
            if target_entity is not None:
                is_destroyed = self.interact(target_entity)
                if is_destroyed:
                    game_map.remove_entity(target_pos)
                    #game_map.move_entity(current_pos, target_pos)
                return True
                
        return False