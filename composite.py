from abc import ABC, abstractmethod


class CombatMove(ABC):
    @abstractmethod
    def execute(self): ...

    @abstractmethod
    def display(self, indent=0): ...


class SingleMove(CombatMove):
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Leon 👮 performs {self.name}!")

    def display(self, indent=0):
        print("  " * indent + f"- {self.name}")


class MoveCombo(CombatMove):

    def __init__(self, name, moves: list):
        self.name = name
        self.moves = moves

    def execute(self):
        print(f"\nLeon 👮 executes [{self.name} Combo]!")
        for move in self.moves:
            move.execute()

    def display(self, indent=0):
        print("  " * indent + f"[{self.name} Combo]")
        for move in self.moves:
            move.display(indent + 1)


kick = SingleMove("Roundhouse Kick 🦵💥🦶👊")
parry = SingleMove("Parry 👊")
slash = SingleMove("Knife Slash 🗡️")
suplex = SingleMove("Suplex 🤼‍♂️")

parry_counter = MoveCombo("Parry 👊 & Counterattack 🤼‍", moves=[parry, slash])

stun_kick = MoveCombo("Stun 🌀 & Kick 🦶", moves=[SingleMove("Stun Enemy"), kick])

full_takedown = MoveCombo("Full Takedown 🤼", moves=[parry_counter, stun_kick, suplex])


print("=== Leon’s Combat Moves 💪 ===")
full_takedown.display()
full_takedown.execute()
