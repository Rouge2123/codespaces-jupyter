# Create a Magic 8 Ball 

import random

name = input("What is your name? ")
question = input("What is your question? Keep in mind that I can only answer yes or no questions. ")

answer = ""

random_number = random.randint(1, 9)
# print(random_number)

if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"
    
if name == "" and question == "":
    print("I can't read your mind")
elif name == "":
    print("Question:", question)
    print("Magic 8-Ball's answer:", answer)
elif question == "":
    print(name + ", I didn't quite catch that - please try again")
else:
    print(name, "asks:", question)
    print("Magic 8-Ball's answer:", answer)

