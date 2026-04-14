from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

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
                error = "⚠️ Please enter your name!"
                return render_template("index.html", error=error)

            if not day or not month or not year:
                error = "⚠️ Fill all fields!"
                return render_template("index.html", error=error)

            if not (day.isdigit() and month.isdigit() and year.isdigit()):
                error = "⚠️ Date must be numbers!"
                return render_template("index.html", error=error)

            d, m, y = int(day), int(month), int(year)

            if not (1 <= d <= 31 and 1 <= m <= 12):
                error = "⚠️ Invalid day or month!"
                return render_template("index.html", error=error)

            if y > datetime.now().year:
                error = "⚠️ Year in future!"
                return render_template("index.html", error=error)

            # Real date check
            birth = datetime(y, m, d)

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

            # Birthday
            is_birthday = (today.day == d and today.month == m)

            next_birthday = datetime(today.year, m, d)
            if next_birthday < today:
                next_birthday = datetime(today.year + 1, m, d)

            days_left = (next_birthday - today).days

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

            result = {
                "name": name,
                "years": years,
                "months": months,
                "days": days,
                "zodiac": zodiac,
                "fortune": random.choice(fortunes),
                "color": colors[zodiac],
                "days_left": days_left,
                "is_birthday": is_birthday
            }

        except:
            error = "⚠️ Invalid date!"

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)