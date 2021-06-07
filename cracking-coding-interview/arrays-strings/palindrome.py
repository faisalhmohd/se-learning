string_a = 'taco cat'
string_b = 'cato tac'
string_c = 'catt cat'
string_d = 'taco atc'
string_e = 'taco cat'

def is_word_permutation(text_a, text_b):
  sorted_text_a = "".join(sorted(text_a))
  sorted_text_b = "".join(sorted(text_b))
  return sorted_text_a == sorted_text_b

def is_permutation(text_a, text_b):
  if len(text_a) != len(text_b):
    return False

  words_a = text_a.split(' ')
  words_b = text_b.split(' ')
  for word_index, value in enumerate(words_a):
    if not is_word_permutation(words_a[word_index], words_b[word_index]):
      return False

  return True

print(is_permutation(string_a, string_b))
print(is_permutation(string_a, string_c))
print(is_permutation(string_a, string_d))
print(is_permutation(string_a, string_e))