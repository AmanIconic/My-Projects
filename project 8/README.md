# 🤖 AI Chatbot (File-Powered) using Python & CustomTkinter

A simple keyword-based chatbot with a modern GUI using [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter). It loads responses from a local JSON file and provides a clean, user-friendly interface.

---

## 📸 Preview

![Chatbot Screenshot](preview.png) <!-- Replace with actual screenshot file if available -->

---

## 🧠 Features

- 📁 File-powered: Loads responses from `responses.json`
- 🌓 Dark mode with customizable themes
- 🖱️ User-friendly interface with entry box and scrollable chat log
- 📄 Easy to extend or modify keyword-response logic

---

## 🛠️ Technologies Used

- Python 3.x
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- JSON for storing responses

---

## ▶️ How to Run
## Install dependencies
```
pip install customtkinter
```

## Run the script
```
Project_8_(Chat_Bot).py
```

---

## 🧠 How It Works
Takes user input from the GUI.

Converts the input to lowercase and checks for matching keywords in responses.json.

If a match is found, it displays the associated response.

If no match, displays a default fallback message.

---

## ✏️ Customization
You can add or modify keyword-response pairs in the responses.json file:
```
{
  "help": "Sure, I'm here to assist you!",
  "joke": "Why did the Python programmer go blind? Because he couldn’t C!"
}
```
---

## 🙋‍♂️ Author

Aman Yadav
