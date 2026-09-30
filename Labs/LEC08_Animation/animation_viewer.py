from pico2d import *

open_canvas(800, 600)
character = load_image('character_sheet.png')
frame_lefts = [181, 302, 421, 547, 673, 797, 917, 1043]
frame = 0

while True:
	clear_canvas()
	character.clip_draw(frame_lefts[frame], 634, 64, 94, 400, 300, 128, 188)
	update_canvas()
	frame = (frame + 1) % len(frame_lefts)
	delay(0.1)

close_canvas()
