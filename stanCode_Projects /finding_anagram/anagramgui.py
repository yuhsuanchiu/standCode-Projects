import tkinter as tk
TEXT_DX = 15


def make_gui(window, width, height, word_d, ans_lst):

    title = tk.Label(window, text='Welcome to stanCode Anagram Generator!', font=('Impact', 35),
                     bg='Azure', fg='darkslategrey')
    title.grid(row=0, columnspan=2)
    # searching entry field
    entry_hint = tk.Label(window, text='Find Anagram:', font=('Arial', 20), bg='Azure')
    entry_hint.grid(row=1, column=0)
    entry = tk.Entry(window, width=45, name='entry', borderwidth=2)
    entry.grid(row=1, column=1, sticky='w')
    entry.focus()

    result = tk.Label(window, text='Here comes the answers', font=('Impact', 20),
                      bg='Azure', fg='darkslategrey')
    result.grid(row=2, columnspan=2)
    # canvas for showing the answers
    canvas = tk.Canvas(window, width=width-350, height=height-200, name='canvas', highlightbackground='darkslategrey')
    canvas.grid(row=3, columnspan=2)

    space = tk.LabelFrame(window, width=10, height=20, borderwidth=0, bg='Azure')
    space.grid(row=4, columnspan=2, sticky='w')

    # When <return> key is hit in a text field, connect to the anagram searching
    entry.bind('<Return>', lambda event: finding_anagram(entry, canvas, word_d))

    window.update()
    return canvas


def finding_anagram(entry, canvas, word_d):
    canvas.delete('all')
    text = entry.get().strip().lower()
    ans_lst = []
    finding_anagram_helper(text, canvas, word_d, ans_lst, len(text), '', [])


def finding_anagram_helper(word, canvas, word_d, ans_list, ans_len, anagram, used_index):
    if len(anagram) == ans_len:
        if anagram in word_d and anagram not in ans_list:
            ans_list.append(anagram)
            canvas.create_text(5, 5+TEXT_DX*(len(ans_list)-1), text=anagram, anchor=tk.NW)

    else:
        for i in range(len(word)):
            if i not in used_index:
                anagram += word[i]
                used_index.append(i)

                finding_anagram_helper(word, canvas, word_d, ans_list, ans_len, anagram, used_index)

                used_index.pop()
                anagram = anagram[:-1]






