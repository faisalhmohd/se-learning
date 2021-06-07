string_a = 'Mr John Smith'
string_b = 'Cracking the Coding Interview'

def urlify(text):
  return text.replace(' ', '%20')

print(urlify(string_a), urlify(string_a) == 'Mr%20John%20Smith')
print(urlify(string_b), urlify(string_b) == 'Cracking%20the%20Coding%20Interview')