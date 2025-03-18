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

def sort_by_count(dict): 
    return dict['count'];

def sort_chars(chars):
    sorted_chars = [];

    for k in chars:
        char_dict = {'char': k, 'count': chars[k]};
        sorted_chars.append(char_dict);
    
    sorted_chars.sort(reverse = True, key = sort_by_count);
    
    return sorted_chars;

def print_report(sorted_chars = [], num_words = 0, book = ''):
    print('============ BOOKBOT ============');
    print('Analyzing book found at ' + book);
    print('----------- Word Count ----------');
    print(f'Found {num_words} total words');
    print('--------- Character Count -------');
    for dict in sorted_chars:
        if(dict['char'].isalpha() != True): continue;

        print(f"{dict['char']}: {dict['count']}");
    
    print('============= END ===============');


