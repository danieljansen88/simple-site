from tkinter import Button
from flask import Flask, render_template

app = Flask(__name__, template_folder='static')


BUTTONS = [
    {
        "text":"comprar",
        "image_url":"static/images/comprar.jpg"
    },
    {
        "text":"vender",
        "image_url":"static/images/vender.jpg"
    }
]

@app.route("/")
def home():
    page_name="home"
    return render_template('templates/pages/index.html', page_name=page_name, buttons=BUTTONS)

@app.route("/buy")
def buy():
    name = 'Samuel'
    return render_template('templates/pages/buy/index.html', name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

