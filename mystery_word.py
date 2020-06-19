import random

debug = False

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
    word = ""
    maxlength = 6 if difficulty == 1 else 8
    minlength = 4 if difficulty == 1 else 6 if difficulty == 2 else 8
    f = open('words.txt', 'r')
    words = f.read().split()
    while len(word) < minlength or len(word) > maxlength:
        word = words[random.randint(0, len(words)-1)].lower()
    f.close()
    return word

def startgame(): # This is a bit too long but it works for now.
    word = randomword()
    if debug: # it's not cheating i swear
        print(word)
    letters = [{"char": word[i], "guessed": False} for i in range(len(word))]
    wrong = 0
    guesses = []
    while True:
        string = ""
        for letter in letters:
            char = letter["char"]
            if letter["guessed"]:
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
            for letter in letters:
                if guess == letter["char"]:
                    letter["guessed"] = True
                    correct = True
        else:
            err()
            continue
        if correct:
            print('Correct!')
        else:
            print('Incorrect')
            wrong += 1
        correctcount = 0
        for letter in letters:
            if letter["guessed"]:
                correctcount += 1
        if correctcount == len(word):
            print("You won!")
            print(f"Your word was {word}")
            if input("Would you like to play again? (y/n): ").lower() == "y":
                startgame()
            else:
                exit(1)
        if wrong == 8:
            print("Too many wrong letters. Game over!")
            print(f"Your word was {word}")
            exit(1)

if __name__ == '__main__':
    startgame()