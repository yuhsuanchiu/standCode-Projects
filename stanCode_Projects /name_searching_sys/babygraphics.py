"""
File: babygraphics.py
Name: Yu Hsuan Chiu
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    inner_width = width - 2 * GRAPH_MARGIN_SIZE
    x_coordinate = GRAPH_MARGIN_SIZE + int(inner_width // len(YEARS) * year_index)

    return x_coordinate


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the rank of the current year
    returns the y coordinate where the rank should be drawn.

    Input:
        height (int): The height of the canvas
        rank (str): The rank number
    Returns:
        y_coordinate (int): The y coordinate of the rank.
    """
    inner_height = height - 2 * GRAPH_MARGIN_SIZE
    y_coordinate = 0

    if rank != '**':
        y_coordinate = GRAPH_MARGIN_SIZE + int(rank) * inner_height // MAX_RANK
    else:
        y_coordinate = GRAPH_MARGIN_SIZE + inner_height

    return y_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Draw two horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    
    # Draw vertical line and the year label
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    for i in range(len(lookup_names)):
        
        name = lookup_names[i]
        color = COLORS[i % len(COLORS)]        
        ranks = []
        
        for j in range(len(YEARS)):         # create the rank list for every year
            year = str(YEARS[j])
            if year in name_data[name]:
                ranks.append(name_data[name][year])
            else:
                ranks.append('**')

        # Draw trend line year by year
        x1 = get_x_coordinate(CANVAS_WIDTH, 0)
        y1 = get_y_coordinate(CANVAS_HEIGHT, ranks[0])
        for j in range(len(YEARS) - 1):
            x2 = get_x_coordinate(CANVAS_WIDTH, j + 1)
            y2 = get_y_coordinate(CANVAS_HEIGHT, ranks[j + 1])
            canvas.create_line(x1, y1, x2, y2, fill=color, width=LINE_WIDTH)
            canvas.create_text(x1 + TEXT_DX, y1, fill=color,
                               anchor=tkinter.SW, text=f'{name} {ranks[j]}')
            x1, y1 = x2, y2
        canvas.create_text(x2 + TEXT_DX, y2, fill=color,
                           anchor=tkinter.SW, text=f'{lookup_names[i]} {ranks[-1]}')


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
