def count_words(s):
  splitted = s.split()
  count = len(splitted)
  return count

def count_chars(s):

  chars_map = {}

  for char in s:

    if char.isalpha() != True:
      continue

    lower_case_char = char.lower()

    if lower_case_char not in chars_map:
      chars_map[lower_case_char] = 1
    else:
      chars_map[lower_case_char] += 1

  return chars_map