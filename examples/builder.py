from abc import ABC, abstractmethod


class Loadout:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display(self):
        for item in self.items:
            print(f"- {item}")


class LoadoutBuilder(ABC):
    @abstractmethod
    def get_loadout(self) -> Loadout: ...

    def build_loadout(self): ...


class VillageLoadoutBuilder(LoadoutBuilder):
    def __init__(self):
        self.loadout = Loadout()

    def add_weapon(self):
        self.loadout.add_item("Handgun /̵͇̿̿/'̿'̿ ̿ ̿̿ ̿̿ ̿̿")
        self.loadout.add_item("Shotgun ▄︻デ══━一")

    def add_ammo(self):
        self.loadout.add_item("9mm Ammo ‣ ‣ ‣")
        self.loadout.add_item("Shotgun Shells ≔ ≔ ≔")

    def add_grenades(self):
        self.loadout.add_item("Grenade 💣")

    def build_loadout(self):
        self.add_weapon()
        self.add_ammo()
        self.add_grenades()

    def get_loadout(self):
        return self.loadout


class CastleLoadoutBuilder(LoadoutBuilder):
    def __init__(self):
        self.loadout = Loadout()

    def add_weapon(self):
        self.loadout.add_item("Magnum /̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿💥")
        self.loadout.add_item("Rifle ▄︻テ══━一💥")
        self.loadout.add_item("TMP ⌐╦╦═─")

    def add_ammo(self):
        self.loadout.add_item("Magnum Ammo ‣ ‣ ‣")
        self.loadout.add_item("Rifle Ammo ✏")
        self.loadout.add_item("TMP Ammo ‣‣‣ ‣‣‣ ‣‣‣")

    def add_grenades(self):
        self.loadout.add_item("Flash Grenade ✨")

    def get_loadout(self):
        return self.loadout

    def build_loadout(self):
        self.add_weapon()
        self.add_ammo()
        self.add_grenades()


class IslandLoadoutBuilder(LoadoutBuilder):
    def __init__(self):
        self.loadout = Loadout()

    def add_weapon(self):
        self.loadout.add_item("Rocket Launcher <=-===╦==<")
        self.loadout.add_item("Exclusive Rifle ▄︻デ══━一💨")

    def add_ammo(self):
        self.loadout.add_item("Rocket Launcher Ammo >==;;-->")
        self.loadout.add_item("Rifle Ammo ✏")

    def add_grenades(self):
        self.loadout.add_item("Flash Grenade ✨")

    def get_loadout(self):
        return self.loadout

    def build_loadout(self):
        self.add_weapon()
        self.add_ammo()
        self.add_grenades()


if __name__ == "__main__":
    for builder in (VillageLoadoutBuilder(), CastleLoadoutBuilder(), IslandLoadoutBuilder()):
        builder.build_loadout()
        loadout = builder.get_loadout()

        print(f"🎒Loadout for {builder.__class__.__name__}")
        loadout.display()
