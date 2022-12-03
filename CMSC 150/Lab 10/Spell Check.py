import re

line_number = 0

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

dictionary_file = open("dictionary.txt")

dictionary_list = []
for line in dictionary_file:
    line = line.strip()
    dictionary_list.append(line)

dictionary_file.close()

print("---Linear Search---")

story_file = open("AliceInWonderLand200.txt")

for line in story_file:
    words = split_line(line)
    line_number += 1
    for word in words:
        key = word
        i=0
        while i < len(dictionary_list) and dictionary_list[i] != word.upper():
            i += 1

        if i == len(dictionary_list):
            print("Line",line_number,"possible misspelled word",word)

story_file.close()

print("---Binary Search---")

story_file = open("AliceInWonderland200.txt")
for line in story_file:
    words = split_line(line)
    line_number += 1
    for word in words:
        key = word.upper()
        lower_bound = 0
        upper_bound = len(dictionary_list) - 1
        found = False

        # Loop until we find the item, or our upper/lower bounds meet
        while lower_bound <= upper_bound and not found:

            # Find the middle position
            middle_pos = (lower_bound + upper_bound) // 2

            # Figure out if we:
            # move up the lower bound, or
            # move down the upper bound, or
            # we found what we are looking for
            if dictionary_list[middle_pos] < key:
                lower_bound = middle_pos + 1
            elif dictionary_list[middle_pos] > key:
                upper_bound = middle_pos - 1
            else:
                found = True

        if not found:
            print("Line",line_number,"possible misspelled word",word)

story_file.close()











