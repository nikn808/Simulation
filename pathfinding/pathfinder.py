from collections import deque
from typing import Callable, Optional

from world.coordinates import Coordinates
from world.game_map import GameMap
from entities.entity import Entity


class PathFinder:
    """Обеспечивает поиск пути"""

    @staticmethod
    def get_path(
        game_map: GameMap,
        start_pos: Coordinates,
        is_target_func: Callable[[Entity], bool],
        is_passable_func: Callable[[Optional[Entity]], bool]
    ) -> Optional[list[Coordinates]]:
        """Ищет кратчайший путь от start_pos до ближайшей цели"""
        
        queue = deque([start_pos])
        came_from: dict[Coordinates, Optional[Coordinates]] = {start_pos: None}

        while queue:
            current = queue.popleft()

            for neighbor in game_map.get_neighbors(current):
                if neighbor in came_from:
                    continue

                entity = game_map.get_entity(neighbor)

                if entity is not None and is_target_func(entity):
                    came_from[neighbor] = current
                    return PathFinder._reconstruct_path(came_from, start_pos, neighbor)

                if is_passable_func(entity):
                    came_from[neighbor] = current
                    queue.append(neighbor)

        return None

    @staticmethod
    def _reconstruct_path(
        came_from: dict[Coordinates, Optional[Coordinates]], 
        start: Coordinates, 
        goal: Coordinates
    ) -> list[Coordinates]:
        """Восстанавливает путь от цели к старту"""
        path = []
        current = goal
        
        while current != start:
            path.append(current)
            current = came_from[current]
        
        path.reverse()
        return path