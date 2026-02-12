from flask import Flask, render_template, request

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

@app.route("/testimonios")
def testimonios():
    return render_template("testimonios.html")

@app.route("/equipo")
def equipo():
    return render_template("equipo.html")

@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        mensaje = request.form["mensaje"]
        print(nombre, correo, mensaje)
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000 )