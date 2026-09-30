from pico2d import *

open_canvas(800, 600)
character = load_image('character_sheet.png')
clear_canvas()
character.clip_draw(0, 0, 100, 100, 400, 400)
update_canvas()
delay(2)
close_canvas()
