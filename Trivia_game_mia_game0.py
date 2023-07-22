import string
import sys

import FamilyGuy as fam
import random

question_number = 0
randomIndex = 0
count = 0
correct = 0
userAnswer = ''


def game_part_0(): #user wants to start the game
    global question_number
    question_number += 1
    return game_part_2()




def game_part_1():# exit from game
    global question_number
    global randomIndex
    global count
    global correct

    question_number = 0
    randomIndex = 0
    count = 0
    correct = 0

    return "\n" +"Come back later to play the game."





def game_part_2():#game questions
    global randomIndex

    if question_number <11:
        while randomIndex in fam.check:
            randomIndex = int(random.random() * len(fam.family))
        #randomIndex = int(random.random() * len(fam.family))

        if randomIndex not in fam.check:
            fam.check.append(randomIndex)

            question = fam.family[randomIndex]
            options = fam.famians[randomIndex]

            return "\n" +str(question_number) +") " +question + "\n\n" +options
        else:
            return "There is an issue. \nContact coorayeronnemanohsawoodapple@gmail.com to report the bug."


def game_part_3(result):#game answers
    global correct
    global count
    global userAnswer

    userAnswer = result.lower()
    # userAnswer = userAnswerl.translate({ord(c): None for c in string.whitespace})
    count = count + 1

    next_response_request = "Are you ready for the next question, if so type yes otherwise type exit to quit the game."

    if (userAnswer == fam.answers[randomIndex]):
        correct = correct + 1
        return 'Your answer is correct\n' +next_response_request

    else:
        return ('Your answer is wrong. \nThe correct answer is: ' +fam.answers[randomIndex]) +"\n" +next_response_request

def game_part_4():#game result
        global correct
        global count
        score = game_part_6(correct, count)
        finalize_message = game_part_1()
        return 'Your performance\n' +score + "\n" + finalize_message



def game_part_6(x, y):#to find score

    try:
        marks = (x / y) * 100
    except ZeroDivisionError:
        marks = 0

    if marks > 90:
        return ("You are a diehard fan of family Guy \n score: " +str(marks) +"%")
    elif marks >= 75:
        return ("You scored well \n score: " +str(marks) +"%")
    elif marks >= 50:
        return ("Compleate all the seasons and come back \n score: " +str(marks) +"%")
    elif marks >= 25:
        return ("You are not a fan of Family Guy \n score: " +str(marks) +"%")
    else:
        return ("Haven't you watched a one single episode? \n score: " +str(marks) +"%")

#z = game_part_6(10, 2)
#print(z)