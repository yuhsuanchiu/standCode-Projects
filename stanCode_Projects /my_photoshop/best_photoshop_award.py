"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage
BLACK_PIXEL = 80


def main():
    """
    NAME OF THE CREATION: STOP PRESSING CALL BELL PLZ!
    When I was the cabin crew, there was a passenger who kept pressing call bell non-stop on EK203.
    EK203 is from DXB to JFK and IT'S A 14 HOURS NIGHT FLIGHT!!
    There was no life n death issue, he was just bored n wanted to get attention.
    Every time when his call bell rang,we were all screaming in our head.
    In the end, the crews were saying that basically we WALKED to NEW YORK and WE SURVIVED!
    The Qatar's uniform is from my friend, we were doing the photo shot of changing uniform.
    I was actually cabin crew of Emirates Airline.
    """
    fg = SimpleImage('image_contest/IMG_0603.JPG')
    bg = SimpleImage('image_contest/IMG_0602.JPG')
    bg.make_as_big_as(fg)
    for x in range(fg.width):
        for y in range(fg.height):
            fg_p = fg.get_pixel(x, y)
            bg_p = bg.get_pixel(x, y)
            total = fg_p.red + fg_p.green + fg_p.blue
            if fg_p.red == fg_p.green or fg_p.red == fg_p.blue or fg_p.green == fg_p.blue:
                if total > BLACK_PIXEL:
                    fg_p.red = bg_p.red
                    fg_p.green = bg_p.green
                    fg_p.blue = bg_p.blue

    fg.show()




if __name__ == '__main__':
    main()
