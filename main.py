from stats import count_words, count_chars
import sys

def read_file(file_path):
  with open(file_path) as f:
    return f.read()

def sort_map(map):
  return dict(sorted(map.items(), key=lambda item: item[1], reverse=True))

def main():

  if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  book_path = sys.argv[1]
  content = read_file(book_path)
  word_count = count_words(content)
  chars_map = count_chars(content)
  sorted_map = sort_map(chars_map)


  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")

  for key, value in sorted_map.items():
    print(f"{key}: {value}")
  
  print("============= END ===============")

main()