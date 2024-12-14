from PyQt6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QLabel, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QBasicTimer, QTimer, Qt
import time
from snakeModel import Snake, Direction

class SnakeGameWindow(QMainWindow):
    """Main game window"""

    def __init__(self):
        super().__init__()

        # Initialize the game and UI elements
        self.snake = Snake()
        self.init_ui()
        self.timer = QBasicTimer()
        self.timer.start(self.snake.frame_time, self)

        # Initialize start time
        self.start_time = time.time()  # Initialize start_time
        self.fps_timer = QTimer()

        self.setWindowTitle('Snake Game')
        self.show()

    def init_ui(self):
        """Set up the UI elements for the game."""
        self.setMinimumSize(self.snake.width, self.snake.height)
        self.setStatusTip('Use arrow keys to control the snake. Press Space for auto-play mode.')

    def update_status_bar(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        elapsed_seconds = int(elapsed_time)
        minutes = elapsed_seconds // 60
        seconds = elapsed_seconds % 60
        total_time = f"Time: {minutes:02}:{seconds:02}"

        status = f"Score: {self.snake.scores} | {total_time}"
        self.statusBar().showMessage(status)

    def paintEvent(self, e):
        """Draw the game graphics."""
        painter = QPainter(self)
        self.draw_snake(painter)
        self.draw_food(painter)
        self.update_status_bar()

    def draw_snake(self, painter):
        """Draw the snake on the board with enhanced visual effects."""
        body_position = self.snake.body_position
        block_size = self.snake.grid_size

        # Drawing snake body with gradient color and transparency
        painter.setPen(Qt.PenStyle.NoPen)
        for index, (x, y) in enumerate(body_position):
            if index == 0:  # Snake head
                painter.setBrush(QColor(255, 0, 0))  # Red head
                painter.drawRect(x, y, block_size, block_size)
            else:
                painter.setBrush(QColor(0, 255, 0))
                painter.drawRect(x, y, block_size, block_size)

    def draw_food(self, painter):
        """Draw the food item."""
        food_position = self.snake.food_position
        block_size = self.snake.grid_size
        if food_position:
            painter.setBrush(QColor(0, 0, 255))  # Food is blue
            painter.drawEllipse(food_position[0], food_position[1], block_size, block_size)

    def timerEvent(self, event):
        """Handle timer events such as moving the snake or updating the game."""
        if self.snake.state_game():
            self.game_over()

    def keyPressEvent(self, event):
        """Handle key presses for controlling the snake."""
        if event.key() == Qt.Key.Key_Up:
            self.snake.direction = Direction.UP
        elif event.key() == Qt.Key.Key_Down:
            self.snake.direction = Direction.DOWN
        elif event.key() == Qt.Key.Key_Left:
            self.snake.direction = Direction.LEFT
        elif event.key() == Qt.Key.Key_Right:
            self.snake.direction = Direction.RIGHT

    def game_over(self):
        """Handle game over scenario with score and elapsed time."""
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        elapsed_seconds = int(elapsed_time)
        minutes = elapsed_seconds // 60
        seconds = elapsed_seconds % 60
        elapsed_time_str = f"{minutes:02}:{seconds:02}"

        # Create a custom QWidget to show the message
        msg_widget = QWidget()

        # Create a QVBoxLayout to layout the widgets inside the message box
        layout = QVBoxLayout()

        # Add the score and elapsed time as QLabel widgets
        score_label = QLabel(f"Game Over! Score: {self.snake.scores}")
        time_label = QLabel(f"{elapsed_time_str}")

        # Add the labels to the layout
        layout.addWidget(score_label)
        layout.addWidget(time_label)

        # Set the layout to the QWidget
        msg_widget.setLayout(layout)

        # Create a custom QMessageBox with the QWidget as content
        msg = QMessageBox(self)
        msg.setWindowTitle("Game Over")

        # Use setText to set the overall title, and set the custom widget content
        msg.setInformativeText(f"Game Over!\nScore: {self.snake.scores}\nElapsed Time: {elapsed_time_str}")

        msg.setStyleSheet("QLabel{font-size: 12pt; font-family: 'Comic Sans MS';}")

        # Adjust the message box size
        msg.setMinimumWidth(200)
        msg.setMinimumHeight(180)

        # Execute the message box
        msg.exec()

        self.snake.init_body_position()  # Reset the game
        self.snake.scores = 0
        self.start_time = time.time()
        self.update()
