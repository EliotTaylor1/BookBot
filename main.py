def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_frequency = get_number_of_each_character(text)
    print_report(word_count, char_frequency)


def get_word_count(string):
    words = string.split()
    return len(words)


def get_book_text(book):
    with open(book) as b:
        return b.read()


def get_number_of_each_character(string):
    character_count = {}
    for char in string:
        lower = char.lower()
        if lower in character_count:
            character_count[lower] += 1
        else:
            character_count[lower] = 1
    return character_count


def print_report(word_count, char_frequency):
    print(f"There are: {word_count} words in this book.")
    print("Each letter appears this many times:")
    sorted_char_frequency = sorted(char_frequency.items(), key=lambda item: item[1], reverse=True)
    for char, frequency in sorted_char_frequency:
        if char.isalpha():
            print(f"{char} appears {frequency} times in this book")


main()
