#Yuta Naito
#September 17, 2021
#Guessing Game

import random

my_listA = ("What is your favourite sport? ", "What is your favourite food? ", "If you could get any pet you want right now, what pet would you pick? ")

g = 2

user_response = input("Welcome to the guessing game. Today, player 2 will be guessing player 1's answers. Hit ENTER to start the game. ")
print("Player 1, here is your topic ")
user_response = input(random.choice(my_listA))
user_response = user_response.lower().strip(" <>:?/:;}]{[||+=_-!@#$%^&*()1234567890")

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
answer_response = input("Player 2, try and answer Player 1's answer! ")
answer_response = answer_response.lower().strip(" <>:?/:;}]{[||+=_-!@#$%^&*()1234567890")
for loop in range(g):
    if answer_response == user_response:
        user_response = user_response.lower().strip(" <>:?/:;}]{[||+=_-!@#$%^&*()1234567890")
        print("Great job! you got it right! Player 2 is the winner of this round.")
        print("\n")
        print("Player 2, here is your question:")
        break
    else:
        print("Incorrect! ")
        print(str(g) + " guesses left")
        g = g - 1
        response = input()
        if response == user_response:
            response = response.lower().strip(" <>:?/:;}]{[||+=_-!@#$%^&*()1234567890")
            print("Great job! you got it right!")
            print("\n")
            print("Player 2, here is your question:")
            break
        elif g == 0:
            print("Thats tough, you have no more guesses. Player 1 is the winner of this round. The correct answer was.... " + user_response + "!")
            print("\n")
            print("Player 2 here is your question:")
        

my_listB = ("What is your least favourite sport? ", "What is your least favourite food? ", "What is your favourite holiday? ")

g = 2

user_response = input(random.choice(my_listB))
user_response = user_response.lower().strip(" <>:?/:;}]{[||+=_-!@#$%^&*()1234567890")

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
answer_response = input("Player 2, try and guess Player 1's answer! ")
user_response = user_response.lower().strip(" <>:?/:;}]{[||+=_-!@#$%^&*()1234567890")
answer_response = answer_response.lower().strip(" <>:?/:;}]{[||+=_-!@#$%^&*()1234567890")
for loop in range(g):
    if answer_response == user_response:
        answer_response = answer_response.lower().strip(" <>:?/:;}]{[||+=_-!@#$%^&*()1234567890")
        print("Great job! you got it right! Player 1 is the winner of this round")
        print("\n")
        break
    else:
        print("Incorrect! ")
        print(str(g) + " guesses left")
        g = g - 1
        response = input()
        if response == user_response:
            response = response.lower().strip(" <>:?/:;}]{[||+=_-!@#$%^&*()1234567890")
            print("Great job! you got it right!")
            break
        elif g == 0:
            print("Thats tough, you have no more guesses. Player 2 is the winner of this round. The correct answer was.... " + user_response + "!")
            
print("\n")
print("Thats all for the game, if you would like to replay the game please hit the F5 key.")
        
    