questions = [
    {
        "question": "What is the capital of Nepal",
        "answer":"Kathmandu"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "mars"
    },
    {
        "question": "Who is known as the Father of Computer?",
        "answer": "charles babbage"
    },
    {
        "question": "Which language is used for web page styling?",
        "answer": "css"
    },
    {
         "question": "What is the national flower of Nepal?",
        "answer": "rhododendron"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "answer": "def"
    }
]
score=0
print("Welcome to the Quiz Game...")
for q in questions:
   print("\n"+ q["question"])
   user_answer=input("Enter your answer:").lower()
   if user_answer==q["answer"]:
    print("correct answer")
    score +=1
   else:
    print("Wrong answer !")
print("Quiz game Completed....")
print(f"your final score is {score}/{len(questions)}")