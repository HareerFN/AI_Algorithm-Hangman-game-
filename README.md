# AI_Algorithm-Hangman-game-


This project is a **Hangman game** where the AI uses a **greedy algorithm** to make guesses. Instead of guessing randomly, the AI chooses the letter that is most likely to appear in the word based on the current state of the game.

1. **Greedy Algorithm**:
   - The AI evaluates each possible letter and calculates a **score** based on how often it appears in words that still match the partially guessed word. It then chooses the letter with the highest score to guess next.
   - The goal is to optimize guesses and minimize the number of wrong attempts, making the AI more efficient than random guessing.

2. **Word Selection**:
   - The AI guesses letters from a list of words pulled from a text file (`words.txt`). It updates its guesses based on which letters have already been tried and whether they appear in the word.

3. **Gameplay**:
   - The game selects a random word, and the AI makes guesses based on its greedy strategy. You have 6 attempts to guess the word, and each incorrect guess brings the player closer to losing.

4. **Visual Feedback**: 
   - If the AI guesses incorrectly, a visual hangman figure is drawn to indicate the remaining attempts.

5. **Replayability**: 
   - After finishing a game, you can choose to play again with a new word.

By using the **greedy algorithm**, this version of Hangman tries to make the AI smarter in its guessing strategy, ensuring it performs better than random guessing while still being fun to play.
