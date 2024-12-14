from enum import Enum
import random

class Direction(Enum):
    """Represents the possible directions the snake can move."""
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

# Define the offsets for each direction
direction_offsets = {
    Direction.UP: (0, -1),
    Direction.DOWN: (0, 1),
    Direction.LEFT: (-1, 0),
    Direction.RIGHT: (1, 0)
}

# Determine the opposite direction
opposite_directions = {
    Direction.UP: Direction.DOWN,
    Direction.DOWN: Direction.UP,
    Direction.LEFT: Direction.RIGHT,
    Direction.RIGHT: Direction.LEFT
}

def know_direction(og_x, og_y, move_x, move_y, current_dir):
    """
    Calculate the new direction to move from the source to the destination.
    """
    new_x = move_x - og_x
    new_y = move_y - og_y

    if abs(new_x) > abs(new_y):
        if new_x > 0 and current_dir != Direction.LEFT:
            return Direction.RIGHT
        elif new_x < 0 and current_dir != Direction.RIGHT:
            return Direction.LEFT
    else:
        if new_y > 0 and current_dir != Direction.UP:
            return Direction.DOWN
        elif new_y < 0 and current_dir != Direction.DOWN:
            return Direction.UP

    return current_dir


class Snake:
    """Class representing the snake and its behavior."""

    def __init__(self):
        self.food_position = None
        self.body_position = None
        self.ignore_body = True
        self.grid_size = 10  # Size of a single snake segment
        self.scores = 0  # Player's score
        self.frame_time = 75  # Time between game updates (Snake speed)
        self.height = 300  # Game area height
        self.width = 300  # Game area width
        self.init_body_position()  # Set initial position
        self.direction = Direction.RIGHT  # Initial movement direction
        self.spawn_food()  # Create initial food position

    def init_body_position(self):
        """Initialize snake body to start in the middle of the game area."""
        mid_x = self.width // 2
        mid_y = self.height // 2
        self.body_position = [
            (mid_x, mid_y),  # Head
            (mid_x - self.grid_size, mid_y),  # Body segment
            (mid_x - 2 * self.grid_size, mid_y)  # Tail segment
        ]

    def state_game(self):
        """Check for game-over conditions."""
        head_x, head_y = self.body_position[0]  # Snake's head position

        # Check if the snake collides with the walls
        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height:
            return True

        # Check if the snake collides with itself (excluding food)
        if not self.ignore_body and (head_x, head_y) in self.body_position[1:]:
            return True

        # No game-over condition
        return False

    def spawn_food(self):
        """Place new food in the game area, ensuring it is not on the snake."""
        while True:
            food_x = random.randint(0, (self.width // self.grid_size) - 1) * self.grid_size
            food_y = random.randint(0, (self.height // self.grid_size) - 1) * self.grid_size
            # Check if food position is not in the snake's body
            if (food_x, food_y) not in self.body_position:
                self.food_position = (food_x, food_y)
                break

    def grow_snake(self, position):
        """Add a new segment to the snake's body."""
        self.body_position.insert(0, position)

    def move(self):
        """Move snake forward and remove the last segment."""
        new_head = self.get_position(self.body_position[0], self.direction)
        self.body_position.insert(0, new_head)  # New head becomes first segment
        self.body_position.pop()  # Remove last segment

    def get_position(self, position, direction):
        """Get the next position of the snake's head given its current position and direction."""
        x, y = position
        offset_x, offset_y = direction_offsets[direction]
        return x + offset_x * self.grid_size, y + offset_y * self.grid_size

    def eat(self):
        """Check if food is eaten and grow the snake."""
        if self.is_food_eaten():
            self.grow_snake(self.body_position[0])  # Grow by adding a new segment at the head position
            self.update_score()
            self.spawn_food()

    def is_food_eaten(self):
        """Check if the snake's head is at the food position."""
        return self.food_position == self.body_position[0]

    def update_score(self):
        """Update the player's score."""
        self.scores = len(self.body_position) - 3  # Score based on body length minus the initial length
