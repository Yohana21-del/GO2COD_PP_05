import random

def hangman():
    
    word_list = ["dog", "cat", "bird", "fish", "cow", "horse", "sheep", "pig", "goat", "duck", "turkey", "chicken", "rabbit", "mouse", "deer", "bear", "lion", "tiger", "monkey", "elephant", "giraffe", "zebra", "crocodile", "snake", "turtle", "frog", "butterfly", "bee", "ant", "spider"]

    word = random.choice(word_list)


    attempts = 6


    display_word = ["_" for _ in word]

    while attempts > 0:
       
        print("Word:", " ".join(display_word))
        print("Attempts remaining:", attempts)

        
        guess = input("Guess a letter: ").lower()

        
        if guess in word:
           
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess

           
            if "_" not in display_word:
                print("Congratulations! You guessed the word:", word)
                return

        else:
            attempts -= 1

    print("You ran out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()