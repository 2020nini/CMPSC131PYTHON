
      ans.append(x)
  return ans

def mymap(t, f):
  """
  t is a list, f is a function that maps an element x in t to
  a different value f(x).
  Return a new list that has every element x from t mapped to f(x).
  """
  ans = []
  for x in t:
    ans.append(f(x))
  return ans

if __name__ == "__main__":
  words = get_words("words.txt")
  print(f"{len(words)} words in words.txt.")
  words1 = myfilter(words, has_no_e)
  print(f"{len(words1)} words has no 'e'.")
  print(f"{len(words1)/len(words)} of the words has no e.")
  wordlens = mymap(words, len)
  print(max(wordlens))

