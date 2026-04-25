import time
from world.game_map import GameMap
from rendering.base import Renderer
from actions.base import Action
from entities.creature import Creature

class Simulation:
    """Управляет основным циклом и выполнением действий"""
    def __init__(self, game_map: GameMap, renderer: Renderer, 
                 init_actions: list[Action], turn_actions: list[Action],
                 turn_delay: float):
        self.game_map = game_map
        self.renderer = renderer
        self.init_actions = init_actions
        self.turn_actions = turn_actions
        self.turn_counter = 0
        self._turn_delay = turn_delay
        self._is_running = False

    def init_simulation(self) -> None:
        """Подготовка карты к старту"""
        for action in self.init_actions:
            action.perform(self.game_map)
        self.renderer.render(self.game_map, self.turn_counter)

    def next_turn(self) -> None:
        """Проигрывает один ход симуляции"""
        for action in self.turn_actions:
            action.perform(self.game_map)
        
        self.turn_counter += 1
        self.renderer.render(self.game_map, self.turn_counter)

    def start_simulation(self) -> None:
        """Запуск бесконечного цикла симуляции"""
        self._is_running = True
        try:
            while self._is_running and not self.is_over():
                self.next_turn()
                time.sleep(self._turn_delay)
        except KeyboardInterrupt:
            self.pause_simulation()

    def pause_simulation(self) -> None:
        """Приостановка цикла симуляции"""
        self._is_running = False
        print("\nСимуляция приостановлена.")

    def is_over(self) -> bool:
        """Симуляция окончена, если не осталось живых существ"""
        return not any(isinstance(e, Creature) and e.is_alive for e in self.game_map.get_all_entities())
