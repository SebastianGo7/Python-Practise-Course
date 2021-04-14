

from art import logo
import random
import replit

print(logo)


def randomNumber():
  #creates a random number
  return random.randint(0,100)


def checkNumber(guessedNumber,solution):
  #returns result guess
  if guessedNumber > solution:
    return "too high"
  elif guessedNumber < solution:
    return "too low"
  elif guessedNumber == solution:
    return "right, you won the game"
  else:
    return "not a number between 0 and 100"



gameRunning = True

while gameRunning == True:
  #loop which runs as long as game runs
  difficultyLevel = input("Feel free to choose your game level 'easy' or 'hard' ")

  guesses = 10

  if difficultyLevel == 'hard':
    guesses = 5

  print(f"You have {guesses} tries to guess the solution.")


  currentlyGuessing = True

  currentSolution = randomNumber()

  while currentlyGuessing == True:
    #loop runs when being in a game guessing one number
    guess = int(input ("Please guess a number between 1 and 100:  "))
    
    print(f"Your chosen value is {checkNumber(guess, currentSolution)}")



    if currentSolution == guess:

      continuation = (input("Do you want to play another game? Type 'y' or 'n'  ")).lower()
      currentlyGuessing = False
      if continuation == 'y':
        replit.clear()
        break
      else:
        gameRunning = False


    guesses -=1
    if guesses == 0:
      currentlyGuessing = False
      print("You used all the trials and lost the game.")
      continuation = (input("Do you want to play another game? Type 'y' or 'n'  ")).lower()
      if continuation == 'y':
        replit.clear()
        break
      else:
        currentlyGuessing = False
        gameRunning = False
      





