from translation import translate_text
from data import questions
import random

def quiz(language):
    #we first need an list of 10 random indexes for the questions
    questionsIndex = []
    for i in range (10) :
        randomNumber = random.randint(0,39)

        #if we have a duplicate find a new random number
        while randomNumber in questionsIndex:
            randomNumber = random.randint(0,39)

        if randomNumber not in questionsIndex:
            questionsIndex.append(randomNumber)


    index = 0

    #2 lists that will hold user answers and correct answers
    userAnswers = []
    correctAnswers = []

    for j in questionsIndex:
        #displaying the question to the user
        print(str(index + 1) + str(". ") + questions[j]['questionToUser'])

        #displaying the answer choices
        for i in range (len(questions[j]['choices'])):
            print("\t" + str(chr(97 + i)) + str(". ") + translate_text(questions[j]['choices'][i],"en-US" , language))
        
        userAnswer = input("Enter your answer: ")

        #grab the correct answer
        correctAnswer = questions[j]["answer"]

        #find the index of where the correct answer is
        correctIndex = questions[j]['choices'].index(correctAnswer)

        #based on what the index is, add 'a' to do to find its corresponding letter
        correctLetter = chr(97 + correctIndex)

        #add what the user enter and the correct answer to their respective lists
        userAnswers.append(userAnswer)
        correctAnswers.append(correctLetter)

        index = index + 1

    return userAnswers, correctAnswers, language
    #evaluate_quiz(userAnswers, correctAnswers, language)
    

