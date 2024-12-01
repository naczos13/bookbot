from collections import Counter

def count_words(text: str) -> int:
    return len(text.split())

def count_letter(text: str) -> dict[str, int]:
    counter = Counter(text.lower())
    return counter
    

def main():
    path_to_file = "./books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        letter_counter = count_letter(file_contents)
        print(f"--- Begin report of {path_to_file} ---")
        print(f"{word_count} words found in the document")
        for letter, number in letter_counter.items():
            print(f"The '{letter}' character was found {number} times")
        print("--- End report ---")  
main()