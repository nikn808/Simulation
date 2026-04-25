from world.game_map import GameMap
from rendering.console_renderer import ConsoleRenderer
 
from actions.spawn_action import SpawnAction
from actions.turn.move_action import MoveAction
from actions.turn.clear_dead_action import ClearDeadAction
from actions.turn.hunger_action import HungerAction
from actions.turn.reproduce_action import ReproduceAction
from actions.turn.grass_grow_action import GrassGrowAction
 
from entities.herbivores import Herbivore
from entities.predators import Predator
from entities.creatureconfig import HerbivoreConfig, PredatorConfig
from entities.static_objects import Grass, Rock, Tree
 
from simulation import Simulation
from config import SimulationConfig, DEFAULT_CONFIG
 
 
class SimulationFactory:
    """Собирает компоненты симуляции"""
 
    @staticmethod
    def create(cfg: SimulationConfig = DEFAULT_CONFIG) -> Simulation:
        game_map = GameMap(cfg.map_width, cfg.map_height)
        renderer = ConsoleRenderer(
            empty_cell_sprite=cfg.empty_cell_sprite,
            sprites=cfg.sprites,
        )
 
        herbivore_config = HerbivoreConfig(
            max_hp=cfg.herbivore_max_hp,
            hp=cfg.herbivore_hp,
            speed=cfg.herbivore_speed,
            max_satiety=cfg.herbivore_satiety_max,
            satiety_drain=cfg.herbivore_satiety_drain_per_turn,
            hp_regen=cfg.herbivore_hp_regen_per_turn,
            hunger_damage=cfg.herbivore_satiety_damage_per_turn,
            satiety_from_grass=cfg.herbivore_satiety_from_grass,
        )
 
        predator_config = PredatorConfig(
            max_hp=cfg.predator_max_hp,
            hp=cfg.predator_hp,
            speed=cfg.predator_speed,
            max_satiety=cfg.predator_satiety_max,
            satiety_drain=cfg.predator_satiety_drain_per_turn,
            hp_regen=cfg.predator_hp_regen_per_turn,
            hunger_damage=cfg.predator_satiety_damage_per_turn,
            attack_power=cfg.predator_attack,
            satiety_from_kill=cfg.predator_satiety_from_kill,
        )
 
        init_actions = [
            SpawnAction(Grass, cfg.grass_amount),
            SpawnAction(Rock, cfg.rock_amount),
            SpawnAction(Tree, cfg.tree_amount),
            SpawnAction(Herbivore, cfg.herbivore_amount, config=herbivore_config),
            SpawnAction(Predator, cfg.predator_amount, config=predator_config),
        ]
 
        turn_actions = [
            HungerAction(),
            ClearDeadAction(),
            MoveAction(),
            ReproduceAction(Herbivore, cfg.herbivore_reproduce_chance, config=herbivore_config),
            ReproduceAction(Predator, cfg.predator_reproduce_chance, config=predator_config),
            GrassGrowAction(Grass, cfg.grass_spawn_per_turn),
        ]
 
        return Simulation(
            game_map=game_map,
            renderer=renderer,
            init_actions=init_actions,
            turn_actions=turn_actions,
            turn_delay=cfg.turn_delay_seconds,
        )