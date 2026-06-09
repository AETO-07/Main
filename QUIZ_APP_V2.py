import random
import tkinter as tk

window = tk.Tk()
window.title("QUIZ APP V2")
window.geometry("500x400")

question_label = tk.Label(
    window,
    text="Question goes here",
    font=("Arial", 18),
    wraplength=400
)
question_label.pack(pady=20)

option_buttons = []

for i in range(4):
    btn = tk.Button(
        window, 
        text="Options",
        width=20,
        font=("Arial", 14)
    )
    btn.pack(pady=5)
    option_buttons.append(btn)


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


current_question = 0
score = 0

progress_label = tk.Label(
    window,
    text = "",
    font = ("Arial", 12)
)

def showQuestion():
    show = quizBank[current_question]
    question_label.config(
        text=show["question"]
    )
    progress_label.config(
        text=f"Question {current_question + 1} of {len(quizBank)}"
    )

    for index, button in enumerate(option_buttons):
        button.config(
            bg="SystemButtonFace",
            fg="black",
            text=show["options"][index],
            command=lambda position=index, btn=button: check_answer(show["options"][position], btn)
        )
    restart_button.pack_forget()

    

def check_answer(selected_option, clicked_btn):
    global score
    global current_question

    correct_answer = quizBank[current_question]["answer"]
    if selected_option == correct_answer:
        clicked_btn.config(bg="green", fg="white")
        score += 1
    else:
        clicked_btn.config(bg="red", fg="white")
        for b in option_buttons:
            if b["text"] == correct_answer:
                b.config(bg="green", fg="white")
                break

    for b in option_buttons:
        b.config(state="disabled")

    def _advance():
        global current_question
        current_question += 1
        if current_question < len(quizBank):
            for b in option_buttons:
                b.config(state="normal")
            showQuestion()
        else:
            question_label.config(text=f"Final Score: {score}/{len(quizBank)}")
            restart_button.pack(pady=20)
            for button in option_buttons:
                button.pack_forget()

    window.after(800, _advance)

 

def restart_quiz():
    global current_question, score
    current_question = 0
    score = 0
    question_label.pack(pady=20)
    question_label.config(text="")
    for btn in option_buttons:
        btn.pack(pady=5)
        btn.config(state="normal")
    
    showQuestion()

restart_button = tk.Button(
            window,
            text = "Restart Quiz",
            font = ("Arial", 14),
            command = restart_quiz
                )
restart_button.pack(pady=20)

with open("highScore.txt", "r") as file:
    high_score = int(file.read())

#print(f"Current High Score: {high_score} \n")


showQuestion()
window.mainloop()