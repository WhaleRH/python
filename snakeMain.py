import sys
from PyQt6.QtWidgets import QApplication
from snakeController import SnakeGameController

def main():
    """Main function to run the Snake game."""
    app = QApplication(sys.argv)  # Create a Qt application
    game = SnakeGameController()  # Initialize the game controller
    game.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main() 