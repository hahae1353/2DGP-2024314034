# 실습 과제 진행

from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')

x, y = 400, 300
state = 0
angle = 0.0
progress = 0.0

def move_circle():
    print("CIRCLE")
    global x, y, angle, state
    cx, cy = 400, 300
    radius = 100

    x = cx + radius * math.cos(angle)
    y = cy + radius * math.sin(angle)

    angle += 0.5
    if angle >= 2 * math.pi:
        angle = 0.0
        state = 1

def move_rectangle():
    print("RECTANGLE")
    global x, y, progress, state
    if progress < 100:
        x += 2
    elif progress < 200:
        y += 2
    elif progress < 300:
        x -= 2
    elif progress < 400:
        y -= 2
    else:
        progress = 0.0
        state = 2
        return
    progress += 2

def move_triangle():
    print("TRIANGLE")
    global x, y, progress, state
    if progress < 100:
        x += 2
        y += 2
    elif progress < 200:
        x -= 4
    elif progress < 300:
        y -= 2
    else:
        progress = 0.0
        state = 0
        return
    progress += 2

while True:
    clear_canvas()
    if state == 0:
        move_circle()
    elif state == 1:
        move_rectangle()
    elif state == 2:
        move_triangle()

    character.draw(x, y)
    update_canvas()

    delay(0.02)

close_canvas()


