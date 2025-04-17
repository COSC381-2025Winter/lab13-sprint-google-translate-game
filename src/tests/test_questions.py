import pytest
from translate_game.data import questions

#check if every question has an answer, answer choices, and the correct answer
def test_all_questions_have_required_keys():
    for q in questions:
        assert "answer" in q
        assert "choices" in q
        assert "questionToUser" in q

#check to see that every question has the answer in the answer choices
def test_answers_are_in_choices():
    for q in questions:
        assert q["answer"] in q["choices"]

#make sure each question only has 4 answer choices, I am running out of ideas
def test_choices_length():
    for q in questions:
        assert len(q["choices"]) == 4

#testing a random question to make sure its grabbing the correct details
def test_question_1_data():
    q = questions[1]  

    assert q["answer"] == "dog"
    assert "dog" in q["choices"]
    assert sorted(q["choices"]) == sorted(["cat", "elephant", "dog", "lizard"])
    assert q["questionToUser"] == "Translate the word dog"
    assert len(q["choices"]) == 4

