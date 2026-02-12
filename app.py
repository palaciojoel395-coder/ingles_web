from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/metodo")
def metodo():
    return "<h1>Método</h1>"

@app.route("/programas")
def programas():
    return "<h1>Programas</h1>"

@app.route("/recursos")
def recursos():
    return "<h1>Recursos</h1>"

@app.route("/blog")
def blog():
    return "<h1>Blog</h1>"

@app.route("/testimonios")
def testimonios():
    return "<h1>Testimonios</h1>"

@app.route("/equipo")
def equipo():
    return "<h1>Equipo</h1>"

@app.route("/contacto")
def contacto():
    return "<h1>Contacto</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)