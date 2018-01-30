from flask import Flask, render_template, request, redirect,flash
app = Flask(__name__)
app.secret_key = 'SecretKey'
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/result', methods=["POST"])
def process():
    # do something with the form data 
    if len(request.form['name']) < 1:
      flash('name Cannot Be Empty!')
    else:
      flash('success!')
    if len(request.form['tet']) < 1:
      flash('comment Cannot Be Empty!')
    else:
      flash('success!')
    if len(request.form['tet']) > 120:
      flash('comments cannot be longer than 120 characters')
    if len(request.form['name']) > 1 < 120 and len(request.form['tet']) > 1:
      name = request.form['name']  
      loc = request.form['loc']
      lang = request.form['language']
      comm = request.form['tet']
      return render_template("user.html",name = name,loc = loc, lang = lang,comm =comm)
    else:
      return redirect('/')
app.run(debug=True) # run server
