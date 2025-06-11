import customtkinter as ctk
import json

with open("project 8/responses.json", "r") as file:
    responses = json.load(file)

def get_response(user_input):
    msg = user_input.lower()
    for keyword in responses:
        if keyword in msg:
            return responses[keyword]
    return "Sorry, I didn't understand that. Can you please rephrase?"

def send_message():
    user_input = entry.get().strip()
    if user_input == "":
        return
    chatbox.configure(state="normal")
    chatbox.insert("end", f"You: {user_input}\n")
    entry.delete(0, ctk.END)

    bot_reply = get_response(user_input)
    chatbox.insert("end", f"Bot: {bot_reply}\n\n")
    chatbox.configure(state="disabled")
    chatbox.see("end")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("AI Chatbot (File-Powered)")
app.geometry("500x600")

chatbox = ctk.CTkTextbox(app, width=480, height=450, font=("Arial", 14), state="disabled")
chatbox.pack(pady=10)

entry = ctk.CTkEntry(app, width=400, placeholder_text="Type your message...", font=("Arial", 14))
entry.pack(pady=5)

send_btn = ctk.CTkButton(app, text="Send", command=send_message)
send_btn.pack()

app.mainloop()
