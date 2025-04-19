from translation import translate_text
from menu import mainMenu
from selectingQuizQuestions import quiz
from score_board import evaluate_quiz

def main():
    while True:
        language = mainMenu()

        if language == 'q':
            break
        else:
            userAnswers, correctAnswers, language = quiz(language)
            evaluate_quiz(userAnswers, correctAnswers, language)
main()