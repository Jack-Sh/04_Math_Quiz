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

# preset variable list
questions_answered = 0
questions = 5
questions_correct = 0
questions_incorrect = 0
quiz_summary = []

# valid lists
true_false_list = ["true", "false"]
yes_no_list = ["yes", "no"]

# start of quiz loop
while questions_answered != questions:

    # generates heading 
    question_heading = "Question {} of {}".format(questions_answered + 1, questions)

    # prints heading
    print(question_heading)
    print()

    # + 1 to question counter
    questions_answered += 1

    # preset question (for testing)
    question = "1 + 1 = 2"

    # prints question
    print(question)

    # sets answer to true
    answer = "true"

    # asks user whether the question is true or false
    user_choice = choice_checker("True or False? ", true_false_list, "(T or F)")

    # gives user feedback based on answer
    if user_choice == answer:
        print("Correct")
        questions_correct += 1

    else:
        print("Incorrect")
        questions_incorrect += 1

    outcome = "Question {}: {} your answer: {} | correct answer: {}".format(questions_answered, question, user_choice, answer)

    quiz_summary.append(outcome)

    print()

quiz_response = choice_checker("Do you want to see the quiz history? ", yes_no_list, "Please enter yes or no")

if quiz_response == "yes":
    print()
    print("=== Quiz History ===")
    for quiz in quiz_summary:
        print(quiz)