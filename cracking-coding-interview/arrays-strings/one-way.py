string_original = 'pale'

string_changed_a = 'marwa'
string_changed_b = 'pales'
string_changed_c = 'psale'
string_changed_d = 'ple'
string_changed_e = 'pal'
string_changed_f = 'ble'
string_changed_g = 'bale'
string_changed_h = 'palk'
string_changed_i = 'pakk'

def is_one_away(text_a, text_b):
  length_text_a = len(text_a)
  length_text_b = len(text_b)
  malcharacter_index = 'Not Found'

  if length_text_a == length_text_b:
    text_one = text_a
    text_two = text_b
  else:
    text_one = text_a if length_text_a < length_text_b else text_b
    text_two = text_a if length_text_a > length_text_b else text_b

  for character_index, character in enumerate(text_one):
    if text_one[character_index] != text_two[character_index]:
      malcharacter_index = character_index
      break

  if malcharacter_index == 'Not Found':
    if length_text_b != length_text_a:
      malcharacter_index = len(text_two) - 1
    else:
      return False

  if length_text_b != length_text_a:
    corrected_text_two = text_two[:malcharacter_index] + text_two[malcharacter_index+1:]
    if corrected_text_two == text_one:
      return True
  else:
    corrected_text_two = text_two[:malcharacter_index] + text_two[malcharacter_index+1:]
    corrected_text_one = text_one[:malcharacter_index] + text_one[malcharacter_index+1:]
    if corrected_text_two == corrected_text_one:
      return True

  return False

print(is_one_away(string_original, string_changed_a)) # False
print(is_one_away(string_original, string_changed_b)) # True
print(is_one_away(string_original, string_changed_c)) # True

print(is_one_away(string_original, string_changed_d)) # True
print(is_one_away(string_original, string_changed_e)) # True
print(is_one_away(string_original, string_changed_f)) # False

print(is_one_away(string_original, string_changed_g)) # True
print(is_one_away(string_original, string_changed_h)) # True
print(is_one_away(string_original, string_changed_i)) # False
