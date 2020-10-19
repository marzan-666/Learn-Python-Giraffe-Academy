from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Black\n(b) Red\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Blue\n(b) Red\n(c) Green\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print("Your Score is " + str(score) + "/" + str(len(questions))+ " Correct")

run_test(questions)
