from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "여기에_본인_API키"

@app.route("/")
def home():

    # 전주 날씨
    city = "Jeonju"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=kr"

    response = requests.get(url)
    data = response.json()

    print(data)   # 디버깅용

    # 기온 / 습도 가져오기
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    return render_template(
        "index.html",
        temp=temp,
        humidity=humidity
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
