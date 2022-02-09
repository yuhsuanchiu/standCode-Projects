import tkinter as tk
import anagramgui as gui

FILE = 'dictionary.txt'
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 450


def main():
    word_d = read_dic()
    ans_lst = []

    top = tk.Tk()
    top.wm_title('Anagram Generator')
    top.configure(bg='Azure')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, word_d, ans_lst)

    top.mainloop()


def read_dic():
    word_d = {}
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            word_d[word] = word
    return word_d


if __name__ == '__main__':
    main()