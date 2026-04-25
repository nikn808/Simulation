from actions.base import Action
from world.game_map import GameMap
from entities.creature import Creature


class MoveAction(Action):
    """Ход существ с учетом приоритета скорости"""
    
    def perform(self, game_map: GameMap) -> None:
        creatures =[e for e in game_map.get_all_entities() if isinstance(e, Creature)]
        creatures.sort(key=lambda c: c.speed, reverse=True)
        
        for creature in creatures:
            if creature.is_alive:
                pos = game_map.get_position(creature)
                if pos is not None:
                    creature.take_turn(game_map, pos)