#importing number of words function from a seperate file
from stats import number_of_words
from stats import char_in_text

def main():
    
    print(char_in_text(get_book_text("books/frankenstein.txt")))

def get_book_text(file_path):
    #opening a file (text file for the books)
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



main()

