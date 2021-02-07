from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host  = '0.0.0.0', port = 5100)
