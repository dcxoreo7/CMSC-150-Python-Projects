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

def main():
    """
    This is a house with two windows and a door
    """
    arcade.open_window("Function", 800,600)
    arcade.set_background_color(arcade.color.ANTIQUE_WHITE)
    arcade.start_render()

    draw_house_framework(0,0)
    draw_door(140,25)
    draw_window(185,185)
    draw_window(-135,185)

    arcade.finish_render()
    arcade.run()

main()
