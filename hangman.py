import random

# List of 5 predefined words
words = ["python", "computer", "program", "developer", "keyboard"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong guesses
wrong_guesses = 0
max_wrong_guesses = 6

# Hidden version of the word
display_word = ["_"] * len(word)

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

# Game loop
while wrong_guesses < max_wrong_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    guess = input("Guess a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether letter is in the word
    if guess in word:
        print("Good guess!")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in display_word:
    print("\nCongratulations! 🎉")
    print("You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)
