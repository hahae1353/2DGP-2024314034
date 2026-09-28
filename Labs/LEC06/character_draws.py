# 실습 과제 진행

from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')

x, y = 400, 300
state = 0
angle = 0.0
rect_progress = 0.0
tri_step = 0
t = 0.0

def move_circle():
    print("CIRCLE")
    global x, y, angle, state
    cx, cy = 400, 300
    radius = 100

    x = cx + radius * math.cos(angle)
    y = cy + radius * math.sin(angle)

    angle += 0.1
    if angle >= 2 * math.pi:
        angle = 0.0
        global rect_progress
        rect_progress = 0.0
        x, y = 300, 200
        state = 1
        return

def move_rectangle():
    print("RECTANGLE")
    global x, y, rect_progress, state
    if rect_progress < 200:
        x += 10
    elif rect_progress < 400:
        y += 10
    elif rect_progress < 600:
        x -= 10
    elif rect_progress < 800:
        y -= 10
    else:
        rect_progress = 0.0
        global tri_step
        tri_step = 0
        x, y = 300, 400
        state = 2
        return
    
    rect_progress += 3

def move_triangle():
    print("TRIANGLE")
    global x, y, tri_step, t, state
    pA = (400, 420)
    pB = (280, 220)
    pC = (520, 220)

    speed = 0.03

    if tri_step == 0:
        x = pA[0] * (1 - t) + pB[0] * t
        y = pA[1] * (1 - t) + pB[1] * t
    elif tri_step == 1:
        x = pB[0] * (1 - t) + pC[0] * t
        y = pB[1] * (1 - t) + pC[1] * t
    elif tri_step == 2:
        x = pC[0] * (1 - t) + pA[0] * t
        y = pC[1] * (1 - t) + pA[1] * t

    t += speed
    if t >= 1.0:
        t = 0.0
        tri_step += 1
        if tri_step > 2:
            tri_step = 0
            state = 0

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


