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


# Main Routine


# Valid lists
yes_no_list = ["yes", "no"]

# Ask the user if they have played before
played_before = "Have you played before? "
played_before_response = choice_checker(question=played_before,
                                        valid_list=yes_no_list,
                                        error="Please choose from yes or no")

# If user enters "no" print out instructions
if played_before_response == "no":
    instructions()