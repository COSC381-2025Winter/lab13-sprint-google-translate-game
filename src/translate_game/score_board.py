from main import translate_text

def evaluate_quiz(user_answers, questions):
    """
    user_answers: list of user input strings
    questions: list of dicts with 'foreign' and 'answer'
    """
    score = 0
    incorrect = []

    for i, q in enumerate(questions):
        correct_answer = q['answer'].lower()
        user_answer = user_answers[i].strip().lower()
        if user_answer == correct_answer:
            score += 1
        else:
            incorrect.append(q['foreign'])

    print(f"\nYou scored {score} out of {len(questions)}!")

    # Grade
    percentage = score / len(questions) * 100
    if score >= 9:
        grade = "A"
    elif score >= 7:
        grade = "B"
    else:
        grade = "C"
    print(f"Grade: {grade} ({percentage:.1f}%)")

    # Show translations for incorrect answers
    if incorrect:
        print("\nReview your incorrect answers (Google Translate):")
        for sentence in incorrect:
            print(f"\nFrench: {sentence}")
            response = translate_text(sentence, "fr", "en")
            for t in response.translations:
                print(f"Google Translate: {t.translated_text}")
