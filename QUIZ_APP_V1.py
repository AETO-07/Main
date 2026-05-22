import random
quizBank = [
     {
        "question": "Calculate 2 + 2",
        "options": ["3", "4", "7", "6"],
        "answer": "4"
    },
    {
        "question": "What is the capital of Nigeria?",
        "options": ["Lagos", "Ekiti", "Abuja", "Kano"],
        "answer": "Abuja"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "CO2", "NaCl", "O2"],
        "answer": "H2O"
    },
    {
        "question": "Who is the current president of the United States?",
        "options": ["Joe Biden", "Donald Trump", "Barack Obama", "George Bush"],
        "answer": "Donald Trump"
    },
    {
        "question": "5 * 3 = ?",
        "options": ["15", "10", "20", "8"],
        "answer": "15"
    }
]

with open("highScore.txt", "r") as file:
    high_score = int(file.read())

print(f"Current High Score: {high_score} \n")


while True:
    random.shuffle(quizBank)
    score = 0

    for question in quizBank:
        random.shuffle(question["options"])

        print(question["question"])

        for index, option in enumerate(question["options"]):
            print(f"{index}: {option}")

        while True:

            try:
                user_answer = int(input("Enter option number: "))
                if(user_answer < 0 or 
                    user_answer >= len(question["options"])):
                    print("Invalid option!")
                    continue
        
                break
            
            except ValueError:
                print("Please enter a number!")
        selected_option = question["options"][user_answer]
        if selected_option == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"\nFinal Score: {score}/{len(quizBank)}")

    if score > high_score:
        with open("highScore.txt", "w") as file:
            file.write(str(score))
            print("New High Score")

    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print("Goodbye!")

        break
