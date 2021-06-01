# MQ component 2 - ask user for lowest number and highest number


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


# main routine


# asks for lowest and highest aswell as checking that their valid
lowest = int_check("Lowest Number: ")
highest = int_check("Highest Number: ", lowest + 1)
