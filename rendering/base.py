from abc import ABC, abstractmethod
from world.game_map import GameMap

class Renderer(ABC):
    """Абстрактный класс рендера карты"""
    
    @abstractmethod
    def render(self, game_map: GameMap, turn_counter: int) -> None:
        pass