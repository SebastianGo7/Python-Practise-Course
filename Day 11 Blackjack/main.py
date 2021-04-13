
import random
from art import logo
import replit


def createAppendRandomCard(cardList):
#creates a random card with one of the values
#and appends it to the previous List

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  cardList.append(random.choice(cards))
  return (cardList)





def ComputerCardDecision(compActualResult):

  randNumberTo10 = random.randint(0,9)

  oneMoreCard = False
  
  if compActualResult >18 and compActualResult < 22:
    oneMoreCard = False

  elif compActualResult >=15:
    #take card 30% of the times when actual value is 15,16,17,18
    if randNumberTo10 > 6:
        oneMoreCard = True

  elif compActualResult >=12:
    #take card 70% of the times when actual value is 12,13,14
    if randNumberTo10 > 2:    
      oneMoreCard = True

  else:
    #always take a card as value is below 12
      oneMoreCard = True

  return oneMoreCard      





def calculateSumCards (cardsList):
  #gets a List of numbers, and calculates the highest possible sum below 21
  #considering that the aces can be 1 or 10 

  cardSum = sum(cardsList)

  for ace in range (0, cardsList.count(11)):
    if cardSum > 21:
      cardSum -= 10

      for index in range (len(cardsList)):
        if (cardsList[index] == 11):
          cardsList[index] = 1
          break


  return cardSum, cardsList



def printFinalScore():

  print(f"Your final hand: {calculateSumCards(playerCurrentCardList)[1]}, final score: {calculateSumCards(playerCurrentCardList)[0]}")

  print(f"Computer's final hand: {calculateSumCards(compCurrentCardList)[1]}, final score: {calculateSumCards(compCurrentCardList)[0]}")    



gameDesired = True 

while gameDesired == True:
#Asking if Game is Desired and dealer distributes first four cards:
  playerCurrentCardList = []
  compCurrentCardList = []

  playerCurrentCardList = createAppendRandomCard (playerCurrentCardList)
  playerCurrentCardList = createAppendRandomCard (playerCurrentCardList)

  compCurrentCardList = createAppendRandomCard (compCurrentCardList)
  compCurrentCardList = createAppendRandomCard (compCurrentCardList)



  startRequest = (input("Do you want to play a round of Blackjack? Type 'y' or 'n'")).lower()

  #stop game if not desired
  if startRequest == "n":
    gameDesired = False
    break


  replit.clear()
  print(logo)

  drawingCards = True      

  while drawingCards == True:
    #cards are being distributed until player stop requesting
    #afterwards computer gets cards depending on logic and the scores are compared

    
    if calculateSumCards(playerCurrentCardList)[0] > 21:
      #in case Player went over 21, the game stops and the computer wins
      printFinalScore()

      print("You went over 21, You lost. ")
      break

    if (playerCurrentCardList[0] == 10 and playerCurrentCardList[1] == 11) or (playerCurrentCardList[0] == 11 and playerCurrentCardList[1] == 10):
      printFinalScore()
      print("You have Black Jack. You won the game. ")
      break



    print(f"Your cards: {calculateSumCards(playerCurrentCardList)[1]}, current score: {calculateSumCards(playerCurrentCardList)[0]}")

    print(f"Computer's first card is: {compCurrentCardList[0]}")

    furtherRequests = (input("Do you want one more card? Type 'y' or 'n'")).lower()

    if furtherRequests == 'y':
      playerCurrentCardList = createAppendRandomCard(playerCurrentCardList)


    elif (compCurrentCardList[0] == 10 and compCurrentCardList[1] == 11) or (compCurrentCardList[0] == 11 and compCurrentCardList[1] == 10):
      printFinalScore()
      print("The computer has Black Jack. You lost the game. ")
      break



    else:   
      #computer gets more cards depending on my computer logic function
      computersDecision = True
      while computersDecision == True:
        computersDecision = ComputerCardDecision(calculateSumCards(compCurrentCardList)[0])
        if computersDecision == True:
          compCurrentCardList = createAppendRandomCard(compCurrentCardList) 



    #Compare Scores here
      if calculateSumCards(compCurrentCardList)[0] > 21:
        printFinalScore()
        print("The computer went over. You won the Game")        


      elif calculateSumCards(playerCurrentCardList)[0] > calculateSumCards(compCurrentCardList)[0]:

        printFinalScore()
        print("You have the higher score. You won the Game")

      else: 
        printFinalScore()
        print("The Computer has a higher Score. You lost the game")


      drawingCards = False

  
      