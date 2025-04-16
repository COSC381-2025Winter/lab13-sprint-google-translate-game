from selectingQuizQuestions import quiz

def mainMenu():
    
    while(True):
        print("Welcome to the Translation Game")
        print("Language options: ")
        print("1. Korean")
        print("2. Spanish")
        print("3. Manderin")
        print("q: quit")
        choice = input("Enter a number to select a language: ")
        if choice == 'q':
            break
        choice = int (choice)
        if choice == 1:
            language = "ko"
        if choice == 2:
            language = "es"
        if choice == 3:
            language = "zh"
        quiz(language)