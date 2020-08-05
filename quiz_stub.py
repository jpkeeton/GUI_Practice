# taken from https://www.mikedane.com/programming-languages/python/building-a-quiz/

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b)Orange",
#     "What color are bananas?\n(a) Red/Green\n(b)Yellow",
# ]

qa_question_prompts = [
    "What is a bug?\n(a) a feature\n(b) a problem"
    # "What color are bananas?\n(a) Red/Green\n(b)Yellow",
]


questions = [
    Question(qa_question_prompts[0], "a")
    # Question(qa_question_prompts[1], "b"),
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got ", score, "/", len(questions))


run_quiz(questions)