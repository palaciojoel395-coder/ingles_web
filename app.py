from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pronunciacion')
def pronunciacion():
    return render_template('pronunciacion.html')

if __name__ == '__main__':
    app.run(debug=True)