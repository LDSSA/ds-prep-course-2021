import unittest
from constants import VELOCITY_NORM
from snake import SnakeGame


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = SnakeGame()

    def test_movement(self):
        self.assertEqual(
            self.snake.velocity,
            (VELOCITY_NORM, 0),
            f"I Should be moving right! My velocity is {self.snake.velocity} but it should be {(VELOCITY_NORM, 0)}"
        )

        # Snake is moving right and should start moving down
        self.snake.move_down()
        self.assertEqual(
            self.snake.velocity,
            (0, VELOCITY_NORM),
            f"""
            I Should be moving down! I was moving right and the down button was hitted.
            My velocity is {self.snake.velocity} but it should be {(0, VELOCITY_NORM)}
            """
        )

        # Snake is moving down and should start moving left
        self.snake.move_left()
        self.assertEqual(
            self.snake.velocity,
            (-VELOCITY_NORM, 0),
            f"""
            I Should be moving left! I was moving down and the left button was hitted.
            My velocity is {self.snake.velocity} but it should be {(-VELOCITY_NORM, 0)}
            """
        )

        # Snake is moving left and it should keep moving left
        self.snake.move_right()
        self.assertEqual(
            self.snake.velocity,
            (-VELOCITY_NORM, 0),
            f"""
            I Should be moving left! I was moving left and the right button was hitted.
            Moving right is not allowed when you are moving left.
            My velocity is {self.snake.velocity} but it should be {(-VELOCITY_NORM, 0)}
            """
        )

        # Snake is moving left and it should start moving up
        self.snake.move_up()
        self.assertEqual(
            self.snake.velocity,
            (0, -VELOCITY_NORM),
            f"""
            I Should be moving up! I was moving left and the up button was hitted.
            My velocity is {self.snake.velocity} but it should be {(0, -VELOCITY_NORM)}
            """
        )

        # Snake is moving up and it should keep moving up
        self.snake.move_down()
        self.assertEqual(
            self.snake.velocity,
            (0, -VELOCITY_NORM),
            f"""
            I Should be moving up! I was moving up and the down button was hitted.
            Moving down is not allowed when you are moving up.
            My velocity is {self.snake.velocity} but it should be {(0, -VELOCITY_NORM)}
            """
        )

    def test_hit_apple(self):
        self.snake.apple_position = (100, 100)
        self.assertTrue(
            type(self.snake._hit_apple((100, 100))) == bool,
            "The method _hit_apple should return a boolean"
        )
        self.assertTrue(
            self.snake._hit_apple((100, 100)),
            "Snake have hit the apple. The new head position is (100, 100) and the apple position is (100, 100)"
        )
        self.assertFalse(
            self.snake._hit_apple((200, 200)),
            "Snake haven't hit the apple. The new head position is (100, 100) and the apple position is (200, 200)"
        )

    def test_hit_itself(self):
        self.assertTrue(
            type(self.snake._hit_itself((260, 260))) == bool,
            "The method hit_itself should return a boolean"
        )
        self.assertTrue(
            self.snake._hit_itself((260, 260)),
            "Snake have hit it self, but the method is returning False"
        )
        self.assertFalse(
            self.snake._hit_itself((500, 500)),
            "Snake haven't hit it self, but the method is returning True"
        )