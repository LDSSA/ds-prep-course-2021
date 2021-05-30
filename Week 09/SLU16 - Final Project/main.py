import time

import pygame
from pygame import K_RIGHT, K_LEFT, K_DOWN, K_UP

from pygame_utils import (
    set_up_screen,
    get_event,
    draw_snake_game,
    show_message
)
from snake import SnakeGame


def main():
    screen = set_up_screen()
    snake = SnakeGame()
    while True:
        event = get_event()
        if event.type == pygame.QUIT:
            break
        keys = pygame.key.get_pressed()
        if snake.is_running():
            if (keys[K_RIGHT]):  # Check if K_RIGHT was Pressed
                snake.move_right()

            if (keys[K_LEFT]):  # Check if K_LEFT was Pressed
                snake.move_left()

            if (keys[K_UP]):  # Check if K_UP was Pressed
                snake.move_up()

            if (keys[K_DOWN]):  # Check if K_DOWS was Pressed
                snake.move_down()
            time.sleep(100.0 / 1000.0)
            snake.tick()
            draw_snake_game(screen, snake)
        else:
            show_message(screen, 'You lost')


if __name__ == '__main__':
    main()
