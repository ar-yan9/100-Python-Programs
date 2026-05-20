from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/bye")
def bye():
    return "<h3>Bye!</h3>"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<h1>Hello {name}, you are {number} years old!</h1>"

if __name__ == "__main__":
    app.run(debug=True)