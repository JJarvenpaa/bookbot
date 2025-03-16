def count_words(text):
    words = text.split();

    return len(words);

def get_book_text(path):
    file_content = None;

    with open(path) as f:
        file_content = f.read();
    
    return file_content;

def char_count(text):
    chars = {};

    for char in text:
        lower_char = char.lower();
        if(lower_char in chars):
            chars[lower_char] += 1;
        else:
            chars[lower_char] = 1;

    return chars;

