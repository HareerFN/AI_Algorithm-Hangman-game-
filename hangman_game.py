import random
def calculate_scores(word_list, guessed_chars):
    """
    Calculate scores for each character based on a heuristic.
    """
    scores = {}
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in guessed_chars:
            score = 0
            for word in word_list:
                if all(c in word for c in guessed_chars):
                    score += word.count(char)
            scores[char] = score
    return scores

def greedy_guess(word_list, guessed_chars):
    """
    Choose the next guess based on a greedy strategy.
    """
    scores = calculate_scores(word_list, guessed_chars)
    return max(scores, key=scores.get)

def hangman(word_list):
    """
    Play a game of Hangman using a greedy strategy.
    """
    while True:
        word = random.choice(word_list)
        guessed_chars = set()
        attempts_left = 6
        guessed_word = ['_' for _ in word]

        print("Let's play Hangman!")
        print("The word to guess:", " ".join(guessed_word))

        while attempts_left > 0 and "_" in guessed_word:
            print("\nAttempts left:", attempts_left)
            print("Guessed characters:", ", ".join(guessed_chars))

            guess = greedy_guess(word_list, guessed_chars)

            if guess in guessed_chars:
                print("You already guessed that character!")
                continue

            guessed_chars.add(guess)
            if guess in word:
                print("Correct guess!")
                for i, letter in enumerate(word):
                    if letter == guess:
                        guessed_word[i] = guess
            else:
                attempts_left -= 1
                print("Incorrect guess!")

            print("The word to guess:", " ".join(guessed_word))
            print("\n   --------    ")
            print("   |      |    ")
            print("   |      " + ("O" if attempts_left < 6 else ""))
            print("   |     " + ("/" if attempts_left < 5 else " ") + ("|" if attempts_left < 4 else "") + ("\\" if attempts_left < 3 else ""))
            print("   |     " + ("/ " if attempts_left < 2 else "") + ("\\" if attempts_left < 1 else ""))
            print("  ---          ")

        if "_" not in guessed_word:
            print("\nCongratulations, you won! The word was:", word)
        else:
            print("\nSorry, you lost! The word was:", word)

        play_again = input("Do you want to play again? (0 for No, 1 for Yes): ")
        if play_again != '1':
            break

word_list = []
with open('words.txt', 'r') as fh:
    for line in fh:
        word_list.append(line.strip())

hangman(word_list)