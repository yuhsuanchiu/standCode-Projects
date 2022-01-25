"""
File: breakoutgraphics.py
Name: Yu Hsuan Chiu
-------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 30     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.x = (window_width - paddle_width) // 2
        self.paddle.y = window_height - paddle_offset - paddle_height
        self.paddle.filled = True
        self.window.add(self.paddle)
        
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball_initial_x = window_width // 2 - ball_radius
        self.ball_initial_y = window_height // 2 - ball_radius
        self.ball.x = self.ball_initial_x
        self.ball.y = self.ball_initial_y
        self.ball.filled = True
        self.window.add(self.ball)
        
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.start)

        # Initialize variables
        self.started = False
        self.bricks_left = brick_rows * brick_cols

        # Draw bricks
        for i in range(0, brick_rows):

            # Assign the color to the brick according to its "row" position
            color = ''
            if i // 2 == 0:
                color = 'red'
            elif i // 2 == 1:
                color = 'orange'
            elif i // 2 == 2:
                color = 'yellow'
            elif i // 2 == 3:
                color = 'green'
            elif i // 2 == 4:
                color = 'blue'

            for j in range(0, brick_cols):
                brick = GRect(brick_width, brick_height)    # We don't have to put the "brick" on "self",
                brick.filled = True                         # because a "single variable" can only store
                brick.fill_color = color                    # a "single object"
                brick.x = j * (brick_width + brick_spacing)
                brick.y = i * (brick_height + brick_spacing) + brick_offset
                self.window.add(brick)

    def paddle_move(self, event):
        """
        This function has the paddle move with its center following the mouse.
        :param event: MouseEvent, stores the position information where the mouse event happens.
        """
        if self.paddle.width / 2 < event.x < self.window.width - self.paddle.width / 2:
            self.paddle.x = event.x - self.paddle.width // 2

        elif event.x < self.paddle.width / 2:  # To prevent the paddle from out-boarding the left side
            self.paddle.x = 0
        else:                                  # To prevent the paddle from out-boarding the right side
            self.paddle.x = self.window.width - self.paddle.width

    def start(self, event):
        """
        This function starts the game.
        :param event: MouseEvent, stores the position information where the mouse event happens.
        """
        if not self.started:
            self.started = True

            # Set a random speed when a new attempt begins
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def detect_corner_hits(self):
        """
        Defines what the ball does when it hits objects(or not.)
        return: None
        """
        for corner_x in range(self.ball.x, self.ball.x + self.ball.width + 1, self.ball.width):
            for corner_y in range(self.ball.y, self.ball.y + self.ball.height + 1, self.ball.height):
                
                object_detected = self.window.get_object_at(corner_x, corner_y)

                if object_detected:
                    # Hits the bricks
                    if object_detected is not self.paddle:
                        self.window.remove(object_detected)
                        self.bricks_left -= 1
                        self.__dy *= -1

                        # This "return" allows us to leave this method's stack frame directly, so
                        # we can break both for loops, preventing the detection of following corners.
                        return

                    # Hits the paddle
                    elif object_detected is self.paddle:
                        if self.__dy > 0:
                            self.__dy *= -1
                        return

    def reset(self):
        """
        This function resets the ball to its original status.
        """
        self.started = False
        self.ball.x = self.ball_initial_x
        self.ball.y = self.ball_initial_y

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def change_x_direction(self):
        self.__dx *= -1

    def change_y_direction(self):
        self.__dy *= -1
