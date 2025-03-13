def get_book_text(path):
    file_content = None;

    with open(path) as f:
        file_content = f.read();
    
    return file_content;


def main():
    book_text = get_book_text('./books/frankenstein.txt');
    print(book_text);

main();

