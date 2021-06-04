# MQ component 4 v5 - generate equations randomly with random answers and random numbers for questions (simplified)

import random

# list of equation types
statement_list = ["addition", "subtraction", "multiplication", "greater_lesser"]

# set variables to make testing easier
lowest = 1
highest = 10

# generates random statement
# prints 10 equations
for item in range(1, 10):
    statement = random.choice(statement_list)

    # variable to choose between correct and incorrect answers (1 = correct, 2 = incorrect)
    chosen_num = random.randint(1,2)

    # generates two random numbers between lowest and highest
    num_1 = random.randint(lowest, highest)
    num_2 = random.randint(lowest, highest)

    # based off of the randomly chosen statement 
    # output the equation with correct answer or an incorrect answer
    if statement == "addition":
        if chosen_num == 1:

            answer = int(num_1 + num_2)
        else:
            answer = random.randint(lowest, highest)

        question = "{} + {} = {}".format(num_1, num_2, answer)

    elif statement == "subtraction":
        if chosen_num == 1:

            answer = int(num_1 - num_2)
        else:

            answer = random.randint(lowest, highest)

        question = "{} - {} = {}".format(num_1, num_2, answer)

    elif statement == "multiplication":
        if chosen_num == 1:

            answer = int(num_1 * num_2)
        else:

            answer = random.randint(lowest, highest)

        question = "{} x {} = {}".format(num_1, num_2, answer)

    else:
        if chosen_num == 1:

            question = "{} > {}".format(num_1, num_2)

        else:

            question = "{} < {}".format(num_1, num_2)

    print(question)