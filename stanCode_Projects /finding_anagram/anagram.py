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

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
all_words = []


def main():
    """
    This program can helps us find all the anagram words from a word.
    """
    print(f'Welcome to StanCode "Anagram Generator" (or -1 to quit)')

    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break

        start = time.time()

        read_dictionary()
        ans_lst = []
        find_anagrams(word, ans_lst)
        print(f'{len(ans_lst)} anagrams: {ans_lst}')

        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    This function stores all the vocabulary in an English dictionary in a Python list.
    """
    with open(FILE, 'r') as f:
        for line in f:
            all_words.append(line.strip())
            

def find_anagrams(word, ans_lst):
    """
    :param word: str, the word inputted by the user.
    :param ans_lst: list, a list to store all anagrams answers.
    """
    print('Searching...')
    find_anagrams_helper(word, ans_lst, '', [])


def find_anagrams_helper(word, ans_lst, current_str, used_index):
    """
    :param word: str, the word inputted by the user.
    :param ans_lst: list, a list to store all anagrams answers.
    :param current_str: str, the current status of word being explored.
    :param used_index: list, used to distinguish whether the character is choosed or not.
    """
    # Base case
    if len(current_str) == len(word):
        if current_str in all_words and current_str not in ans_lst:
            ans_lst.append(current_str)
            print('Found: ' + current_str)
            print('Searching...')

    # Recursive case
    else:
        for i in range(len(word)):  
            if i not in used_index:
                # Choose
                # current_str += word[i]
                used_index.append(i)

                # Explore
                if has_prefix(current_str):
                    find_anagrams_helper(word, ans_lst, current_str + word[i], used_index)

                # Unchoose
                # current_str = current_str[:-1]
                used_index.pop()


def has_prefix(sub_s):
    """
    :param sub_s: str
    :return: boolean, whether there is a word that starts with sub_s, or not.
    """
    for word in all_words:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
