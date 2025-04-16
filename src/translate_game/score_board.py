from translation import translate_text

def evaluate_quiz(user_answers, correct_answers, language):
    """
    user_answers: list of user input strings
    questions: list of dicts with 'foreign' and 'answer'
    """
    score = 0
    incorrect = []

    for i in range(len(user_answers)):
        user_answer = user_answers[i].strip().lower()
        correct_answer = correct_answers[i].strip().lower()
        if user_answer == correct_answer:
            score += 1
        else:
            # store index and correct answer for feedback
            incorrect.append((i + 1, correct_answers[i]))

    print(f"\nYou scored {score} out of {len(correct_answers)}!")

    percentage = score / len(correct_answers) * 100
    if score >= 9:
        grade = "A"
    elif score >= 7:
        grade = "B"
    else:
        grade = "C"
    print(f"Grade: {grade} ({percentage:.1f}%)")

    if incorrect:
        print("\nReview your incorrect answers:")
        for num, correct in incorrect:
            print(f"\nWrong number: {num}")
            translated = translate_text(str(correct), language, "en")
            print(f"Google Translate: {translated}")

