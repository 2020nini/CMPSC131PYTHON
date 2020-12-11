#Author: Wenrui Zhang wkz5094@psu.edu
from sys import argv



def mix_pat(p1, p2):
  if p1 == p2:
    return p1
  res = ''
  for i in range(len(p1)):
    if p1[i] == '_' and p2[i] == '_':
      res += '_'
    elif p1[i] != '_' and p2[i] != '_':
      raise Exception(p1 + p2)
    else:
      res += p1[i] if p1[i] != '_' else p2[i]
  return res



def generate_pattern_dict(word_list, letter):
  patterns={}
  for word in word_list:
    pat = ''.join([l if l == letter else '_' for l in word])    
    if pat not in patterns:
      patterns[pat] = []
    patterns[pat].append(word)
  return patterns



def select_pattern(patterns):
  pat_to_amount = [(p, len(l)) for p, l in patterns.items()]
  pat_to_amount.sort(key=lambda x: x[0])
  pat_to_amount.sort(key=lambda x: x[0].count('_'))
  pat_to_amount.sort(key=lambda x: x[1])

  for a, b in pat_to_amount:
    debug_print(f'{a}:{b}')
  return pat_to_amount[-1][0]


def get_word_list(filename, word_len):
  with open(filename, 'r') as f:
    word_list = f.read().strip().split('\n')
  word_list = [i for i in word_list if len(i) == word_len]
  if not word_list:
    exit(-1)
  return word_list




def main():
  filename = argv[1]
  word_len = argv[2]
  wrong_times = argv[3]

  # filename = 'word.txt'
  # word_len = 8
  # wrong_times = 7

  word_list = get_word_list(filename, word_len)
  missed_letter = []
  current_pat = '_'*word_len
  current_word_list = word_list
  while True:
    if wrong_times <= 0:
      print(f'You lost after {len(missed_letter)} wrong guesses.')
      break
    elif '_' not in current_pat:
      print(f'You guessed the word: {current_pat}')
      break

    debug_print(f'{len(current_word_list)} words left.')

    patterns = {}
    print(current_pat)
    print(
      f'missed letters: {" ".join(missed_letter)} ({wrong_times} chances left)')
    letter = input('Enter your guess: ')

    
    patterns = generate_pattern_dict(current_word_list, letter)

    
    if '_' * word_len in patterns:
      wrong_times -= 1
      missed_letter.append(letter)

    
    patterns = {mix_pat(k, current_pat): v for k, v in patterns.items()}

    
    current_pat = select_pattern(patterns)
    current_word_list = patterns[current_pat]

    print('')


if __name__ == "__main__":
  main()
