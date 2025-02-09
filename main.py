def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_of_words = count_words(text)
    count_of_characters = count_characters(text)
    alpha_dict_sorted = sorted_alpha_characters_dict(count_of_characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_of_words} found in the in the document")
    print()
    [print(f"The '{key}' character was found {value} times") for key, value in alpha_dict_sorted.items()]
    print("--- End Report ---")

def get_book_text(path):
    # Take book path and read the text for futher analysis
    with open(path) as f:
        return f.read()

def count_words(text):
    # Take the text and split into a list on the white spaces to count number of words
    words = text.split()
    return len(words)

def count_characters(text):
    character_dict = {}
    lowered_text = text.lower()

    # count each character in the text by adding to a dictionary
    for s in lowered_text:
        if s in character_dict:
            character_dict[s] += 1
        else:
            character_dict[s] = 1
    return character_dict

def sorted_alpha_characters_dict(characters_dict):
    alpha_dict = {key:value for key, value in characters_dict.items() if key.isalpha()}
    alpha_dict_sorted = dict(sorted(alpha_dict.items(), key=lambda item: item[1], reverse=True))
    return alpha_dict_sorted

main()