"""
Sprite Move With Walls

Simple program to show basic sprite usage.

Artwork from http://kenney.nl
"""
import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyApplication(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        """
        Initializer
        """
        super().__init__(width, height)
        # Sprite lists
        self.all_sprites_list = None
        self.coin_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None
        self.wall_list = None

        # This variable holds our simple "physics engine"
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # character downloaded from http://zfgc.com/forum/index.php?topic=39377.0
        self.score = 0
        self.player_sprite = arcade.Sprite("character.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.all_sprites_list.append(self.player_sprite)

        # Coin downloaded from http://zelda.wikia.com/wiki/Rupee
        coin = arcade.Sprite("coin_01.png", SPRITE_SCALING)
        coin.center_x = 100
        coin.center_y = 477
        self.all_sprites_list.append(coin)
        self.coin_list.append(coin)

        coin = arcade.Sprite("coin_01.png", SPRITE_SCALING)
        coin.center_x = 700
        coin.center_y = 477
        self.all_sprites_list.append(coin)
        self.coin_list.append(coin)

        coin = arcade.Sprite("coin_01.png", SPRITE_SCALING)
        coin.center_x = 700
        coin.center_y = 100
        self.all_sprites_list.append(coin)
        self.coin_list.append(coin)

        coin = arcade.Sprite("coin_01.png", SPRITE_SCALING)
        coin.center_x = 480
        coin.center_y = 221
        self.all_sprites_list.append(coin)
        self.coin_list.append(coin)

        coin = arcade.Sprite("coin_01.png", SPRITE_SCALING)
        coin.center_x = 497
        coin.center_y = 350
        self.all_sprites_list.append(coin)
        self.coin_list.append(coin)

        coin = arcade.Sprite("coin_01.png", SPRITE_SCALING)
        coin.center_x = 363
        coin.center_y = 350
        self.all_sprites_list.append(coin)
        self.coin_list.append(coin)

        coin = arcade.Sprite("coin_01.png", SPRITE_SCALING)
        coin.center_x = 107
        coin.center_y = 350
        self.all_sprites_list.append(coin)
        self.coin_list.append(coin)

        coin = arcade.Sprite("coin_01.png", SPRITE_SCALING)
        coin.center_x = 287
        coin.center_y = 100
        self.all_sprites_list.append(coin)
        self.coin_list.append(coin)


        # Grass downloaded from http://kenney.nl/
        for x in range(25, 800, 64):
            wall = arcade.Sprite("grass.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 30
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        # Block_08 downloaded from http://kenney.nl/
        wall = arcade.Sprite("block_08.png", SPRITE_SCALING)
        wall.center_x = 90
        wall.center_y = 270
        self.all_sprites_list.append(wall)
        self.wall_list.append(wall)

        # StoneCenter_rounded downloaded from http://kenney.nl/
        for x in range(25, 800, 64):
            wall = arcade.Sprite("stoneCenter_rounded.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 542
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        for x in range(350, 650, 64):
            wall = arcade.Sprite("block_08.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 285
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        for x in range(570, 700, 64):
            wall = arcade.Sprite("block_08.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 413
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        for x in range(100, 300, 64):
            wall = arcade.Sprite("block_08.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 413
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        # Create a column of boxes
        for y in range(93, 540, 64):
            wall = arcade.Sprite("stoneCenter_rounded.png", SPRITE_SCALING)
            wall.center_x = 770
            wall.center_y = y
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        for y in range(93, 300, 64):
            wall = arcade.Sprite("block_08.png", SPRITE_SCALING)
            wall.center_x = 220
            wall.center_y = y
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        for y in range(220, 300, 64):
            wall = arcade.Sprite("block_08.png", SPRITE_SCALING)
            wall.center_x = 613
            wall.center_y = y
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        for y in range(220, 300, 64):
            wall = arcade.Sprite("block_08.png", SPRITE_SCALING)
            wall.center_x = 350
            wall.center_y = y
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        for y in range(93, 200, 64):
            wall = arcade.Sprite("block_08.png", SPRITE_SCALING)
            wall.center_x = 478
            wall.center_y = y
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        wall = arcade.Sprite("block_08.png", SPRITE_SCALING)
        wall.center_x = 430
        wall.center_y = 475
        self.all_sprites_list.append(wall)
        self.wall_list.append(wall)

        wall = arcade.Sprite("block_08.png", SPRITE_SCALING)
        wall.center_x = 430
        wall.center_y = 412
        self.all_sprites_list.append(wall)
        self.wall_list.append(wall)

        wall = arcade.Sprite("block_08.png", SPRITE_SCALING)
        wall.center_x = 430
        wall.center_y = 349
        self.all_sprites_list.append(wall)
        self.wall_list.append(wall)

        for y in range(93, 540, 64):
            wall = arcade.Sprite("stoneCenter_rounded.png", SPRITE_SCALING)
            wall.center_x = 30
            wall.center_y = y
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.all_sprites_list.draw()

        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def animate(self, delta_time):
        """ Movement and game logic """

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            self.score += 1
            coin.kill()
            coin_good_sound = arcade.load_sound("coin2.ogg")
            arcade.play_sound(coin_good_sound)

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()


window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
window.setup()

arcade.run()