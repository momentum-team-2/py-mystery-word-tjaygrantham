import random
import math

debug = False

class Letter:

    def __init__(self, letterstr):
        self.str = letterstr
        self.guessed = False

    def __str__(self):
        return self.str

class Word:

    def __init__(self, wordstr):
        self.str = wordstr
        self.length = len(self.str)
        self.letters = [Letter(self.str[i]) for i in range(self.length)]

    def guessed(self):
        return True if sum([1 if letter.guessed else 0 for letter in self.letters]) == self.length else False

    def __str__(self):
        return self.str

def err():
    print("Invalid input, try again.")

def getdifficulty(): # Let player input the difficulty, catch any invalid input
    difficulty = 0
    difficulties = [1, 2, 3]
    while difficulty not in difficulties:
        try:
            difficulty = input('Choose a difficulty (1 for easy, 2 for medium, 3 for hard): ')
            if not difficulty or difficulty.isalpha() or int(difficulty) not in difficulties:
                err()
            else:
                difficulty = int(difficulty)
        except:
            err()
    return difficulty

def randomword(): # Return a random word from words.txt if length matches the difficulty standards
    difficulty = getdifficulty()
    word = Word("")
    maxlength = 6 if difficulty == 1 else 8 if difficulty == 2 else math.inf
    minlength = 4 if difficulty == 1 else 6 if difficulty == 2 else 8
    f = open('words.txt', 'r')
    words = f.read().split()
    while word.length < minlength or word.length > maxlength:
        word = Word(words[random.randint(0, len(words)-1)].lower())
    f.close()
    return word

def startgame(): # This is a bit too long but it works for now.
    word = randomword()
    if debug: # it's not cheating i swear
        print(word)
    wrong = 0
    guesses = []
    while True:
        string = ""
        for letter in word.letters:
            char = letter.str
            if letter.guessed:
                string += f" { char } "
            else:
                string += " _ "
        print(string)
        print(f'You have {8 - wrong} more tries')
        correct = False
        guess = input('Guess a letter: ')
        if len(guess) == 1 and guess.isalpha():
            if guess in guesses:
                print(f"You've already guessed {guess}, try again.")
                continue
            guesses.append(guess)
            for letter in word.letters:
                if guess == letter.str:
                    letter.guessed = True
                    correct = True
        else:
            err()
            continue
        if correct:
            print('Correct!')
        else:
            print('Incorrect')
            wrong += 1
        if word.guessed():
            print("You won!")
            print(f"Your word was {word}")
            break
        elif wrong == 8:
            print("Too many wrong letters. Game over!")
            print(f"Your word was {word}")
            break
    if input("Would you like to play again? (y/n): ").lower() == "y":
        startgame()
    else:
        exit(1)

if __name__ == '__main__':
    startgame()