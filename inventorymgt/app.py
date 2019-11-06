from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/users')
def users():
    return render_template("users.html")


@app.route('/contact_us')
def reach_us():
    return render_template("contact_us.html")


@app.route('/inventory')
def inventory():
    return render_template("inventory.html")


if __name__ == '__main__':
    app.run()
