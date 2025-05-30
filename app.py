from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/photo')
def photo():
    return render_template('photos.html')

@app.route('/answers')
def answers():
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
