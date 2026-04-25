import os
from rendering.base import Renderer
from world.game_map import GameMap
from world.coordinates import Coordinates

class ConsoleRenderer(Renderer):
    """Отвечает за вывод состояния карты в консоль"""
    
    def __init__(self, empty_cell_sprite: str, sprites: dict[str, str]) -> None:
        self._empty_cell_sprite = empty_cell_sprite
        self._sprites = sprites

    def _get_sprite(self, entity) -> str:
        """Возвращает спрайт по имени сущности"""
        return self._sprites.get(type(entity).__name__, "?")
    
    def render(self, game_map: GameMap, turn_counter: int) -> None:
        """Отрисовывает текущее состояние карты"""
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"=== Симуляция: Ход {turn_counter} ===")
        for y in range(game_map.height):
            row_symbols = []
            for x in range(game_map.width):
                entity = game_map.get_entity(Coordinates(x, y))
                if entity is None:
                    row_symbols.append(self._empty_cell_sprite)
                else:
                    row_symbols.append(self._get_sprite(entity))
            print("".join(row_symbols))

        entities = game_map.get_all_entities()
        counts: dict[str, int] = {}
        for entity in entities:
            name = type(entity).__name__
            counts[name] = counts.get(name, 0) + 1
 
        parts = [f"{self._sprites.get(name, name)} {count}"for name, count in counts.items()]
        print("  ".join(parts))
        print("=" * (game_map.width * 2))


    