from stats import get_num_words
from stats import get_num_chars
from stats import sort_dict

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_dict = get_num_chars(text)
    char_list = []
    char_list = sort_dict(char_dict) 
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in char_list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()
