from dataclasses import dataclass


@dataclass(frozen=True)
class CreatureConfig:
    """Базовые параметры любого существа"""
    max_hp: int
    hp: int
    speed: int
    max_satiety: int
    satiety_drain: int
    hp_regen: int
    hunger_damage: int


@dataclass(frozen=True)
class HerbivoreConfig(CreatureConfig):
    """Параметры травоядного"""
    satiety_from_grass: int


@dataclass(frozen=True)
class PredatorConfig(CreatureConfig):
    """Параметры хищника"""
    attack_power: int
    satiety_from_kill: int