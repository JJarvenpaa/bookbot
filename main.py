from stats import count_words, get_book_text, char_count;


def main():
    book = get_book_text('./books/frankenstein.txt');
    num_words = count_words(book);
    print(f'{num_words} words found in the document');

    chars = char_count(book);
    print(chars);

main();

