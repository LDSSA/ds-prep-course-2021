"""
    YOU ARE NOT SUPPOSED TO DO CHANGES TO THIS FILE.
    DO THE CHANGES AT YOUR OWN RISK. IT WOULD BE HARD TO THE INSTRUCTORS
    TO PROVIDE SUPPORT ON THE CONTENT OF THIS FILE
"""
import os
from typing import Tuple
import pygame

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    WHITE,
    GREEN,
    RED,
    SQUARE_SIZE,
    BLACK
)

from snake import SnakeGame

def get_event() -> pygame.event:
    return pygame.event.poll()

def set_up_screen(width: int = SCREEN_WIDTH, height: int = SCREEN_HEIGHT) -> pygame.Surface:
    """
    This function is responsable by initiate the screen.
    It creates the window and setup the background.
    :param width: windown width
    :param height: window height
    """
    pygame.init()
    pygame.display.set_caption('Snake')
    pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    screen.fill(WHITE)
    pygame.display.flip()
    return screen

def draw_snake_game(screen: pygame.Surface, snake: SnakeGame) -> None:
    """
    It draws the game on the screen.
    :param screen: The screen where the game will appear
    :param snake: The snake game object
    """
    screen.fill(WHITE)
    for pos in snake.snake_positions:
        pygame.draw.rect(
            screen,
            GREEN,
            pygame.Rect(pos, (SQUARE_SIZE, SQUARE_SIZE))
        )
    pygame.draw.rect(
            screen,
            RED,
            pygame.Rect(
                snake.apple_position,
                (SQUARE_SIZE, SQUARE_SIZE)
            )
    )
    pygame.display.flip()

def show_message(screen: pygame.Surface, message: str) -> None:
    """
    It shows the specified message on the screen.
    :param screen: Pygame.Surface where the message will appear
    :param message: String message to show on the screen.
    """
    # Prepare the Text
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, BLACK, WHITE)
    text_rect = text.get_rect()
    # Center the text on the screen
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    # Show the text
    screen.blit(text, [text_x, text_y])
    pygame.display.flip()