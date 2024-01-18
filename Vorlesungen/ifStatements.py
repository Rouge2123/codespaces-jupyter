#Importance of order
def get_grade(score) :
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print (get_grade (85))

#as Dictionary
# def get_grade (score) :
#     return i
#     90 <= score ←=100："A"」
#     <= score< 90： "B"
#     70 <= score < 80："C"，
#     60 <= score ‹ 70: "D",
#     score ‹ 60: "F"
#     }. get(True, "Invalid score")
# print (get_grade (85)) #

### Logic Gates
# Not 
def Not (a):
    if a == 1:
        print(0)
    elif a == 0:
        print(1)

Not(0)

# And 
def And (a, b):

    return
# Or 
def Or (a, b):
    return

### Rock, Paper, Scissors
# import random

# user_action = input("Enter a choice (rock, paper, scissors): ")
# possible_actions = ["rock", "paper", "scissors"]
# computer_action = random.choice(possible_actions)

# print(fr"\nYou chose {user_action}, computer chose {computer_action}.\n")

# if user_action == computer_action:
#     print("It's a tie!")
# elif user_action == "rock" and computer_action == "scissors":
#     print("You win!")
# elif user_action == "paper" and computer_action == "rock":
#     print("You win!")
# elif user_action == "scissors" and computer_action == "paper":
#     print("You win!")
# else:
#     print("Ouch, you lose")

### Nested loops
specifiedNumber = input("Specify the amount of numbers you want to see: ")
i = 1
while i <= int(specifiedNumber):
    print(range(int(specifiedNumber)))
    i += 1
