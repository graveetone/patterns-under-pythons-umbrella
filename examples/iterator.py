from abc import ABC, abstractmethod

class Iterator(ABC):
    def has_next(self): ...

    @abstractmethod
    def __next__(self): ...

class LeonInventoryIterator(Iterator):
    def __init__(self, items):
        self._items = items
        self._index = 0

    @property
    def has_next(self):
        return self._index < len(self._items)

    def __next__(self):
        if not self.has_next:
            raise StopIteration

        item = self._items[self._index]
        self._index += 1
        return item


class LeonInventory:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return LeonInventoryIterator(self._items)


inventory = LeonInventory()
inventory.add_item("Handgun  ̸/̸̅̅ ̆̅ ̅̅ ̅̅")
inventory.add_item("Shotgun ▄︻デ══━一💥")
inventory.add_item("First Aid Spray 🧪")
inventory.add_item("TMP ⌐╦╦═─")

print("Leon’s Inventory 🧳:")
for item in inventory:
    print(f"- {item}")
