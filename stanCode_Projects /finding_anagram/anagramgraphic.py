"""
File: anagram.py
Name: Yu Hsuan Chiu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19
If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import tkinter as tk
import anagramgui as gui

FILE = 'dictionary.txt'
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 450


def main():
    word_d = read_dic()

    top = tk.Tk()
    top.wm_title('Anagram Generator')
    top.configure(bg='Azure')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, word_d)

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
