def main():
    with open("books/frankenstein.txt", 'r', encoding='utf-8') as f:
        file_contents = f.read().replace('\r\n', '\n').lower()
    
    # Count words
    words = file_contents.split()
    num_words = len(words)
    
    # Count alphabetic characters
    char_count = {}
    for char in file_contents:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
 
    
    # Print report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    
    
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

main()