import random
import arcade
import math

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin_good(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.angle = 0

        # How far away from the center to orbit, in pixels
        self.radius = 0

        # How fast to orbit, in radians per frame
        self.speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def reset_pos(self):
        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

class Coin_bad(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.angle = 0

        # How far away from the center to orbit, in pixels
        self.radius = 0

        # How fast to orbit, in radians per frame
        self.speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):

        """ Update the ball's position. """
        # Calculate a new x, y
        self.center_x = self.radius * math.sin(self.angle) \
            + self.circle_center_x
        self.center_y = self.radius * math.cos(self.angle) \
            + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.angle += self.speed


class MyAppWindow(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):

        super().__init__(width, height)
        # Sprite lists
        self.all_sprites_list = None
        self.coin_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None

    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.good_coin_list = arcade.SpriteList()
        self.bad_coin_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Character sprite from http://lipsterhink.deviantart.com/art/Toon-Link-265200188
        self.player_sprite = arcade.Sprite("character.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.all_sprites_list.append(self.player_sprite)

        for i in range(50):

            # Create the coin instance

            # Good coin sprite from https://zeldawiki.org/Rupee
            coin = Coin_good("coin_01.png", SPRITE_SCALING / 3)

            # Position the center of the circle the coin will orbit
            coin.circle_center_x = random.randrange(SCREEN_WIDTH)
            coin.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            coin.radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            coin.angle = random.random() * 2 * math.pi

            # Add the coin to the lists
            self.all_sprites_list.append(coin)
            self.good_coin_list.append(coin)

        for i in range(10):

            # Create the coin instance

            # Bad coin sprite from http://www.deviantart.com/art/Legend-of-Zelda-Black-Rupee-Papercraft-611660164
            bad_coin = Coin_bad("coin_02.png", SPRITE_SCALING / 3)

            # Position the center of the circle the coin will orbit
            bad_coin.circle_center_x = random.randrange(SCREEN_WIDTH)
            bad_coin.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            bad_coin.radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            bad_coin.angle = random.random() * 2 * math.pi

            # Add the coin to the lists
            self.all_sprites_list.append(bad_coin)
            self.bad_coin_list.append(bad_coin)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        if len(self.good_coin_list) == 0:
            arcade.draw_text("                                              GAME OVER!!", 10, SCREEN_HEIGHT // 2, arcade.color.FLORAL_WHITE, 20)

        # Draw all the sprites.
        self.all_sprites_list.draw()

        # Put the text on the screen.
        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        if len(self.good_coin_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def animate(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)

        if len(self.good_coin_list) > 0:
            self.all_sprites_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.good_coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            self.score += 1
            coin.kill()
            coin_good_sound = arcade.load_sound("coin2.ogg")
            arcade.play_sound(coin_good_sound)


        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.bad_coin_list)

        for bad_coin in hit_list:
            self.score += -1
            bad_coin.kill()
            coin_bad_sound = arcade.load_sound("hurt5.ogg")
            arcade.play_sound(coin_bad_sound)

def main():
    window = MyAppWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()