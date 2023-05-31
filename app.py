from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/beach")
def beach():
    return render_template("beach.html")

@app.route("/mountains")
def mountains():
    return render_template("mountains.html")

@app.route("/oceans")
def oceans():
    return render_template("oceans.html")

@app.route("/jungle")
def jungle():
    return render_template("jungle.html")

if __name__ == "__main__":
    app.run(debug=True)