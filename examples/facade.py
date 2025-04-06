class Graphics:
    def render(self):
        print("🎨 Rendering game world...")

class Physics:
    def update(self):
        print("⚙️ Updating physics engine...")

class Audio:
    def play_music(self):
        print("🎵 Playing background music...")

class InputHandler:
    def process_input(self):
        print("🎮 Processing player input...")

class GameFacade:
    def __init__(self):
        self.graphics = Graphics()
        self.physics = Physics()
        self.audio = Audio()
        self.input_handler = InputHandler()

    def start_game(self):
        print("🚀 Starting the game...")
        self.audio.play_music()
        self.graphics.render()

    def update_game(self):
        self.input_handler.process_input()
        self.physics.update()
        self.graphics.render()


game = GameFacade()

game.start_game()
game.update_game()
