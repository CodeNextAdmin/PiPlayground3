from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dynamic')
def dynamic():
    
    greeting="Team Edge is in the house!"
    friends = ["Cardi", "Janelle", "Kali", "Jorja", "Rosalia", "Karol"]

    return render_template('dynamic.html', greeting=greeting, friends=friends)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')