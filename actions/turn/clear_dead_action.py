from actions.base import Action
from world.game_map import GameMap
from entities.creature import Creature


class ClearDeadAction(Action):
    """Очистка карты от погибших существ"""
    
    def perform(self, game_map: GameMap) -> None:
        entities = game_map.get_all_entities()
        
        for entity in entities:
            if isinstance(entity, Creature) and not entity.is_alive:
                pos = game_map.get_position(entity)
                if pos is not None:
                    game_map.remove_entity(pos)