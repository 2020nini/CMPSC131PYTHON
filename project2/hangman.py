#Author: Wenrui Zhang wkz5094@psu.edu
from sys import argv
import random


def debug_print(s):
    if len(argv) > 4:
        print(s)


def normal_game():
    # python3 hangman.py w1.txt 8 7
    words = {}
    file = argv[1]
    len_word = int(argv[2])
    chances_num = int(argv[3])
    chances_tmp = chances_num
    with open(file, 'r') as f:
        word_list = f.readlines()
        for word in word_list:
            word = word.strip('\n')
            if len(word) not in words:
                words[len(word)] = [word]
            else:
                words[len(word)].append(word)
    if len_word not in words:
        print("No words of this length")
        return
    else:
        program_word = random.choice(words[len_word])
        user_words = ['_' for _ in range(len_word)]
        miss_str = ""
        while '_' in user_words:
            if chances_num == 0:
                break
            print("".join(user_words))
            print('missed letters: %s(%s chances left)' % (miss_str, chances_num))
            user_guess_char = input("Enter your guess: ")
            if user_guess_char not in program_word:
                chances_num -= 1
                miss_str = miss_str + user_guess_char + " "
            else:
                while user_guess_char in program_word:
                    index = program_word.index(user_guess_char)
                    program_word = program_word[:index] + '_' + program_word[index + 1:]
                    user_words[index] = user_guess_char
        if '_' not in user_words:
            print("You guessed the word: %s" % "".join(user_words))
        elif chances_num == 0:
            print("You lost after %s wrong guesses." % chances_tmp)


def wicked_game():
    file = argv[1]
    len_word = int(argv[2])
    chances_num = int(argv[3])
    chances_tmp = chances_num
    words = {}
    with open(file, 'r') as f:
        word_list = f.readlines()
        for word in word_list:
            word = word.strip('\n')
            if len(word) not in words:
                words[len(word)] = [word]
            else:
                words[len(word)].append(word)

    program_words = words[len_word]
    user_words = ['_' for _ in range(len_word)]
    miss_str = ""
    while chances_num:
        res = {}
        s = '%s words left.' % len(program_words)
        debug_print(s)
        print("".join(user_words))
        print('missed letters: %s(%s chances left)' % (miss_str, chances_num))
        user_guess_char = input("Enter your guess: ")
        for word in program_words:
            tmp_word = ''
            for char in word:
                if char == user_guess_char:
                    tmp_word += char
                else:
                    tmp_word += "_"
            if tmp_word in res:
                res[tmp_word].append(word)
            else:
                res[tmp_word] = [word]
        program_words = res["".join(user_words)]
        for key in res:
            s = "%s: %s" % (key, len(res[key]))
            debug_print(s)
        chances_num -= 1
        miss_str = miss_str + user_guess_char + " "
    print("You lost after %s wrong guesses." % chances_tmp)


if __name__ == '__main__':
    normal_game()