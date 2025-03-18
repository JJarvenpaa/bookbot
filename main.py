from stats import count_words, get_book_text, char_count, sort_chars, print_report;


def main():
    book_file = './books/frankenstein.txt';
    book = get_book_text(book_file);
    num_words = count_words(book);

    chars = char_count(book);
    sorted_chars = sort_chars(chars);

    print_report(sorted_chars, num_words, book_file);

main();

