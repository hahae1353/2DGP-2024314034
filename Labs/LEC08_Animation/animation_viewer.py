from pico2d import *

open_canvas(800, 600)
character = load_image('character_sheet.png')
walking_frames = [173, 294, 413, 539, 665, 789, 909, 1035]
running_frames = [165, 288, 417, 543, 660, 791, 906, 1028]
speed_boost_running_frames = [165, 281, 401, 525, 649, 778, 905, 1020]
stop_running_frames = []
jump_frames = []

while True:
	for frame_lefts, bottom, width, height in (
		(walking_frames, 634, 80, 94),
		(running_frames, 485, 80, 96),
		(speed_boost_running_frames, 346, 80, 88),
		(stop_running_frames, 210, 80, 94),
		(jump_frames, 72, 80, 122),
	):
		for frame_left in frame_lefts:
			clear_canvas()
			character.clip_draw(
				frame_left, bottom, width, height,
				400, 300, width * 2, height * 2,
			)
			update_canvas()
			delay(0.1)

close_canvas()
