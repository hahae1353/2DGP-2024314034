# 원운동 + 사각운동 단계
from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')

x, y = 400, 300
angle = 0.0
circle_center_x, circle_center_y = 400, 300
circle_radius = 120

rect_progress = 0.0
square_start_x, square_start_y = 300, 200
square_size = 200

state = 0


def move_circle():
    global x, y, angle, state
    x = circle_center_x + circle_radius * math.cos(angle)
    y = circle_center_y + circle_radius * math.sin(angle)
    angle += 0.08
    if angle >= 2 * math.pi:
        angle = 0.0
        state = 1
        x, y = 300, 200


def move_square():
    global x, y, rect_progress, state
    if rect_progress < 200:
        x += 5
    elif rect_progress < 400:
        y += 5
    elif rect_progress < 600:
        x -= 5
    elif rect_progress < 800:
        y -= 5
    else:
        rect_progress = 0.0
        state = 0
        x, y = 400, 300
        return

    rect_progress += 3


while True:
    clear_canvas()
    if state == 0:
        move_circle()
    elif state == 1:
        move_square()

    character.draw(x, y)
    update_canvas()
    delay(0.02)

close_canvas()
