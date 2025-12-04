from stats import create_sorted_dict, get_char_count, get_word_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    print('============ BOOKBOT ============')
    book_loc = sys.argv[1]
    print('Analyzing book found at %s' % book_loc)
    text = get_book_text(book_loc)
    cnt = get_word_count(text)
    print('----------- Word Count ----------')
    print('Found %s total words' % (cnt))
    print('--------- Character Count -------')
    sorted_dict = create_sorted_dict(get_char_count(text))
    for entry in sorted_dict:
        if not entry["char"].isalpha():
            continue
        print('%s: %s' % (entry["char"], entry["num"]))


main()
