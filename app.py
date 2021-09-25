from flask import Flask, render_template
import Adafruit_DHT

app = Flask(__name__)

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hiveMap')
def hiveMap():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return render_template('hiveMap.html', humidity=humidity, temperature=temperature)
    else:
        return render_template('hiveMap.html', humidity=0, temperature=0)

@app.route('/ourSolution')
def ourSolution():
    return render_template('ourSolution.html')

@app.route('/addHive')
def addHive():
    return render_template('addHive.html')

if __name__ == '__main__':
    app.run(debug=True)
