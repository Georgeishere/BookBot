def count_words(book):
    count = len(book.split())
    return count

def count_chars(book):
    lower_case_book = book.lower()
    chars = list(lower_case_book)
    char_dict = {}

    for char in chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def sort_your(dict):
    report_list = []
    for char, count in dict.items():
        if char.isalpha():
            report_list.append({"char": char, "count": count})

    report_list.sort(reverse=True, key=sort_on)
    return report_list

def make_report(word_count, char_counts):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in char_counts:
        char = item["char"]
        count = item["count"]
        print(f"{char}: {count}")
    pass