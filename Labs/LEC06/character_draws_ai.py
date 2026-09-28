# 원운동 단계
from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')

x, y = 400, 300
angle = 0.0
circle_center_x, circle_center_y = 400, 300
circle_radius = 120


def move_circle():
    global x, y, angle
    x = circle_center_x + circle_radius * math.cos(angle)
    y = circle_center_y + circle_radius * math.sin(angle)
    angle += 0.08


while True:
    clear_canvas()
    move_circle()
    character.draw(x, y)
    update_canvas()
    delay(0.02)

close_canvas()
