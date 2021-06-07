string_a = 'abc'
string_b = 'bac'
string_c = 'def'
string_d = 'cef'

def is_permutation(text_a, text_b):
  sorted_text_a = "".join(sorted(text_a))
  sorted_text_b = "".join(sorted(text_b))
  return sorted_text_a == sorted_text_b

print(is_permutation(string_a, string_b))
print(is_permutation(string_a, string_c))
print(is_permutation(string_a, string_d))