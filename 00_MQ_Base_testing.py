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


# Function to display instructions when called
def instructions():
    print()
    print("Math Quiz!")
    print()
    print("First you will be asked to choose a number range (this can include negative numbers)")
    print("This determines the difficulty of the quiz")
    print()
    print("Next you will be asked to pick a number of questions")
    print()
    print("The quiz will then begin for each question you will be given a math related question")
    print("It could be multiplication, addition, subtraction or greater, lesser")
    print("For each prompt you will be asked to is this statement True or False (or T, F)")
    print("For example. Question 1: 2+2=4 is this true or false: True")
    print()
    print("At the end you will be given a score and be asked if you want to see your quiz history")
    print("This is a more in depth look rather than just getting a standard out of 10 score")
    print()
    print("Have Fun!")
    print()


# Function to check integers
def int_check(question, low=None, high=None, exit_code=None):

    situation = ""

    # If user has specified a low and a high
    # number (eg. when guessing)
    # set the situation to 'both'
    if low is not None and high is not None:
        situation = "both"

    # If user has only specified a low number
    # (eg. when enetering high number)
    # set situation to 'low only'
    elif low is not None and high is None:
        situation = "low only"

    while True:

        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            # checks input is not too high or
            # too low if both upper and lower bounds
            # are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between {} and {}".format(low, high))
                    continue

            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is more than (or equal to) {}".format(low))
                    continue

            return response

        # checks input is an integer
        except ValueError:
            print("Please enter an integer")
            continue


# Main Routine


# Valid lists
yes_no_list = ["yes", "no"]
statement_list = ["addition", "subtraction", "multiplication", "greater_lesser"]


# Ask the user if they have played before
played_before = "Have you played before? "
played_before_response = choice_checker(question=played_before,
                                        valid_list=yes_no_list,
                                        error="Please choose from yes or no")

# If user enters "no" print out instructions
if played_before_response == "no":
    instructions()

# Asks for lowest and highest aswell as checking that their valid
lowest = int_check("Lowest Number: ")
highest = int_check("Highest Number: ", lowest + 1)

# Ask user if they want to allow negatives in subtraction questions
allow_negative = choice_checker("Do you want negatives in subtraction questions? ", yes_no_list, "Please enter yes or no ")

# Ask for number of questions
questions = int_check("How many questions would you like to answer? ", 1)

statement = random.choice(statement_list)

# variable to choose between correct and incorrect answers (1 = correct, 2 = incorrect)
chosen_num = random.randint(1, 2)

# generates two random numbers between lowest and highest
if statement == "subtraction" and allow_negative == "no":
    num_2 = random.randint(lowest, highest)
    num_1 = random.randint(num_2, highest)

else:
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

