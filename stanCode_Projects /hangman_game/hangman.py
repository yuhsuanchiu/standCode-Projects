"""
File: hangman.py
Name: Yu Hsuan Chiu
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

N_TURNS = 7     # Controls how many chances the user have to guess


def main():
    """
    This program will randomly come up with a vocabulary,
    and the user can pick either one of the 26 alphabets for a guess.
    If the alphabet you pick is in the vocabulary, this program will 
    show you the relative position(s) of the alphabet. If not, 
    you lose one guess.(You have N_TURNS guesses.)
    The game ends either you guess all the alphabets right(win) or used up all 7 guesses(lose.)
    """
    ans = random_word()     # Get a random answer
    n_turns = N_TURNS       # The chances left for the player to guess

    dashed_ans = ''         # Cover the answer with dashes('-')
    for i in range(len(ans)):
        dashed_ans += '-'

    while True:    
        print('The word looks like: ' + dashed_ans)
        print('You have ' + str(n_turns) + ' guesses left.')
        guess = input('Your guess: ').upper()

        if not guess.isalpha() or len(guess) != 1:  # Check if correct format
            print('Illegal format.')
        else:
            guess_right = False     # To see if the guess is right
            new_dashed_ans = ''     # Used to update the dashed_ans
            for i in range(len(dashed_ans)):
                if ans[i] == guess:
                    new_dashed_ans += guess
                    guess_right = True
                else:
                    new_dashed_ans += dashed_ans[i]

            dashed_ans = new_dashed_ans     # Update dashed_ans

            # Update n_turns
            if not guess_right:
                n_turns -= 1
                print('There is no ' + guess + '\'s in the world.')
            else:
                print('Your are correct!')

            # Check if to end the game
            if n_turns == 0:
                print('You are completely hung :(')
                break
            if '-' not in dashed_ans:
                print('You win!!')
                break
    print('The answer is: ' + ans)


def random_word():
    """
    To pick a random answer.
    return: str, the answer picked.
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# --- DO NOT EDIT CODE BELOW THIS LINE --- #
if __name__ == '__main__':
    main()
