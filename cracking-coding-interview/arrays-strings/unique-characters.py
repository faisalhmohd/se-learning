string_a = 'university'
string_b = 'string'

def has_unique_characters(text):
  text_set = set(text)
  return len(text_set) == len(text)

print(has_unique_characters(string_a))
print(has_unique_characters(string_b))

def has_unique_characters_without_memory(text):
  previous_char = ''

  for char in sorted(text):
    if not previous_char:
      previous_char = char
      continue
    else:
      if char == previous_char:
        return False
      previous_char = char

  return True

print(has_unique_characters_without_memory(string_a))
print(has_unique_characters_without_memory(string_b))