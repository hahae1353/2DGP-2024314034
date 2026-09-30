from pico2d import *

open_canvas(800, 600)
character = load_image('character_sheet.png')
clear_canvas()
character.clip_draw(190, 634, 47, 94, 400, 300, 100, 200)
update_canvas()
delay(2)
close_canvas()
