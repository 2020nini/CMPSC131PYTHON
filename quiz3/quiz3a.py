# Author: Wenrui Zhang wkz5094@psu.edu
# GitHub ID: 2020nini

with open("words.txt", 'r') as f:
    words = f.readlines()
len_4_words_list = []

for word in words:
    word = word.strip("\n")
    if len(word) == 4:
        len_4_words_list.append(word)
print(len(len_4_words_list))

char = ['a','e','i','o','u']
res = 0
for word in len_4_words_list:
    times = 0
    for ch in word:
        if ch in char:
            times += 1
    if times >= 2:
        res += 1
print(res)
