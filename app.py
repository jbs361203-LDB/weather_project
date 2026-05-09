from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

SERVICE_KEY = "52706c4850db4268aa4be8b9127ae1f1c70667f0963133cf7a75d443a2a2c2f9"

@app.route('/')

def home():

    now = datetime.now()

    base_date = now.strftime("%Y%m%d")
    base_time = "1100"

    nx = "60"
    ny = "127"

    url = (
        f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
        f"?serviceKey={SERVICE_KEY}"
        f"&pageNo=1"
        f"&numOfRows=10"
        f"&dataType=JSON"
        f"&base_date={base_date}"
        f"&base_time={base_time}"
        f"&nx={nx}"
        f"&ny={ny}"
    )

    temp = "정보 없음"
    humidity = "정보 없음"

    try:

        response = requests.get(url)
        data = response.json()

        items = data['response']['body']['items']['item']

        for item in items:

            if item['category'] == 'T1H':
                temp = item['obsrValue']

            if item['category'] == 'REH':
                humidity = item['obsrValue']

    except Exception as e:
        print(e)

    return render_template(
        'index.html',
        temp=temp,
        humidity=humidity
    )

if __name__ == '__main__':
    app.run(debug=True)