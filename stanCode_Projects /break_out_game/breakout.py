"""
File: breakout.py
Name: Yu Hsuan Chiu
-------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():

    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add animation loop here!
    while True:

        if graphics.started:
            if lives > 0 and graphics.bricks_left > 0:

                graphics.ball.move(graphics.get_dx(), graphics.get_dy())
                
                # Hits the side walls and bounces
                if graphics.ball.x < 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                    graphics.change_x_direction()

                # Hits the ceiling and bounces
                if graphics.ball.y < 0:
                    graphics.change_y_direction()

                # Detects if the ball hits something and do corresponding responses
                graphics.detect_corner_hits()

                # Lose one life
                if graphics.ball.y + graphics.ball.height > graphics.window.height:
                    graphics.reset()
                    lives -= 1                

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
