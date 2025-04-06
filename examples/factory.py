from abc import ABC, abstractmethod

class GameLocationFactory(ABC):
    @abstractmethod
    def create_enemy(self): ...

    @abstractmethod
    def create_weapon(self): ...

    @abstractmethod
    def create_environment(self): ...


class VillageFactory(GameLocationFactory):
    def create_enemy(self):
        return Ganado()

    def create_weapon(self):
        return Pitchfork()

    def create_environment(self):
        return WoodenHouses()

class CastleFactory(GameLocationFactory):
    def create_enemy(self):
        return Zealot()

    def create_weapon(self):
        return Crossbow()

    def create_environment(self):
        return GothicCorridors()

class IslandFactory(GameLocationFactory):
    def create_enemy(self):
        return Soldier()

    def create_weapon(self):
        return StunRod()

    def create_environment(self):
        return MilitaryBase()


class Ganado:
    def attack(self):
        return "Ganado swings a pitchfork! Ψ"

class Zealot:
    def attack(self):
        return "Zealot chants and shoots a crossbow! 🏹"

class Soldier:
    def attack(self):
        return "Soldier fires an SMG! ⌐╦╦═─"

class Pitchfork:
    def use(self):
        return "Using a pitchfork for melee attacks. Ψ"

class Crossbow:
    def use(self):
        return "Firing a crossbow! 🏹"

class StunRod:
    def use(self):
        return "Zapping with a stun rod! ⚡️"

class WoodenHouses:
    def describe(self):
        return "Rustic wooden houses with torches. 🔦"

class GothicCorridors:
    def describe(self):
        return "Dark stone corridors with chandeliers. 🕎"

class MilitaryBase:
    def describe(self):
        return "High-tech military base with bunkers. 🪖"


def setup_game_location(factory: GameLocationFactory):
    enemy = factory.create_enemy()
    weapon = factory.create_weapon()
    environment = factory.create_environment()

    print(environment.describe())
    print(enemy.attack())
    print(weapon.use())


if __name__ == "__main__":
    print("=== 🏘️  Village Level ===")
    setup_game_location(factory=VillageFactory())

    print("\n=== 🏰 Castle Level ===")
    setup_game_location(factory=CastleFactory())

    print("\n=== 🏝️  Island Level ===")
    setup_game_location(factory=IslandFactory())
