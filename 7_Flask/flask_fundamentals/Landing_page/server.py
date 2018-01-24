from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/ninjas')
def two():
    return render_template('ninjas.html')
@app.route('/dojo/new')
def three():
    return render_template('dojos.html', action = '')
app.run(debug=True)