"""
File: boggle.py
Name: Yu Hsuan Chiu
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	word_d = {}
	read_dictionary(word_d)
	input_title = ['4 row of letters: ', '3 row of letters: ', '2 row of letters: ', '1 row of letters: ']
	letters_list = []
	print('Welcome to stanCode boggle game! Please enter 4 rows of letters, each letter shall be separated by blank space.')
	start = time.time()
	while True:
		if len(input_title) > 0:
			string = input(input_title[-1])
			if input_check(string):
				print('Illegal input')
				string = ''
			else:
				ch_list = string.split()
				# Case insensitive
				for i in range(len(ch_list)):
					ch_list[i] = ch_list[i].lower()
				letters_list.append(ch_list)
				input_title.pop()
		else:
			break
	ans_list = []
	find_words(letters_list, word_d, ans_list)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def input_check(string):
	ch_list = string.split()
	if len(ch_list) != 4:
		return True
	for ele in ch_list:
		if len(ele) != 1 and not ele.isalpha():
			return True


def find_words(letter_list, word_d, ans_list):
	# choose the start point of all the chs
	for i in range(len(letter_list)):
		for j in range(len(letter_list[i])):
			x = i
			y = j
			find_words_helper(x, y, letter_list, word_d, ans_list, letter_list[x][y], [])


def find_words_helper(x, y, letter_list, word_d, ans_list, cur_str, index_list):
	# Base case
	if len(cur_str) >= len(letter_list):
		if cur_str in word_d and cur_str not in ans_list:
			ans_list.append(cur_str)
			print('Found: ' + cur_str)
			# Check the neighbors of the last ch are all checked, in case if there's longer word
			for i in range(-1, 2):
				for j in range(-1, 2):
					new_x = x + i
					new_y = y + j
					# prevent the coordinate x or y is out of the range
					if new_x < 0 or new_y < 0:
						pass
					elif new_x > len(letter_list) - 1 or new_y > len(letter_list[0]) - 1:
						pass
					elif (new_x, new_y) not in index_list:
						# Choose
						cur_str += letter_list[new_x][new_y]
						index_list.append((new_x, new_y))
						# Explore
						find_words_helper(new_x, new_y, letter_list, word_d, ans_list, cur_str, index_list)
						# Un-choose
						index_list.pop()
						cur_str = cur_str[:-1]
	# Recursive case
	else:
		# Find the neighbors
		for i in range(-1, 2):
			for j in range(-1, 2):
				if i == 0 and j == 0:
					if (x, y) not in index_list:
						index_list.append((x, y))
				else:
					new_x = x + i
					new_y = y + j
					# prevent the coordinate x or y is out of the range
					if new_x < 0 or new_y < 0:
						pass
					elif new_x > len(letter_list)-1 or new_y > len(letter_list[0])-1:
						pass
					elif (new_x, new_y) not in index_list:
						# Choose
						cur_str += letter_list[new_x][new_y]
						index_list.append((new_x, new_y))
						# Explore
						find_words_helper(new_x, new_y, letter_list, word_d, ans_list, cur_str, index_list)
						# Un-choose
						index_list.pop()
						cur_str = cur_str[:-1]


def read_dictionary(word_dict):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r')as f:
		for line in f:
			word = line.strip()
			word_dict[word] = word


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	pass


if __name__ == '__main__':
	main()
