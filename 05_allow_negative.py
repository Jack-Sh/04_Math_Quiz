# MQ component 5 - ask user if they want to allow negatives in subtraction equations

import random


# Function to check if the user entered a valid answer (text)
def choice_checker(question, valid_list, error):
    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        else:
            print(error)


statement = "subtraction"
lowest = 1
highest = 10

# valid lists
yes_no_list = ["yes", "no"]

allow_negative = choice_checker("Do you want negatives in subtraction questions? ", yes_no_list, "Please enter yes or no ")

for item in range(1,10):

    # variable to choose between correct and incorrect answers (1 = correct, 2 = incorrect)
    chosen_num = random.randint(1,2)

    # generates two random numbers between lowest and highest
    num_1 = random.randint(lowest, highest)
    num_2 = random.randint(lowest, highest)

    if statement == "subtraction" and allow_negative == "yes":
        if chosen_num == 1:

            answer = int(num_1 - num_2)
        else:

            answer = random.randint(lowest, highest)
    
    elif statement == "subtraction" and 

    question = "{} - {} = {}".format(num_1, num_2, answer)

    print(question)
