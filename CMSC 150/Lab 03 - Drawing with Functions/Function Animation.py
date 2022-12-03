import arcade


def draw_window(position_x, position_y):
    """
    This function draws a window
    """

    arcade.draw_lrtb_rectangle_filled(position_x + 250,position_x + 500,position_y + 300,position_y + 100,arcade.color.SKY_BLUE)
    arcade.draw_lrtb_rectangle_outline(position_x + 250,position_x + 500,position_y + 300,position_y + 100, arcade.color.GOLDEN_BROWN)
    arcade.draw_line(position_x + 250,position_y + 205,position_x + 500,position_y + 205,arcade.color.GOLDEN_BROWN,1)
    arcade.draw_line(position_x + 375,position_y + 100,position_x + 375,position_y + 300,arcade.color.GOLDEN_BROWN,1)

def draw_door(position_x, position_y):
    """
    This function draws a door
    """

    # The door
    arcade.draw_lrtb_rectangle_filled(position_x + 175,position_x + 350,position_y + 250,position_y, arcade.color.ROAST_COFFEE)

    # The doorknob
    arcade.draw_lrtb_rectangle_filled(position_x + 280,position_x + 325,position_y + 150,position_y + 100,arcade.color.GOLDEN_BROWN)

def draw_house_framework(position_x,position_y):
    """
    This function draws the basic build of a house
    """

    # Basic structure
    arcade.draw_lrtb_rectangle_filled(position_x + 100,position_x + 700,position_y + 500,position_y + 25, arcade.color.WOOD_BROWN)
    # Roof
    arcade.draw_triangle_filled(position_x + 725,position_y + 500,position_x + 75,position_y + 500,position_x + 400,position_y + 600, arcade.color.BRICK_RED)

# rectangle -> left,right,top,bottom, color
# line -> start_x,start_y,end_x,end_y, color
# triangle -> x1,y1,x2,y2,x3,y3, color

def on_draw(delta_time):
    arcade.start_render()

    on_draw.position_x = on_draw.position_x + 4
    draw_house_framework(on_draw.position_x, 0)
    draw_door(on_draw.position_x + 140, 25)
    draw_window(on_draw.position_x + 185, 185)
    draw_window(on_draw.position_x + -135, 185)
    if on_draw.position_x >= 600:
        on_draw.position_x = -10
on_draw.position_x = -10

def main():
    """
    This is a house with two windows and a door
    """
    arcade.open_window("Function", 800,600)
    arcade.set_background_color(arcade.color.ANTIQUE_WHITE)
    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(on_draw, 1 / 80)


    arcade.run()

main()