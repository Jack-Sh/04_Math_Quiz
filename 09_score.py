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


questions_answered = 0
questions = 10

true_false_list = ["true", "false"]

question_heading = "Question {} of {}".format(questions_answered + 1, questions)
print(question_heading)
print()
questions_answered += 1

while questions_answered != questions:

    question = "1 + 1 = 2"
    print(question)
    answer = "true"

    user_choice = choice_checker("True or False? ", true_false_list, "(T or F)")

    if user_choice == answer:
        print("Correct")
    else:
        print("Incorrect")
    print()