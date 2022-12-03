import arcade

# Create a window
arcade.open_window("Pattern", 1200, 600)

arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

arcade.start_render()

# Draw squares on bottom
arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

# Draw squares on top
arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)

# Section 1
for row in range(30):
    for column in range(30):
        x = (row * 10) + 5 # Instead of zero, calculate the proper x location using row
        y = (column * 10) + 5 # Instead of zero, calculate the proper y location using column
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 2
for row in range(30):
    for column in range(30):
        x = (row * 10) + 305
        y = (column * 10) + 5
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
        if row % 2:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK_BEAN)
# Use the modulus operator and an if statement to select the color

# Section 3
for row in range(30):
    for column in range(30):
        x = (row * 10) + 605
        y = (column * 10) + 5
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
        if column % 2:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK_BEAN)
# Use the modulus operator and an if statement to select the color

# Section 4
for row in range(30):
    for column in range(30):
        x = (row * 10) + 905
        y = (column * 10) + 5
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
        if column % 2:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK_BEAN)
        if row % 2:
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK_BEAN)

# Use the modulus operator and an if statement to select the color

# Section 5
for row in range(30):
    for column in range(row + 1):
        x = (row * 10) + 5
        y = (column * 10) + 305
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 6
for row in range(30):
    for column in range(30 - row):
        x = (row * 10) + 305
        y = (column * 10) + 305
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 7
for row in range(30):
    for column in range(31 - row):
        x = (row * 10) + 605 # Instead of zero, calculate the proper x location using row
        y = -(column * 10) + 605 # Instead of zero, calculate the proper y location using column
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

# Section 8
for row in range(30):
    for column in range(31 - row):
        x = -(row * 10) + 1195 # Instead of zero, calculate the proper x location using row
        y = -(column * 10) + 605 # Instead of zero, calculate the proper y location using column
        arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

arcade.finish_render()

arcade.run()