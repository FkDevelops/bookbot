#importing number of words function from a seperate file
from stats import number_of_words
from stats import char_in_text
from stats import dict_sort

def main():
    #turn text into a dict with characters and count
    unsorted_dict = char_in_text(get_book_text("books/frankenstein.txt"))
    #sort the dict
    sorted_dict = dict_sort(unsorted_dict)

    #printing message that states where the book is found
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(number_of_words(get_book_text("books/frankenstein.txt")))
    print('--------- Character Count -------')

    #loop to only print alphabets
    for i in sorted_dict:
        ch = i["char"]
        num = i["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    
    #print END message
    print("============= END ===============")

def get_book_text(file_path):
    #opening a file (text file for the books)
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



main()

