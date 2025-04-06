from abc import ABC, abstractmethod
import time

class ZombieState(ABC):
    @abstractmethod
    def handle(self, zombie): ...

    @abstractmethod
    def next_state(self, zombie, event): ...


class IdleState(ZombieState):
    def handle(self, zombie):
        print("🧟 The zombie is idle, waiting...")

    def next_state(self, zombie, event):
        if event == "player_near":
            return AttackingState()

        if event == "killed":
            return DeadState()

        return self

class AttackingState(ZombieState):
    def handle(self, zombie):
        print("🧟 The zombie is attacking!")

    def next_state(self, zombie, event):
        if event == "player_gone":
            return IdleState()

        if event == "stunned":
            return StunnedState()

        if event == "killed":
            return DeadState()

        return self

class StunnedState(ZombieState):
    def handle(self, zombie):
        print("💫 The zombie is stunned and can't attack!")
        time.sleep(1)

    def next_state(self, zombie, event):
        if event == "recover":
            return AttackingState()

        if event == "killed":
            return DeadState()

        return self

class DeadState(ZombieState):
    def handle(self, zombie):
        print("💀 The zombie is dead and no longer moves.")

    def next_state(self, zombie, event):
        return self


class Zombie:
    def __init__(self):
        self.state = IdleState()

    def trigger_event(self, event):
        self.state.handle(self)
        print(f"🚨 Event triggered: {event}", end=" | ")
        self.state = self.state.next_state(self, event)


zombie = Zombie()

zombie.trigger_event("player_near")
zombie.trigger_event("player_gone")
zombie.trigger_event("player_near")
zombie.trigger_event("stunned")
zombie.trigger_event("recover")
zombie.trigger_event("killed")
zombie.trigger_event("player_near")
