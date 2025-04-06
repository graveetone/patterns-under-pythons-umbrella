import sys
from abc import ABC, abstractmethod

class Receiver(ABC): ...

class Character(Receiver):
    def __init__(self, name: str):
        self.name = name
        self.current_weapon = "hands ✋😮🤚"

    def go(self, direction: str):
        print(f"{self.name} goes {direction}")

    def hit(self):
        print(f"{self.name} hits with the {self.current_weapon}")

    def switch_weapon(self):
        if self.current_weapon == "knife":
            self.current_weapon = "hands"
        else:
            self.current_weapon = "knife"

        print(f"Weapon changed to {self.current_weapon}")


class Command(ABC):
    def __init__(self, character: Character):
        self.character = character

    @abstractmethod
    def execute(self): ...


class GoAheadCommand(Command):
    def execute(self):
        self.character.go("ahead 🏃")

class GoBackCommand(Command):
    def execute(self):
        self.character.go("back 🏃‍")


class HitCommand(Command):
    def execute(self):
        self.character.hit()

class SwitchWeaponCommand(Command):
    def execute(self):
        self.character.switch_weapon()


if __name__ == "__main__":
    leon = Character("Leon 👮")

    keys_commands_mapping = {
        "w": GoAheadCommand(character=leon),
        "s": GoBackCommand(character=leon),
        "rmc": HitCommand(character=leon),
        "ctrl": SwitchWeaponCommand(character=leon),
    }

    print("Leon Commands 🎮")
    while True:
        key = input("▶ ")

        if key not in keys_commands_mapping:
            continue

        command = keys_commands_mapping[key]
        command.execute()
