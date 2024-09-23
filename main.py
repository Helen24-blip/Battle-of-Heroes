import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """Атакует другого героя, уменьшая его здоровье на величину силы удара."""
        if self.is_alive():
            other.health -= self.attack_power
            print(f"{self.name} атаковал {other.name} и нанес {self.attack_power} урона.")
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
                print(f"{self.player.name} победил!")
                break

            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break

    def player_turn(self):
        """Ход игрока: атака компьютера."""
        self.player.attack(self.computer)
        print(self.computer)

    def computer_turn(self):
        """Ход компьютера: случайная атака игрока."""
        attack_power = random.randint(10, 30)
        self.computer.attack_power = attack_power
        self.computer.attack(self.player)
        print(self.player)


if __name__ == "__main__":
    game = Game("Игрок")
    game.start()
