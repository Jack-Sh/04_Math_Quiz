# MQ component 4 v1 - generate equations for questions

import random

statement_list = ["addition", "subtraction", "multiplication", "greater_lesser"]

for item in range(1, 20):
    statement = random.choice(statement_list)
    print(statement, end="\t")