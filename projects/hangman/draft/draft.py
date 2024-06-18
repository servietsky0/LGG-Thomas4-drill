def get_word() -> str :
    word : str = input("enter the word: ")
    return word

def get_lives() -> int :
    lives : int = int(input("enter the number of lives: "))
    return lives

def get_guess(suggested_letters : list [str]) -> str :
    while True:
        guess : str = input("enter a letter: ").upper()
        if len(guess) != 1:
            print("only one letter")
        elif guess in suggested_letters:
            print("already guessed that letter")
        else:
            return guess

def assess_guess(secret_word : str, guessed_letter : str, lives_left : int) -> int :
    if guessed_letter in secret_word:
        return lives_left
    else:
        print(f"{guessed_letter} is not in the word.")
        return lives_left - 1


def display_word(secret_word : str, suggested_letters : list [str]) -> bool :
    displayed_word = ''.join([letter if letter in suggested_letters else '_' for letter in secret_word])
    print(displayed_word)
    return displayed_word == secret_word

def main():
    secret_word : str = get_word()
    lives : int = get_lives()
    guessed_letters : list [str] = []
    
    while lives > 0:
        guess : str = get_guess(guessed_letters)
        guessed_letters.append(guess)
        lives : int = assess_guess(secret_word, guess, lives)
        
        if display_word(secret_word, guessed_letters):
            print("congratulations")
            break
    else:
        print("u lost..")

if __name__ == "__main__":
    main()