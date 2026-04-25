from dataclasses import dataclass, field
 
 
@dataclass(frozen=True)
class SimulationConfig:
    # Карта
    map_width: int = 20
    map_height: int = 20
 
    # Травоядные
    herbivore_hp: int = 20
    herbivore_max_hp: int = 20
    herbivore_speed: int = 1
    herbivore_hp_regen_per_turn: int = 1
    herbivore_satiety_max: int = 60
    herbivore_satiety_from_grass: int = 30
    herbivore_satiety_drain_per_turn: int = 3
    herbivore_satiety_damage_per_turn: int = 2
    herbivore_reproduce_chance: float = 0.06
 
    # Хищники
    predator_hp: int = 30
    predator_max_hp: int = 30
    predator_speed: int = 2
    predator_attack: int = 7
    predator_hp_regen_per_turn: int = 1
    predator_satiety_max: int = 60
    predator_satiety_from_kill: int = 25
    predator_satiety_drain_per_turn: int = 6
    predator_satiety_damage_per_turn: int = 4
    predator_reproduce_chance: float = 0.02
 
    # Стартовое количество сущностей
    grass_amount: int = 35
    grass_spawn_per_turn: int = 4
    rock_amount: int = 8
    tree_amount: int = 8
    herbivore_amount: int = 20
    predator_amount: int = 3
 
    # UI и тайминги
    turn_delay_seconds: float = 1.0
    start_delay_seconds: float = 2.0
 
    # Спрайты
    empty_cell_sprite: str = "🟫"
    sprites: dict = field(default_factory=lambda: {
        "Herbivore": "🐇",
        "Predator":  "🐺",
        "Grass":     "🌿",
        "Rock":      "🗿",
        "Tree":      "🌳",
    })
 
 
# Экземпляр по умолчанию — используется во всём приложении
DEFAULT_CONFIG = SimulationConfig()