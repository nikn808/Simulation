import time
from factories.simulation_factory import SimulationFactory
from config import DEFAULT_CONFIG

class AppController:
    """Контроллер приложения. Управляет UI-циклом и консольным вводом"""

    MENU = (
        "\n=== Меню ==="
        "\n1. Сделать 1 ход"
        "\n2. Бесконечная симуляция"
        "\n3. Перезапустить мир"
        "\n4. Выход"
    )
    
    def __init__(self) -> None:
        self._simulation = SimulationFactory.create()
        self._simulation.init_simulation()

    def _setup_new_simulation(self) -> None:
        """Пересоздание мира"""
        self._simulation = SimulationFactory.create()
        self._simulation.init_simulation()

    def run(self) -> None:
        """Главный цикл и меню приложения"""
        while True:
            if self._simulation.is_over():
                print("❗️ Симуляция окончена: все вымерли.")

            print(self.MENU)
            
            choice = input("Выберите действие: ").strip()
            
            match choice:
                case "1":
                    self._handle_single_step()
                case "2":
                    self._handle_infinite_loop()
                case "3":
                    self._setup_new_simulation()
                case "4":
                    print("Выход из симуляции...")
                    break
                case _:
                    print("Неверный ввод, попробуйте снова.")

    def _handle_single_step(self) -> None:
        """Обработка одного шага"""
        if not self._simulation.is_over():
            self._simulation.next_turn()   

    def _handle_infinite_loop(self) -> None:
        """Обработка бесконечного цикла"""
        if self._simulation.is_over():
            return

        print("Симуляция запущена. Нажмите Ctrl+C для возврата в меню.")
        time.sleep(DEFAULT_CONFIG.start_delay_seconds)
        self._simulation.start_simulation()