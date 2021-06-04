# MQ component 4 v4 - generate equations randomly with random answers and random numbers for questions

import random

# list of equation types
statement_list = ["addition", "subtraction", "multiplication", "greater_lesser"]

# set variables to make testing easier
lowest = 1
highest = 10

# pre-set statement for testing purposes (would usaully be random)\
for item in range(1, 10):
    statement = random.choice(statement_list)
    chosen_num = random.randint(1,2)
    # prints 10 equations

    # if the statement has been randomly chosen as additon then...
    # generate two random numbers between the users choosen range
    # output the equation with correct answer or an incorrect answer
    if statement == "addition":
        num_1 = random.randint(lowest, highest)
        num_2 = random.randint(lowest, highest)
        if chosen_num == 1:
            answer = int(num_1 + num_2)
        else:
            answer = random.randint(lowest, highest)

        question = "{} + {} = {}".format(num_1, num_2, answer)

    # if the statement has been randomly chosen as subtraction then...
    # generate two random numbers between the users choosen range
    # output the equation with correct answer or an incorrect answer
    elif statement == "subtraction":
        num_1 = random.randint(lowest, highest)
        num_2 = random.randint(lowest, highest)
        if chosen_num == 1:
            answer = int(num_1 - num_2)
        else:
            answer = random.randint(lowest, highest)

        question = "{} - {} = {}".format(num_1, num_2, answer)

    # if the statement has been randomly chosen as multiplication then...
    # generate two random numbers between the users choosen range
    # output the equation with correct answer or an incorrect answer
    elif statement == "multiplication":
        num_1 = random.randint(lowest, highest)
        num_2 = random.randint(lowest, highest)
        if chosen_num == 1:
            answer = int(num_1 * num_2)
        else:
            answer = random.randint(lowest, highest)
        question = "{} x {} = {}".format(num_1, num_2, answer)

    # if the statement has been randomly chosen as greater lesser then...
    # generate two random numbers between the users choosen range
    # output the equation with correct answer or an incorrect answer
    else:
        num_1 = random.randint(lowest, highest)
        num_2 = random.randint(lowest, highest)
        if chosen_num == 1:
            question = "{} > {}".format(num_1, num_2)

        else:
            question = "{} < {}".format(num_1, num_2)

    print(question)