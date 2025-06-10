def count_words(text):
    words = text.split()
    return len(words)

def main():
    user_input = input("Enter a sentence: ")
    word_count = count_words(user_input)
    print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()

