
"""
Artwork and assets used for
 cover, lasers, rockets, enemy and player
 sprites and wall sprites as well as sound effects
 apart from music (which I will source seperately)
 downloaded from http://kenney.nl
"""
import random
import math
import arcade
import pygame

pygame.init()

"""
Song "Ethereal Air" downloaded on youtube from a youtuber known as Xaltus
link here https://www.youtube.com/watch?v=Z61jo2Sk0FA
"""
pygame.mixer.music.load("song.mp3")

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

"""
I drew the instruction screens myself using word document as a blank sheet and converted the file into an image
using https://convertio.co/doc-png/
"""
INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3

MOVEMENT_SPEED = 5
BULLET_SPEED = 7


class Cover(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)


class Player1(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)


class Bullet(arcade.Sprite):
    def update(self):
        self.center_y += self.change_y
        self.center_x += self.change_x


class MyApplication(arcade.Window):


    def __init__(self, width, height):

        super().__init__(width, height)

        pygame.mixer.music.play(-1)


        arcade.set_background_color(arcade.color.AMAZON)


        self.current_state = INSTRUCTIONS_PAGE_0

        self.all_sprites_list = None
        self.bad_coin_list = None


        self.score = 0
        self.level = 1
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
        self.coin_sound = arcade.sound.load_sound("coin4.ogg")

        self.physics_engine = None

    def setup(self):
        "Image downloaded from http://www.deepcutstudio.com/product/terrain-tiles-cobblestone-road/"
        self.background = arcade.load_texture("123.jpg")
        "Image downloaded from http://www.pptgrounds.com/wp-content/uploads/2013/07/Metalic-Border-Frames-Backgrounds-800x600.jpg"
        self.background_2 = arcade.load_texture("imgres.jpg")
        "Image downloaded from http://fungyung.com/pyramid-wallpapers.html"
        self.background_3 = arcade.load_texture("imgres2.jpg")
        "Image downloaded from https://wallpapersafari.com/cool-space-background-wallpapers/"
        self.background_4 = arcade.load_texture("imgres3.jpg")
        "Made this image myself with word document"
        self.background_5 = arcade.load_texture("imgres4.jpg")

        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.cover_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()



        self.score = 0
        self.health = 50
        self.bullet = 15
        self.bulletdamage = 7
        self.enemy1_health = 50
        self.enemy_kill_count = 0




        self.player_sprite = Player1("player_idle.png",
                                     SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.all_sprites_list.append(self.player_sprite)
        self.player_list.append(self.player_sprite)



        enemy_1 = arcade.Sprite("enemy_1.png", SPRITE_SCALING)
        enemy_1.center_x = 400
        enemy_1.center_y = 550
        self.all_sprites_list.append(enemy_1)
        self.enemy_list.append(enemy_1)

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

        self.all_sprites_list.draw()


        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        output = "Health: " + str(self.health)
        arcade.draw_text(output, 10, 40, arcade.color.WHITE, 14)

        output = "Enemy Health: " + str(self.enemy1_health)
        arcade.draw_text(output, 650, 570, arcade.color.RED, 14)



        output = "Rockets: " + str(self.bullet)
        arcade.draw_text(output, 685, 40, arcade.color.WHITE, 14)

    def draw_game_over(self):

        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Enemies killed: " + str(self.enemy_kill_count)
        arcade.draw_text(output, 300, 295, arcade.color.WHITE, 24)

        output = "Final Score: {}".format(self.score)
        arcade.draw_text(output, 317, 350, arcade.color.WHITE, 24)

        output = "Click to restart"
        arcade.draw_text(output, 310, 240, arcade.color.WHITE, 24)

    def on_draw(self):

        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.background)
        if self.level == 4:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.background_2)
        if self.level == 5:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.background_2)
        if self.level == 6:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.background_2)
        if self.level == 7:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.background_3)
        if self.level == 8:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.background_3)
        if self.level == 9:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.background_3)
        if self.level == 10:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.background_4)
        if self.level == 11:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.background_5)

        output = "Level: " + str(self.level)
        arcade.draw_text(output, 20, 530, arcade.color.BLACK, 14)

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
            self.current_state = GAME_OVER
            self.draw_game_over()


    def on_mouse_press(self, x, y, button, modifiers):

        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.current_state = INSTRUCTIONS_PAGE_1
        elif self.current_state == INSTRUCTIONS_PAGE_1:

            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:

            self.setup()
            self.current_state = GAME_RUNNING
            self.level = 1
            pygame.mixer.music.load("song.mp3")
            pygame.mixer.music.play(-1)

    def shoot_rocket(self):
        if self.current_state == GAME_RUNNING:
            if self.health > 0:
                if self.bullet > 0:
                    arcade.sound.play_sound(self.gun_sound)

                    bullet = Bullet("laserBlue01.png", SPRITE_SCALING * 1.5)

                    self.bullet -= 1


                    bullet.angle = 0

                    bullet.change_y = BULLET_SPEED


                    bullet.center_x = self.player_sprite.center_x
                    bullet.bottom = self.player_sprite.top + 10


                    self.all_sprites_list.append(bullet)
                    self.bullet_list.append(bullet)

    def on_key_press(self, key, modifiers):

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
            if key == arcade.key.Q:
                quit()

    def on_key_release(self, key, modifiers):


        if self.health > 0:
            if key == arcade.key.UP or key == arcade.key.DOWN:
                self.player_sprite.change_y = 0
            elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.player_sprite.change_x = 0

    def animate(self, delta_time):

        if self.current_state == GAME_RUNNING:
            if self.health > 0:
                self.bullet_list.update()
                self.wall_list.update()
                self.coin_list.update()
                self.cover_list.update()

                if len(self.enemy_list) == 0:
                    self.level += 1

                    if self.level == 2:
                        enemy = arcade.Sprite("enemy_1.png", SPRITE_SCALING)
                        enemy.center_x = 400
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)
                        self.enemy1_health = 175
                        self.bullet = 25

                        enemy = arcade.Sprite("spaceShips_009.png", SPRITE_SCALING)
                        enemy.center_x = 300
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)

                        superbullet_pwu = arcade.Sprite("super bullet powerup.png", SPRITE_SCALING)
                        superbullet_pwu.center_x = 400
                        superbullet_pwu.center_y = 200
                        self.all_sprites_list.append(superbullet_pwu)
                        self.coin_list.append(superbullet_pwu)

                        cover = Cover("crate_05.png", SPRITE_SCALING)
                        cover.center_x = 500
                        cover.center_y = 200
                        self.all_sprites_list.append(cover)
                        self.wall_list.append(cover)
                        self.cover_list.append(cover)

                        cover = Cover("crate_05.png", SPRITE_SCALING)
                        cover.center_x = 300
                        cover.center_y = 200
                        self.all_sprites_list.append(cover)
                        self.wall_list.append(cover)
                        self.cover_list.append(cover)

                    if self.level == 3:
                        enemy = arcade.Sprite("enemy_1.png", SPRITE_SCALING)
                        enemy.center_x = 400
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)
                        self.enemy1_health = 225

                        enemy = arcade.Sprite("spaceShips_002.png", SPRITE_SCALING)
                        enemy.center_x = 500
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)

                        ammo_pwu = arcade.Sprite("ammo powerup.png", SPRITE_SCALING)
                        ammo_pwu.center_x = 400
                        ammo_pwu.center_y = 200
                        self.all_sprites_list.append(ammo_pwu)
                        self.coin_list.append(ammo_pwu)

                    if self.level == 4:
                        """
                        Song "2ND MYSTERIOUS PLACE [UNDERTALE Q-mix]" downloaded on youtube from a youtuber known as Rukunetsu
link here https://www.youtube.com/watch?v=jfLWImAl1q0&t=38s
                        """
                        pygame.mixer.music.load("song2.mp3")
                        pygame.mixer.music.play(-1)

                        enemy = arcade.Sprite("towerDefense_tile245.png", SPRITE_SCALING)
                        enemy.center_x = 400
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)
                        self.enemy1_health = 250
                        self.health = 50

                        ammo_pwu = arcade.Sprite("ammo powerup.png", SPRITE_SCALING)
                        ammo_pwu.center_x = 400
                        ammo_pwu.center_y = 300
                        self.all_sprites_list.append(ammo_pwu)
                        self.coin_list.append(ammo_pwu)

                    if self.level == 5:
                        enemy = arcade.Sprite("barrelRed_up.png", SPRITE_SCALING)
                        enemy.center_x = 300
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)
                        self.enemy1_health = 300

                        enemy = arcade.Sprite("barrelRed_up.png", SPRITE_SCALING)
                        enemy.center_x = 500
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)

                        ammo_pwu = arcade.Sprite("ammo powerup.png", SPRITE_SCALING)
                        ammo_pwu.center_x = 400
                        ammo_pwu.center_y = 125
                        self.all_sprites_list.append(ammo_pwu)
                        self.coin_list.append(ammo_pwu)

                        ammo_pwu = arcade.Sprite("ammo powerup.png", SPRITE_SCALING)
                        ammo_pwu.center_x = 500
                        ammo_pwu.center_y = 125
                        self.all_sprites_list.append(ammo_pwu)
                        self.coin_list.append(ammo_pwu)

                    if self.level == 6:
                        enemy = arcade.Sprite("barrelRed_up.png", SPRITE_SCALING)
                        enemy.center_x = 300
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)
                        self.enemy1_health = 300

                        enemy = arcade.Sprite("barrelGreen_up.png", SPRITE_SCALING)
                        enemy.center_x = 500
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)

                        enemy = arcade.Sprite("towerDefense_tile245.png", SPRITE_SCALING)
                        enemy.center_x = 400
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)

                        ammo_pwu = arcade.Sprite("ammo powerup.png", SPRITE_SCALING)
                        ammo_pwu.center_x = 400
                        ammo_pwu.center_y = 300
                        self.all_sprites_list.append(ammo_pwu)
                        self.coin_list.append(ammo_pwu)

                    if self.level == 7:
                        """
                        "Song Downloaded on youtube is an instrumental edit from a song on the sonic adventure battle 2 soundtrack"
                        link is here https://www.youtube.com/watch?v=5tjq1iVYiiE
                        """
                        pygame.mixer.music.load("song3.mp3")
                        pygame.mixer.music.play(-1)

                        enemy = arcade.Sprite("enemySpikey_1.png", SPRITE_SCALING * 2)
                        enemy.center_x = 275
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)
                        self.health = 50
                        self.enemy1_health = 375

                        enemy = arcade.Sprite("enemySpikey_4.png", SPRITE_SCALING * 2)
                        enemy.center_x = 525
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)

                        ammo_pwu = arcade.Sprite("ammo powerup.png", SPRITE_SCALING)
                        ammo_pwu.center_x = 400
                        ammo_pwu.center_y = 300
                        self.all_sprites_list.append(ammo_pwu)
                        self.coin_list.append(ammo_pwu)

                        ammo_pwu = arcade.Sprite("ammo powerup.png", SPRITE_SCALING)
                        ammo_pwu.center_x = 500
                        ammo_pwu.center_y = 300
                        self.all_sprites_list.append(ammo_pwu)
                        self.coin_list.append(ammo_pwu)

                    if self.level == 8:
                        enemy = arcade.Sprite("enemySpikey_1.png", SPRITE_SCALING * 2)
                        enemy.center_x = 275
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)
                        self.enemy1_health = 375

                        enemy = arcade.Sprite("enemySpikey_2.png", SPRITE_SCALING * 2)
                        enemy.center_x = 400
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)

                        enemy = arcade.Sprite("enemySpikey_4.png", SPRITE_SCALING * 2)
                        enemy.center_x = 525
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)

                        ammo_pwu = arcade.Sprite("ammo powerup.png", SPRITE_SCALING)
                        ammo_pwu.center_x = 400
                        ammo_pwu.center_y = 300
                        self.all_sprites_list.append(ammo_pwu)
                        self.coin_list.append(ammo_pwu)

                        ammo_pwu = arcade.Sprite("ammo powerup.png", SPRITE_SCALING)
                        ammo_pwu.center_x = 500
                        ammo_pwu.center_y = 300
                        self.all_sprites_list.append(ammo_pwu)
                        self.coin_list.append(ammo_pwu)

                    if self.level == 9:
                        enemy = arcade.Sprite("enemySpikey_1.png", SPRITE_SCALING * 2)
                        enemy.center_x = 275
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)
                        self.enemy1_health = 425

                        enemy = arcade.Sprite("enemySpikey_2.png", SPRITE_SCALING * 2)
                        enemy.center_x = 400
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)

                        enemy = arcade.Sprite("enemyspikey_4.png", SPRITE_SCALING * 2)
                        enemy.center_x = 525
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)

                        enemy = arcade.Sprite("enemyFlyingAlt_1.png", SPRITE_SCALING * 2)
                        enemy.center_x = 575
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)

                        enemy = arcade.Sprite("enemyFloating_1.png", SPRITE_SCALING * 2)
                        enemy.center_x = 225
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)

                        ammo_pwu = arcade.Sprite("ammo powerup.png", SPRITE_SCALING)
                        ammo_pwu.center_x = 400
                        ammo_pwu.center_y = 300
                        self.all_sprites_list.append(ammo_pwu)
                        self.coin_list.append(ammo_pwu)

                        ammo_pwu = arcade.Sprite("ammo powerup.png", SPRITE_SCALING)
                        ammo_pwu.center_x = 500
                        ammo_pwu.center_y = 300
                        self.all_sprites_list.append(ammo_pwu)
                        self.coin_list.append(ammo_pwu)

                    if self.level == 10:
                        """
                        Song downloaded from youtube musician Rukunetsu,
                        remix of Ghost in the shell soundtrack link is here
                        https://www.youtube.com/watch?v=Zi_o_5xIwH8
                        """
                        pygame.mixer.music.load("song4.mp3")
                        pygame.mixer.music.play(-1)

                        """
                        These are images of my professors that I have had in the computer
                        science field of courses Todd Little, my advisor Mark Brodie
                        and the professor who contributed heavily to my knowledge on this
                        course on python, Paul Craven. Special Thanks link to images I used are here
                        http://simpson.edu/computer-science/faculty-and-staff/
                        """

                        enemy = arcade.Sprite("characterSpecial (3).png", SPRITE_SCALING * 1.5)
                        enemy.center_x = 400
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)
                        self.enemy1_health = 2500
                        self.health = 35

                        enemy = arcade.Sprite("Todd-Little-296x167.png", SPRITE_SCALING)
                        enemy.center_x = 300
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)

                        enemy = arcade.Sprite("Comp-Sci-Dept2.png", SPRITE_SCALING)
                        enemy.center_x = 500
                        enemy.center_y = 550
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)

                        ammo_pwu = arcade.Sprite("ammo powerup.png", SPRITE_SCALING)
                        ammo_pwu.center_x = 400
                        ammo_pwu.center_y = 300
                        self.all_sprites_list.append(ammo_pwu)
                        self.coin_list.append(ammo_pwu)

                    if self.level == 11:
                        """
                        Song downloaded from youtube, mario kart wii, wifi lobby music
                        link is here https://www.youtube.com/watch?v=yjkISc-5ZcI
                        """
                        pygame.mixer.music.load("song5.mp3")
                        pygame.mixer.music.play(-1)

                        enemy = arcade.Sprite("star_gold.png", SPRITE_SCALING * 2)
                        enemy.center_x = 600
                        enemy.center_y = 200
                        self.all_sprites_list.append(enemy)
                        self.enemy_list.append(enemy)
                        self.enemy1_health = 1
                        self.health = 75

                if self.level == 12:
                    pygame.mixer.music.load("song.mp3")
                    pygame.mixer.music.play(-1)
                    self.bulletdamage = 7

                    if len(self.enemy_list) == 0:
                        self.level = 1


                for enemy in self.enemy_list:

                    if random.randrange(100) == 0:
                        bullet_bad1 = Bullet("laserBlue16.png", SPRITE_SCALING * 1.5)

                        arcade.sound.play_sound(self.enemygun_sound)


                        start_x = enemy.center_x
                        start_y = enemy.center_y
                        bullet_bad1.center_x = start_x
                        bullet_bad1.center_y = start_y - 55


                        dest_x = self.player_sprite.center_x
                        dest_y = self.player_sprite.center_y

                        x_diff = dest_x - start_x
                        y_diff = dest_y - start_y
                        angle = math.atan2(y_diff, x_diff)


                        bullet_bad1.angle = math.degrees(angle) - 90


                        bullet_bad1.change_x = math.cos(angle) * BULLET_SPEED
                        bullet_bad1.change_y = math.sin(angle) * BULLET_SPEED

                        self.all_sprites_list.append(bullet_bad1)
                        self.bullet_list.append(bullet_bad1)

                for enemy in self.enemy_list:

                    if random.randrange(100) == 0:
                        bullet_bad1 = Bullet("laserRed16.png", SPRITE_SCALING * 1.5)

                        arcade.sound.play_sound(self.enemygun_sound)

                        #  How to create enemies that can shoot at player
                        start_x = enemy.center_x
                        start_y = enemy.center_y
                        bullet_bad1.center_x = start_x
                        bullet_bad1.center_y = start_y - 55

                        dest_x = self.player_sprite.center_x
                        dest_y = self.player_sprite.center_y

                        x_diff = dest_x - start_x
                        y_diff = dest_y - start_y
                        angle = math.atan2(y_diff, x_diff)

                        bullet_bad1.angle = math.degrees(angle) - 90

                        bullet_bad1.change_x = math.cos(angle) * BULLET_SPEED
                        bullet_bad1.change_y = math.sin(angle) * BULLET_SPEED

                        self.all_sprites_list.append(bullet_bad1)
                        self.bullet_list.append(bullet_bad1)

                for cover in self.cover_list:
                    hit_list = arcade.check_for_collision_with_list(cover,
                                                                    self.bullet_list)

                    for bullet_bad1 in hit_list:
                        bullet_bad1.kill()

                for bullet in self.bullet_list:

                    if bullet.bottom > SCREEN_HEIGHT:
                        bullet.kill()

                    hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bullet_list)

                    for bullet_bad1 in hit_list:
                        bullet_bad1.kill()
                        self.health -= 7

                        arcade.sound.play_sound(self.hurt_sound)

                    hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

                    for enemy_1 in hit_list:
                        bullet.kill()
                        self.enemy1_health -= self.bulletdamage
                        if self.enemy1_health < 0:
                            enemy_1.kill()
                            self.enemy_kill_count += 1
                            self.score += 10

                        arcade.sound.play_sound(self.hit_sound)

                    hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

                    for ammo_pwu in hit_list:
                        ammo_pwu.kill()
                        self.bullet += 10

                        arcade.sound.play_sound(self.coin_sound)

                    for superbullet_pwu in hit_list:
                        superbullet_pwu.kill()
                        self.bulletdamage += 5
                        arcade.sound.play_sound(self.coin_sound)

                    hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

                    for enemy_2 in hit_list:
                        bullet.kill()
                        self.enemy1_health -= 5
                        if self.enemy1_health < 15:
                            enemy_2.kill()
                            self.enemy_kill_count += 1
                            self.score += 10
                            if enemy_2.kill():
                                self.enemy_kill_count += 1

                        arcade.sound.play_sound(self.hit_sound)

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
