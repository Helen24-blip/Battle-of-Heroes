import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other, attack_power=None):
        """Атакует другого героя с возможностью указания силы удара."""
        if self.is_alive():
            actual_attack_power = attack_power if attack_power else self.attack_power
            other.health -= actual_attack_power
            print(f"{self.name} атаковал {other.name} и нанес {actual_attack_power} урона.")
        else:
            print(f"{self.name} мертв и не может атаковать.")

    def is_alive(self):
        """Возвращает True, если здоровье героя больше 0, иначе False."""
        return self.health > 0

    def __str__(self):
        """Возвращает строковое представление героя."""
        return f"{self.name}: здоровье = {self.health}, сила удара = {self.attack_power}"


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        """Запускает игру и чередует ходы между игроком и компьютером."""
        print("Начало игры!")
        print(self.player)
        print(self.computer)

        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if not self.computer.is_alive():
                print(f"\n{self.player.name} победил!")
                break # Прерываем цикл, если компьютер проиграл

            self.computer_turn()
            if not self.player.is_alive():
                print(f"\n{self.computer.name} победил!")
                break # Прерываем цикл, если игрок проиграл

    def player_turn(self):
        """Ход игрока: выбор силы атаки и атака компьютера."""
        print("\nВыберите силу атаки:")
        print("1. Слабая атака (10 урона)")
        print("2. Средняя атака (20 урона)")
        print("3. Сильная атака (30 урона)")
        choice = input("Введите номер атаки (1/2/3): ")

        if choice == '1':
            self.player.attack(self.computer, 10)
        elif choice == '2':
            self.player.attack(self.computer, 20)
        elif choice == '3':
            self.player.attack(self.computer, 30)
        else:
            print("Некорректный выбор! Выберите 1, 2 или 3.")
            self.player_turn()  # Повторное предложение выбора атаки, если был некорректный ввод.

        print(self.computer)

    def computer_turn(self):
        """Ход компьютера: случайная атака игрока с шансом на критический удар."""
        attack_power = random.randint(10, 30)
        is_critical = random.choice([True, False])  # 50% шанс критического удара

        if is_critical:
            attack_power *= 2
            print(f"Критический удар! {self.computer.name} удваивает свою атаку!")

        self.computer.attack_power = attack_power
        self.computer.attack(self.player)
        print(self.player)


if __name__ == "__main__":
    game = Game("Игрок")
    game.start()
