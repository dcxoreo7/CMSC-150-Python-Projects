import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

RECT_WIDTH = 100
RECT_HEIGHT = 100

def on_draw(delta_time):

    arcade.start_render()

    arcade.draw_rectangle_filled(on_draw.center_x, on_draw.center_y, RECT_WIDTH, RECT_HEIGHT,arcade.color.ALIZARIN_CRIMSON)

    on_draw.center_x += on_draw.delta_x * delta_time
    on_draw.center_y += on_draw.delta_y * delta_time

    if on_draw.center_x < RECT_WIDTH // 2 \
            or on_draw.center_x > SCREEN_WIDTH - RECT_WIDTH // 2:
        on_draw.delta_x *= -1
    if on_draw.center_y < RECT_HEIGHT // 2 \
            or on_draw.center_y > SCREEN_HEIGHT - RECT_HEIGHT // 2:
        on_draw.delta_y *= -1

on_draw.center_x = 100
on_draw.center_y = 50
on_draw.delta_x = 115
on_draw.delta_y = 130

arcade.open_window("Animation", SCREEN_WIDTH,SCREEN_HEIGHT)

arcade.schedule(on_draw, 1 / 80)

arcade.run()
