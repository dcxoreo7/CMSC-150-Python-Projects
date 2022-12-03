"""
Sprite Move With Walls

Simple program to show basic sprite usage.

Artwork from http://kenney.nl
"""
import random
import math
import arcade
import pygame

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3

MOVEMENT_SPEED = 5
BULLET_SPEED = 5
METEOR_SPEED = 0



class Cover(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

class Player1(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

class Bullet(arcade.Sprite):
    def update(self):
        self.center_y += self.change_y
        self.center_x += self.change_x

class Meteor(arcade.Sprite):

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
        self.center_y += METEOR_SPEED - 2

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class MyApplication(arcade.Window):
    """ Main application class. """


    def __init__(self, width, height):
        """
        Initializer
        """
        super().__init__(width, height)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Start 'state' will be showing the first page of instructions.
        self.current_state = INSTRUCTIONS_PAGE_0

        self.all_sprites_list = None
        self.coin_list = None

        # Set up the player
        self.score = 0
        self.health = 100
        self.bullet = 15
        self.player_sprite = None
        self.wall_list = None

        self.instructions = []
        texture = arcade.load_texture("instructions_0.png")
        self.instructions.append(texture)

        texture = arcade.load_texture("instructions_1.png")
        self.instructions.append(texture)

        self.gun_sound = arcade.sound.load_sound("laser2.ogg")
        self.hit_sound = arcade.sound.load_sound("hit2.ogg")
        self.hurt_sound = arcade.sound.load_sound("hurt3.ogg")
        self.enemygun_sound = arcade.sound.load_sound("laser4.ogg")
        # This variable holds our simple "physics engine"
        self.physics_engine = None

        # pygame.init()
        # song = pygame.mixer.Sound("02-leave-alone-rare-.ogg")
        # clock = pygame.time.Clock()
        # song.play()
        # while True:
        #     clock.tick(60)
        # pygame.quit()



    def setup(self):
        """ Set up the game and initialize the variables. """



        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.cover_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        # self.pwu_list = arcade.SpriteList()


        # character downloaded from http://kenney.nl
        self.score = 0
        self.health = 200
        self.bullet = 30
        self.enemy1_health = 100
        self.enemy_kill_count = 0

        # if self.bullet < 1:
        #     rocket_pwu = arcade.Sprite("spaceMissiles_021.png")
        #     rocket_pwu.center_x = 380
        #     rocket_pwu.center_y = 300
        #     self.all_sprites_list.append(rocket_pwu)
        #     self.pwu_list.append(rocket_pwu)



        self.player_sprite = Player1("player_idle.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.all_sprites_list.append(self.player_sprite)
        self.player_list.append(self.player_sprite)

        cover = Cover("crate_05.png", SPRITE_SCALING)
        cover.center_x = 300
        cover.center_y = 200
        self.all_sprites_list.append(cover)
        self.wall_list.append(cover)
        self.cover_list.append(cover)

        # enemy_2 = arcade.Sprite("spaceShips_009.png", SPRITE_SCALING)
        # enemy_2.center_x = 300
        # enemy_2.center_y = 550
        # self.all_sprites_list.append(enemy_2)
        # self.enemy_list.append(enemy_2)

        # enemy_3 = arcade.Sprite("spaceShips_002.png", SPRITE_SCALING)
        # enemy_3.center_x = 500
        # enemy_3.center_y = 550
        # self.all_sprites_list.append(enemy_3)
        # self.enemy_list.append(enemy_3)

        enemy_1 = arcade.Sprite("enemy_1.png", SPRITE_SCALING)
        enemy_1.center_x = 400
        enemy_1.center_y = 550
        self.all_sprites_list.append(enemy_1)
        self.enemy_list.append(enemy_1)

        cover = Cover("crate_05.png", SPRITE_SCALING)
        cover.center_x = 500
        cover.center_y = 200
        self.all_sprites_list.append(cover)
        self.wall_list.append(cover)
        self.cover_list.append(cover)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.cover_list)

        for x in range(95, 720, 64):
            wall = arcade.Sprite("crate_02.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 400
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        wall = arcade.Sprite("crate_02.png", SPRITE_SCALING)
        wall.center_x = 705
        wall.center_y = 400
        self.all_sprites_list.append(wall)
        self.wall_list.append(wall)


        for i in range(15):
            # Create the coin instance
            coin = Meteor("coin_01.png", SPRITE_SCALING)

            # Position the coin
            coin.center_x = random.randrange(125, 675)
            coin.center_y = random.randrange(500, 600)

            # Random radius from 10 to 200
            coin.radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            coin.angle = random.random() * 2 * math.pi

            # Add the coin to the lists
            self.all_sprites_list.append(coin)
            self.coin_list.append(coin)

        for y in range(25, 450, 64):
            wall = arcade.Sprite("crate_43.png", SPRITE_SCALING)
            wall.center_y = y
            wall.center_x = 770
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        for y in range(25, 450, 64):
            wall = arcade.Sprite("crate_19.png", SPRITE_SCALING)
            wall.center_y = y
            wall.center_x = 30
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        for x in range(95, 720, 64):
            wall = arcade.Sprite("grassMid.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 25
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)



        wall = arcade.Sprite("grassMid.png", SPRITE_SCALING)
        wall.center_x = 705
        wall.center_y = 25
        self.all_sprites_list.append(wall)
        self.wall_list.append(wall)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)

    def draw_instructions_page(self, page_number):
        """
        Draw an instruction page. Load the page as an image.
        """
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)

    def draw_game(self):
        """
        Draw all the sprites, along with the score.
        """
        # Draw all the sprites.
        self.all_sprites_list.draw()

        # Put the text on the screen.
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        output = "Health: " + str(self.health)
        arcade.draw_text(output, 10, 40, arcade.color.WHITE, 14)

        output = "Enemy Health: " + str(self.enemy1_health)
        arcade.draw_text(output, 650,570,arcade.color.RED, 14)

        output = "Enemies killed: " + str(self.enemy_kill_count)
        arcade.draw_text(output, 650, 545, arcade.color.RED, 14)

        output = "Rockets: " + str(self.bullet)
        arcade.draw_text(output, 685, 40, arcade.color.WHITE, 14)

    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Click to restart"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)

    def draw_game_win(self):
        """
        Draw "Game over" across the screen.
        """
        output = "You Win"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Congratz"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instructions_page(0)

        elif self.current_state == INSTRUCTIONS_PAGE_1:
            self.draw_instructions_page(1)

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        else:
            self.draw_game()
            self.draw_game_over()

        if self.health < 1:
            self.draw_game_over()

        if self.enemy_kill_count > 0:
            self.draw_game_win()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        if self.current_state == INSTRUCTIONS_PAGE_0:
            # Next page of instructions.
            self.current_state = INSTRUCTIONS_PAGE_1
        elif self.current_state == INSTRUCTIONS_PAGE_1:
            # Start the game
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            # Restart the game.
            self.setup()
            self.current_state = GAME_RUNNING

    def shoot_rocket(self):
        if self.current_state == GAME_RUNNING:
            if self.health > 0:
                if self.bullet > 0:
                    arcade.sound.play_sound(self.gun_sound)

                    bullet = Bullet("laserBlue01.png", SPRITE_SCALING * 1.5)

                    self.bullet -= 1

                    # The image points to the right, and we want it to point up. So
                    # rotate it.
                    bullet.angle = 0

                    bullet.change_y = BULLET_SPEED

                    # Position the bullet
                    bullet.center_x = self.player_sprite.center_x
                    bullet.bottom = self.player_sprite.top + 10

                    # Add the bullet to the appropriate lists
                    self.all_sprites_list.append(bullet)
                    self.bullet_list.append(bullet)



    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if self.current_state == GAME_RUNNING:
            if self.health > 0:
                if key == arcade.key.UP:
                    self.player_sprite.change_y = MOVEMENT_SPEED
                elif key == arcade.key.DOWN:
                    self.player_sprite.change_y = -MOVEMENT_SPEED
                elif key == arcade.key.LEFT:
                    self.player_sprite.change_x = -MOVEMENT_SPEED
                elif key == arcade.key.RIGHT:
                    self.player_sprite.change_x = MOVEMENT_SPEED
                elif key == arcade.key.SPACE:
                    self.shoot_rocket()


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if self.health > 0:
            if key == arcade.key.UP or key == arcade.key.DOWN:
                self.player_sprite.change_y = 0
            elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.player_sprite.change_x = 0

    def animate(self, delta_time):
        """ Movement and game logic """
        if self.current_state == GAME_RUNNING:
            if self.health > 0:
                self.coin_list.update()
                self.bullet_list.update()
                self.wall_list.update()
                self.cover_list.update()



                for enemy_1 in self.enemy_list:

                        if random.randrange(150) == 0:

                            bullet_bad1 = Bullet("laserBlue16.png", SPRITE_SCALING * 1.5)

                            arcade.sound.play_sound(self.enemygun_sound)

                            #  How to create enemies that can shoot at player
                            start_x = enemy_1.center_x
                            start_y = enemy_1.center_y
                            bullet_bad1.center_x = start_x
                            bullet_bad1.center_y = start_y - 45

                            # Get from the mouse the destination location for the bullet
                            dest_x = self.player_sprite.center_x
                            dest_y = self.player_sprite.center_y

                            # Do math to calculate how to get the bullet to the destination.
                            # Calculation the angle in radians between the start points
                            # and end points. This is the angle the bullet will travel.
                            x_diff = dest_x - start_x
                            y_diff = dest_y - start_y
                            angle = math.atan2(y_diff, x_diff)
                            print("Bullet angle: {:.2f}".format(bullet_bad1.angle))

                            # Angle the bullet sprite so it doesn't look like it is flying
                            # sideways.
                            bullet_bad1.angle = math.degrees(angle)-90

                            # Taking into account the angle, calculate our change_x
                            # and change_y. Velocity is how fast the bullet travels.
                            bullet_bad1.change_x = math.cos(angle) * BULLET_SPEED
                            bullet_bad1.change_y = math.sin(angle) * BULLET_SPEED

                            # Add the bullet to the appropriate lists
                            self.all_sprites_list.append(bullet_bad1)
                            self.bullet_list.append(bullet_bad1)

                # for enemy_2 in self.enemy_list:
                #
                #         if random.randrange(50) == 0:
                #
                #             bullet_bad1 = Bullet("laserBlue16.png", SPRITE_SCALING * 1.5)
                #
                #             arcade.sound.play_sound(self.enemygun_sound)
                #
                #             #  How to create enemies that can shoot at player
                #             start_x = enemy_2.center_x
                #             start_y = enemy_2.center_y
                #             bullet_bad1.center_x = start_x
                #             bullet_bad1.center_y = start_y - 45
                #
                #             # Get from the mouse the destination location for the bullet
                #             dest_x = self.player_sprite.center_x
                #             dest_y = self.player_sprite.center_y
                #
                #             # Do math to calculate how to get the bullet to the destination.
                #             # Calculation the angle in radians between the start points
                #             # and end points. This is the angle the bullet will travel.
                #             x_diff = dest_x - start_x
                #             y_diff = dest_y - start_y
                #             angle = math.atan2(y_diff, x_diff)
                #             print("Bullet angle: {:.2f}".format(bullet_bad1.angle))
                #
                #             # Angle the bullet sprite so it doesn't look like it is flying
                #             # sideways.
                #             bullet_bad1.angle = math.degrees(angle)-90
                #
                #             # Taking into account the angle, calculate our change_x
                #             # and change_y. Velocity is how fast the bullet travels.
                #             bullet_bad1.change_x = math.cos(angle) * BULLET_SPEED
                #             bullet_bad1.change_y = math.sin(angle) * BULLET_SPEED
                #
                #             # Add the bullet to the appropriate lists
                #             self.all_sprites_list.append(bullet_bad1)
                #             self.bullet_list.append(bullet_bad1)

                # for enemy_3 in self.enemy_list:
                #
                #         if random.randrange(50) == 0:
                #
                #             bullet_bad1 = Bullet("laserBlue16.png", SPRITE_SCALING * 1.5)
                #
                #             arcade.sound.play_sound(self.enemygun_sound)
                #
                #             #  How to create enemies that can shoot at player
                #             start_x = enemy_3.center_x
                #             start_y = enemy_3.center_y
                #             bullet_bad1.center_x = start_x
                #             bullet_bad1.center_y = start_y - 45
                #
                #             # Get from the mouse the destination location for the bullet
                #             dest_x = self.player_sprite.center_x
                #             dest_y = self.player_sprite.center_y
                #
                #             # Do math to calculate how to get the bullet to the destination.
                #             # Calculation the angle in radians between the start points
                #             # and end points. This is the angle the bullet will travel.
                #             x_diff = dest_x - start_x
                #             y_diff = dest_y - start_y
                #             angle = math.atan2(y_diff, x_diff)
                #             print("Bullet angle: {:.2f}".format(bullet_bad1.angle))
                #
                #             # Angle the bullet sprite so it doesn't look like it is flying
                #             # sideways.
                #             bullet_bad1.angle = math.degrees(angle)-90
                #
                #             # Taking into account the angle, calculate our change_x
                #             # and change_y. Velocity is how fast the bullet travels.
                #             bullet_bad1.change_x = math.cos(angle) * BULLET_SPEED
                #             bullet_bad1.change_y = math.sin(angle) * BULLET_SPEED
                #
                #             # Add the bullet to the appropriate lists
                #             self.all_sprites_list.append(bullet_bad1)
                #             self.bullet_list.append(bullet_bad1)




                hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                    self.coin_list)



                for coin in hit_list:
                    coin.kill()
                    self.health -= 10
                    self.score -= 1

                    arcade.sound.play_sound(self.hurt_sound)


                for cover in self.cover_list:
                    hit_list = arcade.check_for_collision_with_list(cover,
                                                                    self.bullet_list)

                    for bullet_bad1 in hit_list:
                        bullet_bad1.kill()

                for cover in self.cover_list:
                    hit_list = arcade.check_for_collision_with_list(cover,
                                                                    self.coin_list)

                    for coin in hit_list:
                        coin.kill()


                for bullet in self.bullet_list:
                    hit_list = arcade.check_for_collision_with_list(bullet,
                                                                    self.coin_list)

                    if len(hit_list) > 0:
                        bullet.kill()

                    for coin in hit_list:
                        coin.kill()
                        self.score += 1

                        arcade.sound.play_sound(self.hit_sound)


                    if bullet.bottom > SCREEN_HEIGHT:
                        bullet.kill()



                    hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.bullet_list)



                    for bullet_bad1 in hit_list:
                        bullet_bad1.kill()
                        self.health -= 5

                        arcade.sound.play_sound(self.hurt_sound)

                    hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

                    for enemy_1 in hit_list:
                        bullet.kill()
                        self.enemy1_health -= 5
                        if self.enemy1_health < 15:
                            enemy_1.kill()
                            self.enemy_kill_count += 1
                            self.score += 10
                            if enemy_1.kill():
                                self.enemy_kill_count += 1

                        arcade.sound.play_sound(self.hit_sound)

                    # hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
                    #
                    # for enemy_2 in hit_list:
                    #     bullet.kill()
                    #     self.enemy1_health -= 5
                    #     if self.enemy1_health < 15:
                    #         enemy_2.kill()
                    #         self.enemy_kill_count += 1
                    #         self.score += 10
                    #         if enemy_2.kill():
                    #             self.enemy_kill_count += 1

                        arcade.sound.play_sound(self.hit_sound)

                    # hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
                    #
                    # for enemy_3 in hit_list:
                    #     bullet.kill()
                    #     self.enemy1_health -= 5
                    #     if self.enemy1_health < 15:
                    #         enemy_3.kill()
                    #         self.enemy_kill_count += 1
                    #         self.score += 10
                    #         if enemy_3.kill():
                    #             self.enemy_kill_count += 1
                    #
                    #     arcade.sound.play_sound(self.hit_sound)

        # Generate a list of all sprites that collided with the player.
        # Loop through each colliding sprite, remove it, and add to the score.
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
                self.physics_engine.update()

                if self.player_sprite.left < 0:
                    self.player_sprite.left = 0
                elif self.player_sprite.right > 800:
                    self.player_sprite.right = 800
                elif self.player_sprite.top > 450:
                    self.player_sprite.top = 450


window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
window.setup()

arcade.run()
