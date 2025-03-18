import sys;

from stats import count_words, get_book_text, char_count, sort_chars, print_report;


def main():
    if(len(sys.argv) < 2):
        print('Usage: python3 main.py <book_file_name_no_extension>');
        sys.exit(1);
    
    book_file = './books/' + sys.argv[1] + '.txt';
    book = get_book_text(book_file);
    num_words = count_words(book);

    chars = char_count(book);
    sorted_chars = sort_chars(chars);

    print_report(sorted_chars, num_words, book_file);

main();

