from PyQt6.QtWidgets import QApplication
from snakeModel import SnakeModel
from snakeView import SnakeView
from snakeController import SnakeController
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = SnakeModel(grid_size = 30)
    view = SnakeView(model)
    controller = SnakeController(model, view)

    view.show()

    sys.exit(app.exec())