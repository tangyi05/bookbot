import sys
from stats import word_count, char_count, char_count_sorted


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_cnt = word_count(text)
    char_cnt = char_count(text)
    sorted_char_cnt = char_count_sorted(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_path)
    print("----------- Word Count ----------")
    print(f"Found {word_cnt} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_cnt:
        print(f"{char}: {count}")
    print("============= END ===============")
    


main()