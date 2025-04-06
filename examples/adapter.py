from abc import ABC


class AbstractEnemy(ABC):
    def hit(self): ...


class GanadoZombie(AbstractEnemy):
    def hit(self):
        print("Ganado 🧟‍ hits with an ax 🪓")

class InfectedDog:
    def bite(self):
        print("Zombie Dog 🐕 bites with the sharp teeth 🦷")


class DogZombie(AbstractEnemy):
    def __init__(self, dog: InfectedDog):
        self._dog = dog

    def hit(self):
        self._dog.bite()

for enemy in (GanadoZombie(), DogZombie(InfectedDog()), GanadoZombie()):
    enemy.hit()

