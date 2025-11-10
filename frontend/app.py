from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hola')
def registration():
    return render_template('hola.html')
                           
if __name__ == '__main__':
    app.run(port= 5002 , debug=True)
