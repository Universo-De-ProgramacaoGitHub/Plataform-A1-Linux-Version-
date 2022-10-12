import arcade

# Set constants for the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Plataform A1")

def on_draw(self):
SPRITE_SCALING_PLAYER = 1.0

player = arcade.Sprite("player.png", SPRITE_SCALING_PLAYER)

SPRITE_SCALING_GRAMA = 1.0

grama = arcade.Sprite("grama.png", SPRITE_SCALING_GRAMA)

SPRITE_SCALING_BLOCO = 1.0

bloco = arcade.Sprite("bloco.png", SPRITE_SCALING_BLOCO)
    pass

def setup(self):
    """ Set up the game and initialize the variables. """

    # Create the sprite lists
    self.player_list = arcade.SpriteList()
    self.grama_list = arcade.SpriteList()
    self.bloco_list = arcade.SpriteList()
    
    # Set Up The Player
    # Character image from kenney.nl
    self.player_sprite = arcade.Sprite("player.png", SPRITE_SCALING_PLAYER)
    self.player_sprite.center_x = 50 # Starting position
    self.player_sprite.center_y = 50
    self.player_list.append(self.player_sprite)
