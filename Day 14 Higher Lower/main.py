
import random
from game_data import data
from art import logo, vs
from replit import clear


def randomInt():
  randInt = random.randint(0,49)
  return randInt


def printDictData (dictionariesNumber1,dictionariesNumber2):
#Function takes two random numbers, prints the needed values of the dictionary keywords
#it compares the followers number and returns the winner
  print(f"Compare A: {data[dictionariesNumber1]['name']}, a {data[dictionariesNumber1]['description']}, from {data[dictionariesNumber1]['country']}.")
  print(vs)
  print(f"Against B: {data[dictionariesNumber2]['name']}, a {data[dictionariesNumber2]['description']}, from {data[dictionariesNumber2]['country']}.")

  if (data[dictionariesNumber1]['follower_count']) > (data[dictionariesNumber2]['follower_count']):
    return 0
  else:
    return 1



def higherFollowersNumberGame():
  clear() 
  print(logo)
  print("Welcome to the Instagram followers higher lower game.")

  randomDictEntry1 = randomInt()

  usersScore = 0


  currentlyPlaying = True

  while currentlyPlaying:
  #Player keeps choosing who he thinks has more followers
  #Computer displays entries and calculates if user is righta  
    randomDictEntry2 = randomInt()
    if randomDictEntry1 == randomDictEntry2:
      randomDictEntry2 = randomInt()

    if usersScore > 0:
      print(f"That's right. Your current score is {usersScore}.")

    winnerFollowers = printDictData(randomDictEntry1,randomDictEntry2)

    
    usersChoice = ""
    usersChoice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if usersChoice == 'a' and winnerFollowers == 0 or usersChoice == 'b' and winnerFollowers == 1:
      #continue playing
      randomDictEntry1 = randomDictEntry2
      usersScore += 1
      clear() 
      print(logo)
    else:
      #game is lost
      print("I'm sorry, you lost")
      currentlyPlaying = False


higherFollowersNumberGame()

