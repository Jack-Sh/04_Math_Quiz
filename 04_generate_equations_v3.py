# MQ component 4 v3 - generate equations randomly with numbers for questions

import random

# list of equation types
statement_list = ["addition", "subtraction", "multiplication", "greater_lesser"]

# set variables to make testing easier
lowest = 1
highest = 10

# pre-set statement for testing purposes (would usaully be random)\
for item in range(1, 10):
    statement = random.choice(statement_list)

    # prints 10 equations

    # if the statement has been randomly chosen as additon then...
    # generate two random numbers between the users choosen range
    # output the equation with correct answer
    if statement == "addition":
        num_1 = random.randint(lowest, highest)
        num_2 = random.randint(lowest, highest)
        answer = int(num_1 + num_2)
        question = "{} + {} = {}".format(num_1, num_2, answer)

    elif statement == "subtraction":
        num_1 = random.randint(lowest, highest)
        num_2 = random.randint(lowest, highest)
        answer = int(num_1 - num_2)
        question = "{} - {} = {}".format(num_1, num_2, answer)

    elif statement == "multiplication":
        num_1 = random.randint(lowest, highest)
        num_2 = random.randint(lowest, highest)
        answer = int(num_1 * num_2)
        question = "{} x {} = {}".format(num_1, num_2, answer)

    else:
        num_1 = random.randint(lowest, highest)
        num_2 = random.randint(lowest, highest)
        chosen_num = random.randint(1,2)
        if chosen_num == 1:
            question = "{} > {}".format(num_1, num_2)

        else:
            question = "{} < {}".format(num_1, num_2)

    print(question)