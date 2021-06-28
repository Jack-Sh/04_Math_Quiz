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
    statement_generator("Math Quiz!", "=")
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
    statement_generator("Have Fun!", "=")


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


# Function to print five symbols on either side of specified statements
def statement_generator(statement, decoration):

    sides = decoration * 5
    statement = "{} {} {}".format(sides, statement, sides)

    print(statement)

    return ""


# Main Routine

questions_answered = 0
questions_correct = 0
questions_incorrect = 0

# Valid lists
yes_no_list = ["yes", "no"]
symbol_list = ["+", "-", "*", "<", ">", "=="]
true_false_list = ["true", "false"]
quiz_summary = []

# Ask the user if they have played before
played_before = "Have you played before? "
played_before_response = choice_checker(question=played_before,
                                        valid_list=yes_no_list,
                                        error="Please choose from yes or no")

# If user enters "no" print out instructions
if played_before_response == "no":
    instructions()

# Asks for lowest and highest aswell as checking that their valid
print()
print("----------------")
lowest = int_check("Lowest Number: ")
highest = int_check("Highest Number: ", lowest + 1)
print("----------------")
print()
# Ask user if they want to allow negatives in subtraction questions
allow_negative = choice_checker("Do you want negatives in subtraction questions? ", yes_no_list, "Please enter yes or no ")

# Ask for number of questions
print()
questions = int_check("How many questions would you like to answer? ", 1)

# start of game loop
while questions_answered != questions:

    # generates and prints heading before every question
    heading = "Question {} of {}".format(questions_answered + 1, questions)
    print()
    statement_generator(heading, "-")
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
            answer = eval(num_question)
            tf_answer = "true"

        # generate a random incorrect answer and define answer as false
        else:
            correct_answer = eval(num_question)
            answer = random.randint(lowest, highest)

            # if the randomly generated answer is the correct answer
            # the answer = true
            if answer == correct_answer:
                tf_answer = "true"

            # otherwise the answer is false
            else:
                tf_answer = "false"

    # greater, lesser, equals questions
    else:
        
        # evaluate the correct answer (true or false)
        answer = eval(num_question)

        # define answer based on the num_question
        if answer == True:
            tf_answer = "true"

        else:
            tf_answer = "false"

    # different question outputs

    # multiplication question
    if symbol == "*":
        question = "{} x {} = {}".format(num_1, num_2, answer)

    # add, sub questions
    elif symbol == "+" or symbol == "-":
        question = "{} {} {} = {}".format(num_1, symbol, num_2, answer)

    # greater, lesser, equals questions
    else:
        question = "{} {} {}".format(num_1, symbol, num_2)

    # prints randomly generated question
    statement_generator(question, "*")

    # asks user whether the question is true or false
    user_choice = choice_checker("Is this equation True or False? ", true_false_list, "Please enter true or false (T or F)")

    # gives feedback to user based on their answer
    if user_choice == tf_answer:
        statement_generator("Correct", "=")
        questions_correct += 1

    else:
        statement_generator("Incorrect", "~")
        questions_incorrect += 1

    # generates outcome format for quiz history
    outcome = "Question {}: {} your answer: {} | correct answer: {}".format(questions_answered, question, user_choice, tf_answer)

    # arranges all outcomes in a list
    quiz_summary.append(outcome)

# generates score and prints output
print()
statement_generator("Score", "-")
score = "      {} / {}".format(questions_correct, questions)
print(score)
print()

# calculates quiz stats
percent_correct = questions_correct / questions * 100
percent_incorrect = questions_incorrect / questions * 100

# generate stats and prints output
statement_generator("Statistics", "-")
stats = "Correct - {:.0f}%  |  Incorrect - {:.0f}%".format(percent_correct, percent_incorrect)
print(stats)

# asks user whether they want to see their quiz history
print()
quiz_response = choice_checker("Do you want to see the quiz history? ", yes_no_list, "Please enter yes or no")

# if they do then print the history in a list
if quiz_response == "yes":
    print()
    statement_generator("Quiz History", "-")
    for quiz in quiz_summary:
        print(quiz)