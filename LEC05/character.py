from pico2d import *

open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')

game_is_running = True
cx, cy = 400, 300
r = 200
angle = 0.0
speed = 0.05
x, y = cx, cy

def update_game_logic():
    global angle, x, y

    angle += speed

    x = cx + r * math.cos(angle)
    y = cy + r * math.sin(angle)

    if angle >= 2 * math.pi:
        angle -= 2 * math.pi

def render_game_state():
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()

while game_is_running:
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_is_running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_is_running = False

    update_game_logic()
    render_game_state()

    delay(0.02)

close_canvas()

