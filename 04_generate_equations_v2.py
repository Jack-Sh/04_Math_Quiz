# MQ component 4 v2 - generate addition equations with numbers for questions

import random

# list of equation types
statement_list = ["addition", "subtraction", "multiplication", "greater_lesser"]

# set variables to make testing easier
lowest = 1
highest = 10

# pre-set statement for testing purposes (would usaully be random)
statement = "addition"

# prints 10 equations
for item in range(1, 10):

    # if the statement has been randomly chosen as additon then...
    # generate two random numbers between the users choosen range
    # output the equation with correct answer
    if statement == "addition":
        num_1 = random.randint(lowest, highest)
        num_2 = random.randint(lowest, highest)
        answer = int(num_1 + num_2)
        question = "{} + {} = {}".format(num_1, num_2, answer)
        print(question)