def main():
    user_input = input("What's your input? ")
    output = shorten(user_input)
    print(f"{output}")
def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for vowel in vowels:
        word = word.replace(vowel, "")
    return word
if __name__ == "__main__":
    main()