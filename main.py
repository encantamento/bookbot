import sys

from stats import (
    get_num_words,
    get_num_char,
    sort_char_list,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char_dict = get_num_char(text)
    ch_sort_list = sort_char_list(num_char_dict)
    print_report(book_path, num_words, ch_sort_list)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def print_report(book_path, num_words, ch_sort_list):
    print("=============BOOKBOT==============")
    print(f"Analyzing book found at {book_path}...")
    print("------------Word Count------------")
    print(f"Found {num_words} total words")
    print("---------Character Count----------")
    for i in ch_sort_list:
        if not i["char"].isalpha():
            continue
        print(f"{i['char']}: {i['num']}")

    print("================END===============")


main() 
