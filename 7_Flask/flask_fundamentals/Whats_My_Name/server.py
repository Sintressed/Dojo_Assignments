from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/process', methods=["POST"])
def process():
    # do something with the form data 
    name = request.form['name']
    return render_template("user.html",name = name)
    return redirect('/')
app.run(debug=True) # run server

