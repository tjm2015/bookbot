def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_of_words = count_words(text)
    count_of_characters = count_characters(text)
    alpha_dict_sorted = sort_characters_output(count_of_characters)
    #print(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_of_words} found in the in the document")
    print()
    #print(count_of_characters)
    [print(f"The '{key}' character was found {value} times") for key, value in alpha_dict_sorted.items()]
    print("--- End Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_dict = {}
    lowered_text = text.lower()
    for s in lowered_text:
        if s in character_dict:
            character_dict[s] += 1
        else:
            character_dict[s] = 1
    return character_dict

def sort_characters_output(characters_dict):
    alpha_characters = [key for key in characters_dict if key.isalpha()]
    alpha_dict = {key:value for key, value in characters_dict.items() if key in alpha_characters}
    alpha_dict_sorted = dict(sorted(alpha_dict.items(), key=lambda item: item[1], reverse=True))
    return alpha_dict_sorted

main()