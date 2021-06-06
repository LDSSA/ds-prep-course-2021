from random import randint
from typing import Tuple

from constants import (
    SQUARE_SIZE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    VELOCITY_NORM
)


class SnakeGame:
    def __init__(self, initial_length=10):
        """
        :param initial_length: Snake initial length, defaults to 10
        """
        self.game_running = True

        self.snake_positions = [
            (260 - i*SQUARE_SIZE, 260) for i in range(initial_length)
        ]
        self.velocity = (VELOCITY_NORM, 0)  # Start moving right

        self.apple_position = (100, 100)

        self._generate_new_apple()

    def is_running(self) -> bool:
        """
        This method allow us to check if the game stills running.
        :return: True if the game stills running.
        """
        return self.game_running

    def _compute_new_head_position(self) -> Tuple[int, int]:
        """
        Compute the head position. The actual head position is the first element at the
        self.snake_positions list. The new head position will be the actual head position plus
        self.velocity
        :return: New head position
        """
        return (
            self.snake_positions[0][0] + self.velocity[0],
            self.snake_positions[0][1] + self.velocity[1]
        )

    def tick(self) -> None:
        """
        Game main loop.
        """
        new_head_pos = self._compute_new_head_position()
        if self._hit_itself(new_head_pos):
            self.stop_game()
        else:
            self.snake_positions.insert(0, new_head_pos)
            if self._hit_apple(new_head_pos):
                self._generate_new_apple()
            else:
                del self.snake_positions[-1]
            self._hit_wall()

    def _generate_new_apple(self) -> None:
        """
        Method that allow us to generate a new position to the apple.
        It will appear at a random position.
        """
        self.apple_position = (
            randint(3, (SCREEN_WIDTH - 3 * SQUARE_SIZE) /
                    SQUARE_SIZE) * SQUARE_SIZE,
            randint(3, (SCREEN_HEIGHT - 3 * SQUARE_SIZE) /
                    SQUARE_SIZE) * SQUARE_SIZE
        )
        print(f'New apple generate at {self.apple_position}')
        # check if the generated apple is on the top of snake
        if self.apple_position in self.snake_positions:
            self.generate_new_apple()

    def _hit_apple(self, new_head_pos: Tuple[int, int]) -> bool:
        """
        It checks if snake have ate the apple.
        :param new_head_pos: Next snake head position
        :return: True if the new head position is equal to the apple position
        """
        return new_head_pos == self.apple_position

    def _hit_wall(self) -> None:
        """
        If snake is outside of the screen limit, we move it to the opposite direction.
        """
        head_pos = self.snake_positions[0]
        if head_pos[0] < 0:
            self.snake_positions[0] = (SCREEN_WIDTH, head_pos[1])
        elif head_pos[0] >= SCREEN_WIDTH:
            self.snake_positions[0] = (0, head_pos[1])
        elif head_pos[1] < 0:
            self.snake_positions[0] = (head_pos[0], SCREEN_HEIGHT)
        elif head_pos[1] >= SCREEN_HEIGHT:
            self.snake_positions[0] = (head_pos[0], 0)

    def _hit_itself(self, new_head_pos) -> bool:
        """
        It checks if snake have hit it self. It is true if the new head_position is equal to any of
        the positions in self.snake_positions
        :param new_head_pos: New snake head position.
        :return: True if snake have hit it self
        """
        return new_head_pos in self.snake_positions

    def move_right(self) -> None:
        """
        After this method is called, snake will start moving right with velocity equal to VELOCITY_NORM.
        If snake is moving left, it should keep moving left.
        Changing direction to right is not allowed when you are moving right.
        """
        if self.velocity == (-VELOCITY_NORM, 0):
            return
        self.velocity = (VELOCITY_NORM, 0)

    def move_left(self) -> None:
        """
        After this method is called, snake will start moving left.
        If snake is moving right, it should keep moving right.
        Changing direction to left is not allowed when you are moving right
        The velocity norm is always the constant value VELOCITY_NORM
        """
        if self.velocity == (VELOCITY_NORM, 0):
            return
        self.velocity = (-VELOCITY_NORM, 0)

    def move_down(self) -> None:
        """
        After this method is called, snake will start moving down.
        If snake is moving up, it should keep moving up.
        Changing direction to down is not allowed when you are moving up.
        The velocity norm is always the constant value VELOCITY_NORM.
        """
        if self.velocity == (0, -VELOCITY_NORM):
            return
        self.velocity = (0, VELOCITY_NORM)

    def move_up(self) -> None:
        """
        After this method is called, snake will start moving up.
        If snake is moving down, it should keep moving down.
        Changing direction to up is not allowed when you are moving down.
        The velocity norm is always the constant value VELOCITY_NORM
        """
        if self.velocity == (0, VELOCITY_NORM):
            return
        self.velocity = (0, -VELOCITY_NORM)

    def stop_game(self) -> None:
        print('Game ended')
        self.game_running = False
