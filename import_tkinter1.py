import tkinter as tk
from datetime import datetime
import random

# Colors
bg = "#121212"
fg = "white"

root = tk.Tk()
root.title("Age & Fortune App")
root.geometry("600x500")
root.configure(bg=bg)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Frames
input_frame = tk.Frame(root, bg=bg)
result_frame = tk.Frame(root, bg=bg)

for frame in (input_frame, result_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# -------- INPUT PAGE --------
tk.Label(input_frame, text="🌟 Age & Fortune App",
         font=("Segoe UI Emoji", 18, "bold"),
         bg=bg, fg=fg).pack(pady=20)

def create_input(label):
    tk.Label(input_frame, text=label,
             font=("Segoe UI Emoji", 11),
             bg=bg, fg=fg).pack()
    entry = tk.Entry(input_frame)
    entry.pack(pady=5)
    return entry

name_entry = create_input("👤 Name")
day_entry = create_input("📅 Day")
month_entry = create_input("📆 Month")
year_entry = create_input("🗓️ Year")

# -------- RESULT PAGE --------
result_label = tk.Label(
    result_frame,
    text="",
    font=("Segoe UI Emoji", 14),
    bg=bg,
    fg=fg,
    justify="left",
    wraplength=500
)
result_label.pack(expand=True, fill="both", padx=20, pady=20)

def go_back():
    input_frame.tkraise()

tk.Button(result_frame, text="⬅ Back", command=go_back).pack(pady=10)

# -------- FUNCTION --------
def calculate():
    name = name_entry.get().strip()
    day = day_entry.get().strip()
    month = month_entry.get().strip()
    year = year_entry.get().strip()

    # -------- VALIDATION --------
    if not name:
        result_label.config(text="⚠️ Please enter your name!")
        result_frame.tkraise()
        return

    if not day or not month or not year:
        result_label.config(text="⚠️ Please fill in all date fields!")
        result_frame.tkraise()
        return

    if not day.isdigit():
        result_label.config(text="⚠️ Day must be a number!")
        result_frame.tkraise()
        return

    if not month.isdigit():
        result_label.config(text="⚠️ Month must be a number!")
        result_frame.tkraise()
        return

    if not year.isdigit():
        result_label.config(text="⚠️ Year must be a number!")
        result_frame.tkraise()
        return

    d = int(day)
    m = int(month)
    y = int(year)

    if not (1 <= d <= 31):
        result_label.config(text="⚠️ Day must be between 1 and 31!")
        result_frame.tkraise()
        return

    if not (1 <= m <= 12):
        result_label.config(text="⚠️ Month must be between 1 and 12!")
        result_frame.tkraise()
        return

    if y > datetime.now().year:
        result_label.config(text="⚠️ Year cannot be in the future!")
        result_frame.tkraise()
        return

    if y < 1900:
        result_label.config(text="⚠️ Year is too old!")
        result_frame.tkraise()
        return

    try:
        birth = datetime(y, m, d)
    except:
        result_label.config(text="⚠️ This date does not exist!")
        result_frame.tkraise()
        return

    # -------- CALCULATION --------
    today = datetime.now()

    years = today.year - y
    months = today.month - m
    days = today.day - d

    if days < 0:
        months -= 1
        days += 30
    if months < 0:
        years -= 1
        months += 12

    # -------- AGE MESSAGE --------
    if years <= 13:
        age_message = "🧒 You're a kid, enjoy your time"
    elif 14 <= years <= 18:
        age_message = "😎 Teenager mode activated"
    elif 19 <= years <= 30:
        age_message = "😄 Welcome to adult life"
    else:
        age_message = "👴 hallo old people"

    is_birthday = (today.day == d and today.month == m)

    next_birthday = datetime(today.year, m, d)
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, m, d)

    days_left = (next_birthday - today).days

    fortunes = [
        "🍀 Luck will follow you today",
        "✨ Today is your day to shine",
        "🎁 A surprise is waiting for you",
        "😊 Someone will make you smile",
        "💪 You will achieve something great",
        "🌈 Happiness is coming your way",
        "🔥 Today is full of energy — use it wisely",
        "🌟 A great opportunity may come today",
        "💖 Love and kindness will surround you",
        "🎯 Stay focused — success is close",
        "😎 Today will be calm and peaceful",
        "🚀 Big progress is coming your way",
        "🎉 Something exciting might happen today",
        "🧠 A smart decision will help you a lot",
        "🌸 A fresh start is waiting for you",
        "💡 A new idea could change your day",
        "🎵 Enjoy the little moments today",
        "🌞 Positivity will guide your path",
        "🤝 You may meet someone important today",
        "⚡ Be ready — something unexpected is coming",
        "🏆 You’re closer to your goals than you think",
        "💫 Magic moments are hidden in your day",
        "📈 Today is a good day for improvement",
        "🌊 Go with the flow and things will work out",
        "🛤️ Your path is becoming clearer today",
        "🎨 Creativity will shine through you",
        "🔑 You might find an important answer today",
        "🌍 Today could open new doors for you"
    ]

    fortune = random.choice(fortunes)

    if is_birthday:
        text = f"🎉🎂 HAPPY BIRTHDAY {name}! 🎂🎉\n\n"
    else:
        text = f"👋 Hi {name},\n\n"

    text += (
        f"🎯 Age: {years} years, {months} months, {days} days\n\n"
        f"🧠 Stage: {age_message}\n\n"
        f"⏳ Days until birthday: {days_left}\n\n"
        f"🌟 {fortune}"
    )

    result_label.config(text=text)
    result_frame.tkraise()

# Button
tk.Button(input_frame, text="✨ Calculate",
          command=calculate,
          font=("Segoe UI Emoji", 12, "bold")).pack(pady=20)

input_frame.tkraise()
root.mainloop()