# MQ component 6 - implement round / question mechanics


# integer checking function
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


# main routine


questions = int_check("How many questions would you like to answer? ", 1)
print()

questions_answered = 0

while questions_answered != questions:

    heading = "Question {} of {}".format(questions_answered + 1, questions)
    print(heading)
    questions_answered += 1
    
    equation = "2 + 2 = 4"
    print(equation)
    print()

    true_false = input("True or false? ")

    if true_false == "true":
        print("correct")
        continue
    elif true_false == "false":
        print("wrong")
        continue