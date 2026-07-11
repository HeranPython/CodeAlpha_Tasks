import random

word_list = ["APPLE", "EDUCATION", "PYTHON", "ORANGE", "ELEPHANT"]

while True:

    secret_word = random.choice(word_list).upper()

    guessed_letters = []

    lives = 6

    display = ["_"] * len(secret_word)

    while lives > 0 and "_" in display:
        
        print("\nWord:", " ".join(display))
        print("Lives:", lives)

        guess = input("Enter a letter: ").upper()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!")

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display[i] = guess
        else:
            print("Wrong ❌")
            lives -= 1

    if "_" not in display:
        print("\nYou won! The word was:", secret_word)
    else:
        print("\nGame over. The word was:", secret_word)

    while True:
        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again == "yes":
            break

        elif again == "no":
            print("Thanks for playing!")
            quit()

        else:
            print("Invalid choice. Please enter yes or no.")

   

