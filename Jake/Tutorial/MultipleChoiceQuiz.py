from QnA import Question
question_prompts = [
    "Who was the most recent DOR?\n(a) BIG RIC\n(b) Drago\n(c)BM 3 Pettyjohn\n\n",
    "Who is the anchor cadet?\n(a) Tranny\n(b) Barbee\n(c) Davis\n\n",
    "Who was the latest mast?\n(a) Davis\n(b) Allen\n(c) Tranny\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("you got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)