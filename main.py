# main.py
import sys
from stats import word_num, char_counter, sort_on

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, "r", encoding="utf-8") as f:
        return f.read()

def main():
    # Require exactly one CLI argument: the path to the book
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: file not found: {book_path}")
        sys.exit(1)
    except OSError as e:
        print(f"Error: could not read '{book_path}': {e}")
        sys.exit(1)

    total_words = word_num(text)
    sorted_chars = sort_on(char_counter(text))  # [{"item": "e", "num": 123}, ...]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['item']}: {entry['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
