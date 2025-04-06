from abc import ABC, abstractmethod

DEFAULT_ZOMBIE_HEALTH = 70
PLAGUED_ZOMBIE_HEALTH = 100

class AbstractZombie(ABC):
    name: str
    health: float

    @abstractmethod
    def take_damage(self, damage: float): ...

    @property
    def is_dead(self):
        return self.health <= 0

    def __str__(self):
        zombie_type = self.__class__.__name__
        if self.is_dead:
            return f"Dead 💀 {zombie_type} {self.name}"

        return f"Alive 🧟‍ {zombie_type} {self.name} with health 💊: {self.health}"


class Zombie(AbstractZombie):
    def __init__(self, name):
        self.name = name
        self.health = DEFAULT_ZOMBIE_HEALTH


    def take_damage(self, damage: float):
        if self.is_dead:
            return

        print(f"{self} takes damage {damage} 😵")
        self.health -= damage


class ZombieWithPlague(AbstractZombie):

    def __init__(self, zombie: AbstractZombie):
        self._zombie = zombie
        self._zombie.health = PLAGUED_ZOMBIE_HEALTH
        self._plagued: bool = False

    def take_damage(self, damage: float):
        self._zombie.take_damage(damage)

        if self._zombie.health <= DEFAULT_ZOMBIE_HEALTH:
            self._plagued = True

    def __str__(self):
        if self._plagued:
            return f"Plagued ☣️  {self._zombie}"

        return str(self._zombie)


if __name__ == "__main__":
    zombies = [
        Zombie('Ganado 🧟‍️'),
        Zombie('Zealot 🧛🏼‍'),
        ZombieWithPlague(Zombie('Ganado 🧟‍'))
    ]

    for zombie in zombies:
        print(zombie)
        zombie.take_damage(80)
        print(zombie)
        print("_" * 60)
