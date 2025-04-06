class ZombieType:
    def __init__(self, name, speed, base_health):
        self.name = name
        self.speed = speed
        self.base_health = base_health

    def display_info(self):
        print(f"Zombie 🧟‍ Type: {self.name}, Speed ⚡︎ : {self.speed}, Base Health ✙ : {self.base_health}")


class ZombieFactory:
    _zombie_types = {}

    def get_zombie_type(self, name, speed, base_health):
        if name not in self._zombie_types:
            self._zombie_types[name] = ZombieType(name, speed, base_health)
        return self._zombie_types[name]


class Zombie:
    def __init__(self, zombie_type, position, current_health):
        self.zombie_type = zombie_type
        self.position = position
        self.current_health = current_health

    def display_info(self):
        self.zombie_type.display_info()
        print(f"  📍 Position: {self.position}, Current Health ✙: {self.current_health}\n")


zombie_factory = ZombieFactory()

ganado = zombie_factory.get_zombie_type("Ganado", speed=1.2, base_health=100)
regenerator = zombie_factory.get_zombie_type("Regenerator", speed=0.5, base_health=300)

zombie_1 = Zombie(ganado, position=(10, 20), current_health=100)
zombie_2 = Zombie(ganado, position=(15, 25), current_health=80)
zombie_3 = Zombie(ganado, position=(5, 10), current_health=300)

zombie_1.display_info()
zombie_2.display_info()
zombie_3.display_info()
