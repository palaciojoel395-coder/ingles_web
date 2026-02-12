from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/metodo")
def metodo():
    return render_template("metodo.html")

@app.route("/programas")
def programas():
    return render_template("programas.html")

@app.route("/recursos")
def recursos():
    return render_template("recursos.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)