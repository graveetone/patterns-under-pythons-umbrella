from abc import ABC, abstractmethod


class BaseMerchant(ABC):
    @abstractmethod
    def buy(self, item): ...

class Merchant(BaseMerchant):
    def __init__(self):
        self.items = {
            "Handgun": 10000,
            "Shotgun": 20000,
            "First Aid Spray": 5000
        }
        self.black_market_items = {
            "Chicago Typewriter": 1000000,
            "Infinite Rocket Launcher": 999999,
            "Handcannon": 750000
        }

    def buy(self, item):
        if item in self.items:
            print(f"🧙‍Merchant: '{item}' purchased for {self.items[item]} PTAS.")
        else:
            print(f"🧙‍Merchant: '{item}' is not available.")


class BlackMarketProxy(Merchant):
    """Proxy that restricts access to special items."""

    def __init__(self, merchant, has_access):
        self.merchant = merchant
        self.has_access = has_access

    def buy(self, item):
        black_market_items = self.merchant.black_market_items

        if item in black_market_items:
            if self.has_access:
                print(f"💸 Black Market: '{item}' purchased for {black_market_items[item]} PTAS.")
            else:
                print(f"💸 Black Market: Sorry, '{item}' is only available after completing the game.")
        else:
            self.merchant.buy(item)


game_completed = False

merchant = Merchant()
black_market = BlackMarketProxy(merchant, game_completed)

print("=== 🤑 Attempting Purchases 🤑 ===")
black_market.buy("Handgun")
black_market.buy("Chicago Typewriter")

game_completed = True
print("\n=== After completing the game ===\n")
black_market = BlackMarketProxy(merchant, game_completed)

print("\n=== 🤑 Attempting Purchases 🤑 ===")
black_market.buy("Handgun")
black_market.buy("Chicago Typewriter")