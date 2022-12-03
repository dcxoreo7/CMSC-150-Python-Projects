import arcade
arcade.open_window("Drawing",800,600)

# Negative background color half
arcade.set_background_color(arcade.color.COOL_BLACK)

arcade.start_render()

#Positive background color half
arcade.draw_lrtb_rectangle_filled(0,400,650,0, arcade.color.GHOST_WHITE)

##Positive/Negative Face

#face
arcade.draw_rectangle_filled(250,400,300,500,arcade.color.GOLDEN_BROWN)

#negative face
arcade.draw_rectangle_filled(550,400,300,500,arcade.color.APPLE_GREEN)


#eye
arcade.draw_circle_filled(280,450,100,arcade.color.FLORAL_WHITE)

#negative eye
arcade.draw_circle_filled(525,450,100,arcade.color.BLACK_BEAN)

#eye pupil
arcade.draw_circle_filled(280,450,50, arcade.color.BLACK_BEAN)

#negative eye pupil
arcade.draw_circle_filled(525,450,50, arcade.color.CARMINE_RED)

#eyebrow
arcade.draw_rectangle_filled(285,590,200,75, arcade.color.BLACK_BEAN)

#negative eyebrow
arcade.draw_rectangle_filled(520,590,200,75, arcade.color.DARK_LAVA)

#nose
arcade.draw_triangle_filled(325,300,400,300,400,400, arcade.color.BROWN_NOSE)

#negative nose
arcade.draw_triangle_filled(475,300,400,300,400,400, arcade.color.DARK_CANDY_APPLE_RED)

#mouth
arcade.draw_line(275,250,550,250,arcade.color.BLACK_BEAN,400)

#teeth
arcade.draw_rectangle_filled(345,229,110,35,arcade.color.WHITE_SMOKE)

#negative teeth
arcade.draw_rectangle_filled(462,228.8,123,35,arcade.color.FIRE_ENGINE_RED)



arcade.finish_render()
arcade.run()