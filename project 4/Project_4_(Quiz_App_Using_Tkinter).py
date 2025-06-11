import customtkinter as ctk
import json
import os

json_path = os.path.join("project 4", "quiz_questions.json")
with open(json_path, "r") as f:
    questions = json.load(f)

total_questions = len(questions)
current_index = 0
user_answers = [""] * total_questions

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Quiz App")
app.geometry("600x550")

selected_answer = ctk.StringVar()


def load_question(index):
    selected_answer.set(user_answers[index])
    q = questions[index]
    question_label.configure(text=f"Q{index + 1}. {q['question']}")
    for i in range(4):
        option_buttons[i].configure(text=q["options"][i])
        if user_answers[index] == q["options"][i]:
            selected_answer.set(q["options"][i])

def save_answer():
    answer = selected_answer.get()
    if answer:
        user_answers[current_index] = answer

def next_question():
    global current_index
    save_answer()
    if current_index < total_questions - 1:
        current_index += 1
        load_question(current_index)

def prev_question():
    global current_index
    save_answer()
    if current_index > 0:
        current_index -= 1
        load_question(current_index)

def submit_quiz():
    save_answer()
    score = 0
    for i in range(total_questions):
        correct = questions[i]['answer'].strip().lower()
        given = user_answers[i].strip().lower()
        if given == correct:
            score += 1
    final_score_label.configure(text=f"Your Score: {score} / {total_questions}")


question_label = ctk.CTkLabel(app, text="", font=("Arial", 20), wraplength=550)
question_label.pack(pady=30)

option_buttons = []
for _ in range(4):
    btn = ctk.CTkRadioButton(app, text="", font=("Arial", 16), variable=selected_answer)
    btn.pack(anchor="w", padx=60, pady=5)
    option_buttons.append(btn)

nav_frame = ctk.CTkFrame(app)
nav_frame.pack(pady=20)

ctk.CTkButton(nav_frame, text="Previous", command=prev_question, width=120).pack(side="left", padx=20)
ctk.CTkButton(nav_frame, text="Next", command=next_question, width=120).pack(side="left", padx=20)

ctk.CTkButton(app, text="Submit", command=submit_quiz, width=250).pack(pady=10)
final_score_label = ctk.CTkLabel(app, text="", font=("Arial Bold", 18))
final_score_label.pack(pady=10)

load_question(current_index)

app.mainloop()

#Currently Working to correct the score board it is not working properly
