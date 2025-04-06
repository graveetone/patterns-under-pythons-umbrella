from abc import ABC


class AttackStrategy(ABC):
    def attack(self):
        print("Attacking with bare hands 🫶")


class HandgunAttack(AttackStrategy):
    def attack(self):
        print("Shooting with the Handgun  ̸/̸̅̅ ̆̅ ̅̅ ̅̅. Pow! Pow!")


class ShotgunAttack(AttackStrategy):
    def attack(self):
        print("Firing the Shotgun ▄︻テ══━一💥. Boom!")


class GrenadeAttack(AttackStrategy):
    def attack(self):
        print("Throwing a Grenade 🧨. Boom!")


class Leon:
    def __init__(self):
        self.attack_strategy = AttackStrategy()

    def set_attack_strategy(self, strategy: AttackStrategy):
        self.attack_strategy = strategy

    def perform_attack(self):
        self.attack_strategy.attack()


leon = Leon()
leon.perform_attack()

leon.set_attack_strategy(HandgunAttack())
leon.perform_attack()

leon.set_attack_strategy(ShotgunAttack())
leon.perform_attack()

leon.set_attack_strategy(GrenadeAttack())
leon.perform_attack()
