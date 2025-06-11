import tkinter as tk
from tkinter import messagebox

# Optional: for weather icons
from PIL import Image, ImageTk

# Mock API data
mock_weather_data = {
    "Delhi": {"temperature": "35°C", "description": "Sunny", "humidity": "30%", "icon": "sunny.png"},
    "Mumbai": {"temperature": "29°C", "description": "Rainy", "humidity": "85%", "icon": "rain.png"},
    "Bangalore": {"temperature": "27°C", "description": "Cloudy", "humidity": "60%", "icon": "cloudy.png"},
    "Chennai": {"temperature": "33°C", "description": "Humid", "humidity": "70%", "icon": "humid.png"},
}

# Function to simulate fetching weather data
def fetch_weather():
    city = city_entry.get().strip().title()
    if city in mock_weather_data:
        data = mock_weather_data[city]
        temperature_label.config(text=f"Temperature: {data['temperature']}")
        description_label.config(text=f"Description: {data['description']}")
        humidity_label.config(text=f"Humidity: {data['humidity']}")

        # Optional: display weather icon
        try:
            icon = Image.open(data["icon"])
            icon = icon.resize((50, 50))
            icon = ImageTk.PhotoImage(icon)
            icon_label.config(image=icon)
            icon_label.image = icon
        except Exception as e:
            icon_label.config(image='', text="Icon not found")

    else:
        messagebox.showerror("Error", "City not found in mock API!")

# GUI setup
root = tk.Tk()
root.title("Weather App (Mock API)")
root.geometry("350x300")
root.config(bg="#f0f0f0")

tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12), justify='center')
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=fetch_weather, font=("Arial", 12)).pack(pady=10)

temperature_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
temperature_label.pack(pady=5)

description_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
description_label.pack(pady=5)

humidity_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
humidity_label.pack(pady=5)

icon_label = tk.Label(root, bg="#f0f0f0")
icon_label.pack(pady=10)

root.mainloop()


#Currently my project is on demo api
# I am working to make it fully working on api