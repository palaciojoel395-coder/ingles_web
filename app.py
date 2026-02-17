from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/pronunciacion")
def pronunciacion():
    return render_template("pronunciacion.html")

@app.route("/interaccion y aprendizaje")
def interaccion():
    return render_template("interaccion y aprendizaje.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)