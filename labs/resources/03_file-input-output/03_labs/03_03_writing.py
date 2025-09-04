# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

#OPEN THE FILE AND READ INPUT FILE CONTENTS
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
file = open('words.txt', 'r')
contents = file.read()
split_contents = contents.split()

#REVERSE THE LIST CONTENTS
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
reversed_list = []
# for i in split_contents:
# print(split_contents)
for index, value in enumerate(split_contents):
    reversed_list.append(split_contents[len(split_contents)-1-index])

#reversed_list is a list of the words which the original list contains, but backwards

#CLOSE THE INPUT FILE
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
file.close()

words_reverse_txt = open("words_reverse.txt", "w")

for i in reversed_list:
    words_reverse_txt.write(i)
    words_reverse_txt.write("\n")

words_reverse_txt.close()