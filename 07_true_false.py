# MQ component 7 - ask user whether question is true or false
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


# Main routine


# valid lists
true_false_list = ["true", "false"]
end_game = "no"

equation = "addition"
lowest = 1
highest = 10

while end_game != "yes":

    num_1 = random.randint(lowest, highest)
    num_2 = random.randint(lowest, highest)
    chosen_num = random.randint(1, 2)

    if equation == "addition":
        correct_answer = int(num_1 + num_2)
        if chosen_num == 1:

            answer = int(num_1 + num_2)

        else:
            answer = random.randint(lowest, highest)

        question = "{} + {} = {}".format(num_1, num_2, answer)

    print(question)

    true_false = choice_checker("Is this equation True or False? ", true_false_list, "Please enter true or false")

    if chosen_num == 1:
        if true_false == "true":
            print("correct")

        else:
            print("incorrect")

    else:
        if true_false == "true" and answer == correct_answer:
            print("correct")

        elif true_false == "false":
            print("correct")

        else:
            print("incorrect")

