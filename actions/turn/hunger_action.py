from actions.base import Action
from world.game_map import GameMap
from entities.creature import Creature


class HungerAction(Action):
    """Применение эффекта голода ко всем живым существам"""
    
    def perform(self, game_map: GameMap) -> None:
        creatures =[e for e in game_map.get_all_entities() if isinstance(e, Creature)]
        
        for creature in creatures:
            if creature.is_alive:
                creature.apply_hunger()
