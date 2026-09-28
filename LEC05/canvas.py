from pico2d import *
import os


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    open_canvas(800, 600)

    grass = load_image('grass.png')
    character = load_image('character.png')

    grass.draw(400, 30)
    character.draw(400, 300)
    character.draw(300, 200)
    character.draw(500, 400)

    update_canvas()
    delay(5)
    close_canvas()


if __name__ == "__main__":
    main()