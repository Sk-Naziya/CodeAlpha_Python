import random

words = [
    "python",
    "laptop",
    "streamlit",
    "coding",
    "github"
]

word = random.choice(words)

guessed_letters = []

wrong_guesses = 0
max_wrong = 6

display_word = ["_"] * len(word)

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while wrong_guesses < max_wrong and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

        print("✅ Correct!")

    else:

        wrong_guesses += 1
        print("❌ Wrong guess!")

if "_" not in display_word:

    print("\n🎉 Congratulations!")
    print("You guessed the word:", word)

else:

    print("\n💀 Game Over!")
    print("The word was:", word)