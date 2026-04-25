from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinates:
    """Неизменяемый класс координат для работы с сеткой карты"""
    x: int
    y: int