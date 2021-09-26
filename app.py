from flask import Flask, render_template
import Adafruit_DHT
import psycopg2
import os
from threading import Timer
from datetime import datetime

app = Flask(__name__)

conn = psycopg2.connect(
    host="free-tier.gcp-us-central1.cockroachlabs.cloud",
    port=26257,
    database="muted-rhino-1559.defaultdb",
    user=os.environ['COCKROACH_USER'],
    password=os.environ['COCKROACH_PASSWORD'])

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hiveMap')
def hiveMap():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(f"Humidity: {humidity}\nTemperature: {temperature}")
        return render_template('hiveMap.html', humidity=humidity, temperature=temperature)
    else:
        return render_template('hiveMap.html', humidity=0, temperature=0)

@app.route('/ourSolution')
def ourSolution():
    return render_template('ourSolution.html')

@app.route('/addHive')
def addHive():
    return render_template('addHive.html')

def update_db():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS beehive_data (time TEXT , temperature FLOAT, humidity FLOAT)"
        )
        cur.execute("INSERT INTO beehive_data VALUES("+str(datetime.now().strftime('%H:%M'))+"," + str(temperature) + "," + str(humidity)+");")
        conn.commit()

if __name__ == '__main__':
    t = Timer(3.0, update_db)
    t.start()
    app.run(debug=True, host='0.0.0.0')