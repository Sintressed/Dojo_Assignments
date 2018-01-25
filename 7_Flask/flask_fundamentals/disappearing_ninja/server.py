from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def route():
    return render_template('route.html')
@app.route('/ninja')
def index():
  return render_template("index.html")
@app.route('/ninja/<color>')
def img_picker(color):
    if color == 'blue':
        img = 'leonardo.jpg'
    elif color == 'red':
        img = 'raphael.jpg'
    elif color == 'orange':
        img = 'michelangelo.jpg'
    elif color == 'purple':
        img = 'donatello.jpg'
    else:
        img = 'notapril.jpg'
    return render_template('color.html',img = img)
app.run(debug=True)