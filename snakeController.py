from PyQt6.QtCore import Qt
from snakeView import SnakeGameWindow
from snakeModel import Direction


class SnakeGameController(SnakeGameWindow):
    """Controller that manages game events based on user input."""
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        """Takes user key inputs."""
        if event.key() == Qt.Key.Key_Up:
            self.snake.direction = Direction.UP
        elif event.key() == Qt.Key.Key_Down:
            self.snake.direction = Direction.DOWN
        elif event.key() == Qt.Key.Key_Left:
            self.snake.direction = Direction.LEFT
        elif event.key() == Qt.Key.Key_Right:
            self.snake.direction = Direction.RIGHT

    def timerEvent(self, event):
        """Takes timer events (moving the snake or updating the game.)"""
        if self.snake.judge_game():
            self.game_over()
            return

        self.snake.move()
        self.snake.eat()
        self.update()