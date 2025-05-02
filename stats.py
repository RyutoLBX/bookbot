def get_book_text(filepath: str) -> str:
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def get_num_words(book: str) -> int:
  words = book.split()
  num_words = len(words)
  return num_words

def get_letter_counts(book: str) -> dict[str, int]:
  letters = list(book)
  letter_counts: dict[str, int] = {}
  for l in letters:
      if l.lower() in letter_counts:
        letter_counts[l.lower()] += 1
      else:
          letter_counts[l.lower()] = 1
  return letter_counts

def print_analysis(book_filepath: str) -> None:
  book = get_book_text(book_filepath)
  word_count = get_num_words(book)
  character_counts = get_letter_counts(book)
  sorted_character_counts = sorted(character_counts.items(),
    key=lambda kv: (kv[1], kv[0]),
    reverse=True)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_filepath}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for c in sorted_character_counts:
     if c[0].isalpha():
      print(f"{c[0]}: {character_counts[c[0]]}")
  print("============= END ===============")