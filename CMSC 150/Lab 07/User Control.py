import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 20


def draw_window(position_x, position_y):
    """
    This function draws a window
    """

    arcade.draw_lrtb_rectangle_filled(position_x + 250, position_x + 500, position_y + 300, position_y + 100,
                                      arcade.color.SKY_BLUE)
    arcade.draw_lrtb_rectangle_outline(position_x + 250, position_x + 500, position_y + 300, position_y + 100,
                                       arcade.color.GOLDEN_BROWN)
    arcade.draw_line(position_x + 250, position_y + 205, position_x + 500, position_y + 205,
                     arcade.color.GOLDEN_BROWN, 1)
    arcade.draw_line(position_x + 375, position_y + 100, position_x + 375, position_y + 300,
                     arcade.color.GOLDEN_BROWN, 1)


def draw_door(position_x, position_y):
    """
    This function draws a door
    """

    # The door
    arcade.draw_lrtb_rectangle_filled(position_x + 175, position_x + 350, position_y + 250, position_y,
                                      arcade.color.ROAST_COFFEE)

    # The doorknob
    arcade.draw_lrtb_rectangle_filled(position_x + 280, position_x + 325, position_y + 150, position_y + 100,
                                      arcade.color.GOLDEN_BROWN)

class Window_house:
    def __init__(self, position_x, position_y, change_x, change_y):
        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        draw_window(self.position_x, self.position_y)

    def animate(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction

        if self.position_x > SCREEN_WIDTH:
            self.change_x *= -1

        if self.position_y > SCREEN_HEIGHT:
            self.change_y *= -1

class MyApplication(arcade.Window):


    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        self.ball_x_position = BALL_RADIUS
        self.ball_x_pixels_per_second = 70

        self.position_x = 70

        self.window_house = Window_house(100,130,0,0)

        # Note:
        # You can change how often the animate() method is called by using the
        # set_update_rate() method in the parent class.
        # The default is once every 1/80 of a second.
        # self.set_update_rate(1/80)



    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Two Face Background
        arcade.set_background_color(arcade.color.COOL_BLACK)

        arcade.draw_lrtb_rectangle_filled(0, 400, 650, 0, arcade.color.GHOST_WHITE)

        arcade.draw_rectangle_filled(250, 400, 300, 500, arcade.color.GOLDEN_BROWN)

        arcade.draw_rectangle_filled(550, 400, 300, 500, arcade.color.APPLE_GREEN)

        arcade.draw_circle_filled(280, 450, 100, arcade.color.FLORAL_WHITE)

        arcade.draw_circle_filled(525, 450, 100, arcade.color.BLACK_BEAN)

        arcade.draw_circle_filled(280, 450, 50, arcade.color.BLACK_BEAN)

        arcade.draw_circle_filled(525, 450, 50, arcade.color.CARMINE_RED)

        arcade.draw_rectangle_filled(285, 590, 200, 75, arcade.color.BLACK_BEAN)

        arcade.draw_rectangle_filled(520, 590, 200, 75, arcade.color.DARK_LAVA)

        arcade.draw_triangle_filled(325, 300, 400, 300, 400, 400, arcade.color.BROWN_NOSE)

        arcade.draw_triangle_filled(475, 300, 400, 300, 400, 400, arcade.color.DARK_CANDY_APPLE_RED)

        arcade.draw_line(275, 250, 550, 250, arcade.color.BLACK_BEAN, 400)

        arcade.draw_rectangle_filled(345, 229, 110, 35, arcade.color.WHITE_SMOKE)

        arcade.draw_rectangle_filled(462, 228.8, 123, 35, arcade.color.FIRE_ENGINE_RED)

        # Animated Circle
        arcade.draw_circle_filled(self.ball_x_position, SCREEN_HEIGHT // 2,
                                  BALL_RADIUS, arcade.color.GREEN)

        self.window_house.draw()

        # Draw the text
        arcade.draw_text("Why did the Craven write the code?  To on_draw the other side!!",
                         10, SCREEN_HEIGHT // 2, arcade.color.BLACK, 20)


    def animate(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        # Move the ball
        self.ball_x_position += self.ball_x_pixels_per_second * delta_time

        # Did the ball hit the right side of the screen while moving right?
        if self.ball_x_position > SCREEN_WIDTH - BALL_RADIUS \
                and self.ball_x_pixels_per_second > 0:
            self.ball_x_pixels_per_second *= -1

        # Did the ball hit the left side of the screen while moving left?
        if self.ball_x_position < BALL_RADIUS \
                and self.ball_x_pixels_per_second < 0:
            self.ball_x_pixels_per_second *= -1

        self.window_house.animate()



    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://pythonhosted.org/arcade/arcade.key.html
        """

        # See if the user hit Shift-Space
        # (Key modifiers are in powers of two, so you can detect multiple
        # modifiers by using a bit-wise 'and'.)
        if key == arcade.key.SPACE and key_modifiers == arcade.key.MOD_SHIFT:
            print("You pressed shift-space")

        # See if the user just hit space.
        elif key == arcade.key.SPACE:
            print("You pressed the space bar.")

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.SPACE:
            print("You stopped pressing the space bar.")

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)



arcade.run()