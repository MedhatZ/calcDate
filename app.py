from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)


# -------- ZODIAC FUNCTION --------
def get_zodiac(m, d):
    if (m == 3 and d >= 21) or (m == 4 and d <= 19):
        return "Aries"
    elif (m == 4 and d >= 20) or (m == 5 and d <= 20):
        return "Taurus"
    elif (m == 5 and d >= 21) or (m == 6 and d <= 20):
        return "Gemini"
    elif (m == 6 and d >= 21) or (m == 7 and d <= 22):
        return "Cancer"
    elif (m == 7 and d >= 23) or (m == 8 and d <= 22):
        return "Leo"
    elif (m == 8 and d >= 23) or (m == 9 and d <= 22):
        return "Virgo"
    elif (m == 9 and d >= 23) or (m == 10 and d <= 22):
        return "Libra"
    elif (m == 10 and d >= 23) or (m == 11 and d <= 21):
        return "Scorpio"
    elif (m == 11 and d >= 22) or (m == 12 and d <= 21):
        return "Sagittarius"
    elif (m == 12 and d >= 22) or (m == 1 and d <= 19):
        return "Capricorn"
    elif (m == 1 and d >= 20) or (m == 2 and d <= 18):
        return "Aquarius"
    else:
        return "Pisces"


# -------- AGE MESSAGE --------
def get_age_message(years):
    if years <= 13:
        return "🧒 You're a kid, enjoy your time"
    elif 14 <= years <= 18:
        return "😎 Teenager mode activated"
    elif 19 <= years <= 30:
        return "😄 Welcome to adult life"
    else:
        return "👴 Hello old people"


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            name = request.form["name"].strip()
            day = request.form["day"]
            month = request.form["month"]
            year = request.form["year"]

            # -------- VALIDATION --------
            if not name:
                return render_template("index.html", error="⚠️ Please enter your name!")

            if not (day and month and year):
                return render_template("index.html", error="⚠️ Fill all fields!")

            if not (day.isdigit() and month.isdigit() and year.isdigit()):
                return render_template("index.html", error="⚠️ Date must be numbers!")

            d, m, y = int(day), int(month), int(year)

            if not (1 <= d <= 31 and 1 <= m <= 12):
                return render_template("index.html", error="⚠️ Invalid day or month!")

            if y > datetime.now().year:
                return render_template("index.html", error="⚠️ Year in future!")

            # validate real date
            birth = datetime(y, m, d)

            today = datetime.now()

            # -------- AGE CALCULATION --------
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
            age_message = get_age_message(years)

            # -------- BIRTHDAY CHECK --------
            is_birthday = (today.day == d and today.month == m)

            next_birthday = datetime(today.year, m, d)
            if next_birthday < today:
                next_birthday = datetime(today.year + 1, m, d)

            days_left = (next_birthday - today).days

            # -------- ZODIAC --------
            zodiac = get_zodiac(m, d)

            colors = {
                "Aries": "#ff4d4d",
                "Taurus": "#2ecc71",
                "Gemini": "#f1c40f",
                "Cancer": "#3498db",
                "Leo": "#e67e22",
                "Virgo": "#1abc9c",
                "Libra": "#9b59b6",
                "Scorpio": "#e74c3c",
                "Sagittarius": "#ff9800",
                "Capricorn": "#95a5a6",
                "Aquarius": "#00bcd4",
                "Pisces": "#3f51b5"
            }

            fortunes = [
                "🍀 Luck will follow you!",
                "✨ Today is your day!",
                "🎁 Surprise coming!",
                "😊 Smile today!",
                "💪 You got this!",
                "🌈 Happiness is near!"
            ]

            # -------- RESULT --------
            result = {
                "name": name,
                "years": years,
                "months": months,
                "days": days,
                "age_message": age_message,
                "zodiac": zodiac,
                "fortune": random.choice(fortunes),
                "color": colors[zodiac],
                "days_left": days_left,
                "is_birthday": is_birthday
            }

        except:
            error = "⚠️ Invalid date!"

    return render_template("index.html", result=result, error=error)


import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
