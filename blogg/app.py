from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/fashion')
def fashion():
    return render_template("fashion.html")


@app.route('/trend')
def trend():
    return render_template("trends.html")


@app.route('/house')
def house():
    return render_template("the_house.html")


@app.route('/entertainment')
def entertainment():
    return render_template("entertainment.html")


@app.route('/news')
def news():
    return render_template("news.html")


if __name__ == '__main__':
    app.run()
