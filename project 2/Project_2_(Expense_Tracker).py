import customtkinter as ctk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Expense Tracker")
app.geometry("500x650")
app.resizable(False, False)

DATA_FILE = "project 2/expenses.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense():
    try:
        amount = float(entry_amount.get())
        category = entry_category.get().strip()
        date = add_calendar.get_date().strftime("%Y-%m-%d")

        if not category:
            raise ValueError("Please fill all fields.")

        data = load_data()
        data.append({"amount": amount, "category": category, "date": date})
        save_data(data)
        messagebox.showinfo("Success", "Expense added successfully.")
        entry_amount.delete(0, ctk.END)
        entry_category.delete(0, ctk.END)
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def show_report(month):
    data = load_data()
    filtered = [d for d in data if d['date'].startswith(month)]
    if not filtered:
        messagebox.showinfo("Info", f"No data for {month}")
        return

    totals = defaultdict(float)
    for d in filtered:
        totals[d['category']] += d['amount']

    report_text = f"Expenses for {month}:\n"
    for cat, amt in totals.items():
        report_text += f"{cat}: ₹{amt:.2f}\n"

    messagebox.showinfo("Report", report_text)

def show_chart(month):
    data = load_data()
    filtered = [d for d in data if d['date'].startswith(month)]
    if not filtered:
        messagebox.showinfo("Info", f"No data for {month}")
        return

    totals = defaultdict(float)
    for d in filtered:
        totals[d['category']] += d['amount']

    categories = list(totals.keys())
    amounts = list(totals.values())

    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%")
    plt.title(f"Expense Distribution - {month}")
    plt.show()

def get_selected_month():
    selected_date = report_calendar.get_date()
    return selected_date.strftime("%Y-%m")


ctk.CTkLabel(app, text="Expense Tracker", font=("Arial Bold", 20)).pack(pady=15)

ctk.CTkLabel(app, text="Add Expense", font=("Arial", 20)).pack(pady=10)

entry_amount = ctk.CTkEntry(app, placeholder_text="Amount (e.g. 250)", width=300)
entry_amount.pack(pady=5)

entry_category = ctk.CTkEntry(app, placeholder_text="Category (e.g. Food)", width=300)
entry_category.pack(pady=5)

style = ttk.Style()
style.configure('my.DateEntry', arrowsize=20, font=('Arial', 20))
add_calendar = DateEntry(app, date_pattern="yyyy-mm-dd", width=20, font=("Arial", 20), style='my.DateEntry')
add_calendar.pack(pady=10)

ctk.CTkButton(app, text="Add Expense", command=add_expense).pack(pady=10)

ctk.CTkLabel(app, text="Monthly Report", font=("Arial Bold", 20)).pack(pady=15)

style = ttk.Style()
style.configure('my.DateEntry', arrowsize=20, font=('Arial', 20))

ctk.CTkLabel(app, text="Pick any date from the month", font=("Arial", 20)).pack(pady=(10, 0))
report_calendar = DateEntry(app, date_pattern="yyyy-mm-dd", width=20, font=("Arial", 20), style='my.DateEntry')
report_calendar.pack(pady=10)

ctk.CTkButton(app, text="Show Report", command=lambda: show_report(get_selected_month())).pack(pady=5)
ctk.CTkButton(app, text="Show Pie Chart", command=lambda: show_chart(get_selected_month())).pack(pady=5)

app.mainloop()
