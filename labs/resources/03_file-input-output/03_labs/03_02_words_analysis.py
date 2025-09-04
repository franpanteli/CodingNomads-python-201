#TASK
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

#READING IN THE WORDS FROM THE words.txt file
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

words = open("words.txt", "r")
# reader = words.read()
list_of_words = words.read().split() #reads the contents of the file,
                                    # and then splits it into a list of words
for i in list_of_words:
    if len(i) < 2:
        print(i)
        list_of_words.remove(i)

# 1. The shortest word (if there is a tie, print all)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#we know a function which prints the word length
length_list = [] #a list which contains the lengths of the words in list_of_words
for i in list_of_words:
    length_list.append(len(i))

# #get rid of the elements whose lengths are greater than 2
for index, length in enumerate(length_list):
    if length == min(length_list):
        print("Word of minimal length in list: ", list_of_words[index])

# 2. The longest word (if there is a tie, print all)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for index, length in enumerate(length_list):
    if length == max(length_list):
        print("Word of maximal length in list: ", list_of_words[index])

# 3. The total number of words in the file.
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
print("Total number of words in the file: ", len(list_of_words))

#CLOSE THE words.txt file
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
words.close()

#FILE OUTPUT
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
""" 
Word of minimal length in list:  aa
Word of minimal length in list:  ad
Word of minimal length in list:  ae
Word of minimal length in list:  ah
Word of minimal length in list:  ai
Word of minimal length in list:  am
Word of minimal length in list:  an
Word of minimal length in list:  ar
Word of minimal length in list:  as
Word of minimal length in list:  at
Word of minimal length in list:  aw
Word of minimal length in list:  ay
Word of minimal length in list:  ba
Word of minimal length in list:  be
Word of minimal length in list:  bi
Word of minimal length in list:  bo
Word of minimal length in list:  by
Word of minimal length in list:  da
Word of minimal length in list:  de
Word of minimal length in list:  do
Word of minimal length in list:  ef
Word of minimal length in list:  eh
Word of minimal length in list:  el
Word of minimal length in list:  em
Word of minimal length in list:  en
Word of minimal length in list:  er
Word of minimal length in list:  es
Word of minimal length in list:  et
Word of minimal length in list:  ex
Word of minimal length in list:  fa
Word of minimal length in list:  go
Word of minimal length in list:  ha
Word of minimal length in list:  he
Word of minimal length in list:  hi
Word of minimal length in list:  ho
Word of minimal length in list:  id
Word of minimal length in list:  if
Word of minimal length in list:  in
Word of minimal length in list:  is
Word of minimal length in list:  it
Word of minimal length in list:  jo
Word of minimal length in list:  ka
Word of minimal length in list:  la
Word of minimal length in list:  li
Word of minimal length in list:  lo
Word of minimal length in list:  ma
Word of minimal length in list:  me
Word of minimal length in list:  mi
Word of minimal length in list:  mu
Word of minimal length in list:  my
Word of minimal length in list:  na
Word of minimal length in list:  no
Word of minimal length in list:  nu
Word of minimal length in list:  od
Word of minimal length in list:  oe
Word of minimal length in list:  of
Word of minimal length in list:  oh
Word of minimal length in list:  om
Word of minimal length in list:  on
Word of minimal length in list:  op
Word of minimal length in list:  or
Word of minimal length in list:  os
Word of minimal length in list:  ow
Word of minimal length in list:  ox
Word of minimal length in list:  oy
Word of minimal length in list:  pa
Word of minimal length in list:  pe
Word of minimal length in list:  pi
Word of minimal length in list:  re
Word of minimal length in list:  sh
Word of minimal length in list:  si
Word of minimal length in list:  so
Word of minimal length in list:  ta
Word of minimal length in list:  ti
Word of minimal length in list:  to
Word of minimal length in list:  un
Word of minimal length in list:  up
Word of minimal length in list:  us
Word of minimal length in list:  ut
Word of minimal length in list:  we
Word of minimal length in list:  wo
Word of minimal length in list:  xi
Word of minimal length in list:  xu
Word of minimal length in list:  ya
Word of minimal length in list:  ye
Word of maximal length in list:  counterdemonstrations
Word of maximal length in list:  hyperaggressivenesses
Word of maximal length in list:  microminiaturizations
Total number of words in the file:  113809
"""