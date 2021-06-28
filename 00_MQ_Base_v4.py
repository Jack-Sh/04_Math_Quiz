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
    print("The quiz will then begin, for each question you will be given a math related question")
    print("It could be multiplication, addition, subtraction or greater / lesser / equals")
    print("For each prompt you will be asked, is this statement True or False? (you can type T, F aswell)")
    print("For example. Question 1: 2 + 2 = 4 is this true or false: True")
    print()
    print("At the end you will be given a score and be asked if you want to see your quiz history")
    print("'Quiz History' is a more in depth look rather than just getting a standard out of 10 score")
    print()
    print("Have Fun!")
    print()


# Function to check integers
def int_check(question, low=None,):

    situation = ""

    # If user has only specified a low number
    # (eg. when entering high number)
    # set situation to 'low only'
    if low is not None:
        situation = "low only"

    while True:

        response = input(question).lower()

        try:
            response = int(response)

            # checks input is not too low
            if situation == "low only":
                if response < low:
                    print("Please enter a number that is more than (or equal to) {}".format(low))
                    continue

            return response

        # checks input is an integer
        except ValueError:
            print("Please enter an integer")
            continue


# Main Routine

questions_answered = 0
questions_correct = 0
questions_incorrect = 0

# Valid lists
yes_no_list = ["yes", "no"]
symbol_list = ["+", "-", "*", "<", ">", "=="]
true_false_list = ["true", "false"]

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

# start of game loop
while questions_answered != questions:

    # generates and prints heading before every question
    heading = "Question {} of {}".format(questions_answered + 1, questions)
    print()
    print(heading)
    print()

    # add one to question counter
    questions_answered += 1

    # generates a random symbol for each question
    symbol = random.choice(symbol_list)

    # variable to choose between correct and incorrect answers (1 = correct, 2 = incorrect)
    chosen_num = random.randint(1, 2)

    # if the user doesn't want negatives for subtraction generate two numbers but ensure
    # that the first number is greater than the second
    if symbol == "-" and allow_negative == "no":
        num_2 = random.randint(lowest, highest)
        num_1 = random.randint(num_2, highest)

    # generates two random numbers between lowest and highest
    else:
        num_1 = random.randint(lowest, highest)
        num_2 = random.randint(lowest, highest)

    # changes the symbol to '==' if the generated numbers are the same and
    # the symbol is either '<' or '>'
    if symbol == "<" or symbol == ">" and num_1 == num_2:
        symbol = "=="

    # generate the correct equation (non printed format)
    num_question = "{} {} {}".format(num_1, symbol, num_2)

    # add, sub, mult questions
    if symbol == "+" or symbol == "-" or symbol == "*":

        # generate the answer if the randomly generated number is 1 and define answer as true
        if chosen_num == 1:
            correct_answer = eval(num_question)
            answer = "true"

        # generate a random incorrect answer and define answer as false
        else:
            correct_answer = random.randint(lowest, highest)
            answer = "false"

    # greater, lesser, equals questions
    else:
        
        # evaluate the correct answer (true or false)
        correct_answer = eval(num_question)

        # define answer based on the num_question
        if correct_answer == True:
            answer = "true"

        else:
            answer = "false"  

    # different question outputs

    # multiplication question
    if symbol == "*":
        question = "{} x {} = {}".format(num_1, num_2, correct_answer)

    # add, sub questions
    elif symbol == "+" or symbol == "-":
        question = "{} {} {} = {}".format(num_1, symbol, num_2, correct_answer)

    # greater, lesser, equals questions
    else:
        question = "{} {} {}".format(num_1, symbol, num_2)

    # prints randomly generated question
    print(question)

    # asks user whether the question is true or false
    user_choice = choice_checker("Is this equation True or False? ", true_false_list, "Please enter true or false (T or F)")

    # gives feedback to user based on their answer
    if user_choice == answer:
        print("Correct")
        questions_correct += 1

    else:
        print("Incorrect")
        questions_incorrect += 1

# generates score and prints output
print()
print("|--- SCORE ---|")
score = "     {} / {}".format(questions_correct, questions)
print(score)
print()

# caculates quiz stats
percent_correct = questions_correct / questions * 100
percent_incorrect = questions_incorrect / questions * 100

# generate stats and prints output
print("|----------   STATS   ----------|")
stats = "Correct - {:.0f}%  |  Incorrect - {:.0f}%".format(percent_correct, percent_incorrect)
print(stats)