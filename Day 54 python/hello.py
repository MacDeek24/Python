from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye_func():
    return "<p>Bye</p>"

if __name__ == "__main__":
    app.run(debug=True)