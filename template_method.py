from abc import ABC, abstractmethod


class Weapon(ABC):

    def attack(self):
        self.prepare_weapon()
        self.aim()
        self.execute_attack()
        self.recover()

    def prepare_weapon(self):
        print(f"Leon 👮 equips the {self.__class__.__name__.lower()}.")

    @abstractmethod
    def aim(self): ...

    @abstractmethod
    def execute_attack(self): ...

    def recover(self):
        print("Leon put the weapon down. 🙌")


class Handgun(Weapon):
    def aim(self):
        print("Leon carefully lines up a headshot. 🎯")

    def execute_attack(self):
        print("Leon fires a single 9mm bullet ✏!")

class Shotgun(Weapon):
    def aim(self):
        print("Leon braces for recoil and points at a group of enemies. 𖦏")

    def execute_attack(self):
        print("Leon fires a powerful spread shot, knocking enemies back! 🔫💥")

class Knife(Weapon):
    def aim(self):
        print("Leon raises his knife for close combat. 🗡")

    def execute_attack(self):
        print("Leon slashes quickly at the enemy! 🔪 🩸")


def simulate_attack(weapon: Weapon):
    print("=== Leon Attacks  with", weapon.__class__.__name__, "===")
    weapon.attack()


simulate_attack(Handgun())
simulate_attack(Shotgun())
simulate_attack(Knife())
