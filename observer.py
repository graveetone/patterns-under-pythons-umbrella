from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self): ...

class Observable(ABC):
    def __init__(self):
        self.observers = set()

    def add_observer(self, observer):
        self.observers.add(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

class Gun(Observable):
    def shoot(self):
        print("🔫 Gun fired!")

        self.notify_observers()


class Enemy(Observer):
    def update(self):
        print("Enemy hears 👂 the gun shot")

class AmmoCounterDisplay(Observer):
    def __init__(self):
        self.ammo = 10

    def update(self):
        self.ammo -= 1
        print(f"🕹️ Ammo left: {self.ammo}")


if __name__ == "__main__":
    gun = Gun()
    enemy1 = Enemy()
    enemy2 = Enemy()
    ammo_counter = AmmoCounterDisplay()

    gun.add_observer(enemy1)
    gun.add_observer(enemy2)
    gun.add_observer(ammo_counter)

    for _ in range(3):
        gun.shoot()
