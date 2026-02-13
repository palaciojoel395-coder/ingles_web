from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pronunciacion')
def pronunciacion():
    return render_template('pronunciacion.html')

# Rutas temporales para enlaces en base.html
@app.route('/interaccion')
def interaccion():
    return render_template('pronunciacion.html')  # usa la misma página de pronunciación

@app.route('/metodo')
def metodo():
    return "<h1>Método (Próximamente)</h1>"

@app.route('/programas')
def programas():
    return "<h1>Programas (Próximamente)</h1>"

@app.route('/recursos')
def recursos():
    return "<h1>Recursos (Próximamente)</h1>"

@app.route('/testimonios')
def testimonios():
    return "<h1>Testimonios (Próximamente)</h1>"

@app.route('/blog')
def blog():
    return "<h1>Blog (Próximamente)</h1>"

@app.route('/equipo')
def equipo():
    return "<h1>Equipo (Próximamente)</h1>"

@app.route('/contacto')
def contacto():
    return "<h1>Contacto (Próximamente)</h1>"

if __name__ == '__main__':
    app.run(debug=True)