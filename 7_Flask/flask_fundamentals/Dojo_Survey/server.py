from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/result', methods=["POST"])
def process():
    # do something with the form data 
    name = request.form['name']
    loc = request.form['loc']
    lang = request.form['language']
    comm = request.form['tet']
    return render_template("user.html",name = name,loc = loc, lang = lang,comm =comm)
    return redirect('/')
app.run(debug=True) # run server
