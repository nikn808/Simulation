from abc import ABC, abstractmethod
from world.game_map import GameMap


class Action(ABC):
    """Абстрактный класс действия"""
    
    @abstractmethod
    def perform(self, game_map: GameMap) -> None:
        pass
