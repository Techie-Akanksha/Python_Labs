questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Which language are we learning?",
        "options": ["Python", "Java", "C++", "HTML"],
        "answer": "Python"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["6", "7", "8", "9"],
        "answer": "8"
    }
]

score = 0

for question in questions:
    print(question["question"])

    for option in question["options"]:
        print(option)

    user_answer = input("Your answer: ")

    if user_answer.lower() == question["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Your score:", score, "/", len(questions))