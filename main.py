from stats import count_words, count_chars, sort_your, make_report
import sys

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def main():

    if len(sys.argv) == 2:
        try:
            words = get_book_text(sys.argv[1])
        except Exception as e:
            print(f"Error encountered: {e}")
            sys.exit(1)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    count = count_words(words)
    char_list = count_chars(words)
    report_list = sort_your(char_list)
    make_report(count, report_list)

main()