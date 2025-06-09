import customtkinter as ctk
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

currency_list = ["USD", "EUR", "INR", "JPY", "GBP", "CAD", "AUD", "CHF", "CNY"]

#fuction
def curr_convert():
    amount=amount_entry.get()
    from_currency=l2.get()
    to_currency=l3.get()

    if not amount:
        result.configure(text="⚠️ Please enter the amount")
        return
    
    try:
        amount=float(amount)
    except ValueError:
        result.configure(text="❌ Invalid Amount")
        return
    
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data= response.json()
        converted = data['rates'][to_currency]
        result.configure(text=f"{amount}{from_currency} = {converted:.2f}{to_currency}")
    except ValueError:
        result.configure(text="⚠️ Error Fetching Data")



#window creation
window = ctk.CTk()
window.title("CURRENCY CONVERTER")
window.geometry("500x500")
window.resizable(False,False)

label1 = ctk.CTkLabel(window , text="Currency Coverter" , font=("Arial Rounded MT Bold",24))
label1.pack(pady = 20)

amount_entry = ctk.CTkEntry(window, placeholder_text="Enter the amount" , font=("Arial",16),width=300 , height=40)
amount_entry.pack(pady = 15)

label2 = ctk.CTkLabel(window , text="From Currency" , font=("Arial Bold",18))
label2.pack()
l2 = ctk.CTkOptionMenu(window,values=currency_list,width=300,height=40,font=("Arial",16))
l2.pack(pady=10)
l2.set('USD')

label3 = ctk.CTkLabel(window , text="TO Currency" , font=("Arial Bold",18))
label3.pack()
l3 = ctk.CTkOptionMenu(window,values=currency_list,width=300,height=40,font=("Arial",16))
l3.pack(pady=10)
l3.set('INR')

button = ctk.CTkButton(window,text="Convert",command=curr_convert , font=("Arial Bold",24) , width=200 , height=40)
button.pack(pady=20)

result = ctk.CTkLabel(window,text="💰 Result will appear here" , font=("Arial",18),text_color="white")
result.pack(pady= 10)

window.mainloop()