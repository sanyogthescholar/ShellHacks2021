from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hiveMap')
def hiveMap():
    return render_template('hiveMap.html')

@app.route('/ourSolution')
def ourSolution():
    return render_template('ourSolution.html')

@app.route('/addHive')
def addHive():
    return render_template('addHive.html')

if __name__ == '__main__':
    app.run(debug=True)
