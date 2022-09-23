import random
import hangman_words
import hangman_art

print(hangman_art.logo)
#word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
print(f"the chosen word is {chosen_word} ")

display =[]
for i in range(word_length):
    display.append("_")

print(display)
while not end_of_game:
    guess = input("guess a letter : ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, thats not in the word. You lose a life")
        lives -= 1
        if lives == 0 :
            print("You Lose! ")
            end_of_game = True

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(hangman_art.stages[lives])
