def get_book_text(path):
    file_content = None;

    with open(path) as f:
        file_content = f.read();
    
    return file_content;

def count_words(text):
    words = text.split();

    return len(words);


def main():
    book = get_book_text('./books/frankenstein.txt');
    num_words = count_words(book);
    
    print(f'{num_words} words found in the document');

main();

