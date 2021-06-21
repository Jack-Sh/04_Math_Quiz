import random


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


true_false_list = ["true", "false"]
lowest = 1
highest = 10
statement = "greater_lesser"
endgame = "no"

while endgame != "yes":

    chosen_num = random.randint(lowest, highest)
    num_1 = random.randint(lowest, highest)
    num_2 = random.randint(lowest, highest)

    if statement == "greater_lesser":
        if chosen_num == 1:

            question = "{} > {}".format(num_1, num_2)

        else:

            question = "{} < {}".format(num_1, num_2)

        print(question)
        correct_answer = eval(question)
        
        if correct_answer == True:
            answer = "true"
        else:
            answer = "false"

    true_false = choice_checker("Is this equation True or False? ", true_false_list, "Please enter true or false")

    if true_false == answer:
        print("CORRECT")
    else:
        print("INCORRECT")