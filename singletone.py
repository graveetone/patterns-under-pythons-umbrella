class GameSettings:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return

        self.screen_width = 800
        self.screen_height = 600
        self.music_level = 100
        self.__initialized = True

    def set_screen_resolution(self, width: int, height: int):
        self.screen_width = width
        self.screen_height = height

    def set_music_level(self, level: int):
        self.music_level = level

    def __str__(self):
        return f"Resident Evil 4 settings ⚙️  <{id(self)}>\n" \
               f"Screen resolution ⌞ ⌝: {self.screen_width}x{self.screen_height}\n" \
               f"Music level 🎶: {self.music_level}%\n"


if __name__ == "__main__":
    separator = f"\n{'_' * 60}\n"
    game_settings1 = GameSettings()

    print(f"Game settings 1 {separator}")
    print(game_settings1)

    game_settings2 = GameSettings()
    print(f"Game settings 2 {separator}")
    print(game_settings2)

    game_settings1.set_music_level(95)
    game_settings2.set_screen_resolution(1200, 900)

    print(f"Game settings 1 {separator}")
    print(game_settings1)
    print(f"Game settings 2 {separator}")
    print(game_settings2)