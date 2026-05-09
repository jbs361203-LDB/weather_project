from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("WEATHER_API_KEY")

@app.route("/")
def home():
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"

    params = {
        "serviceKey": API_KEY,
        "pageNo": "1",
        "numOfRows": "10",
        "dataType": "JSON",
        "base_date": "20260509",
        "base_time": "2300",
        "nx": "55",
        "ny": "127"
    }

    response = requests.get(url, params=params)
    data = response.json()

    temperature = "없음"
    humidity = "없음"

    try:
        items = data['response']['body']['items']['item']

        for item in items:
            if item['category'] == 'T1H':
                temperature = item['obsrValue']

            if item['category'] == 'REH':
                humidity = item['obsrValue']

    except:
        pass

    return render_template(
        "index.html",
        temperature=temperature,
        humidity=humidity
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
