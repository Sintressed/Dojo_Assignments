from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
  return redirect('/process')
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/process',methods =['POST'])
def show_user_profile():
    name = request.form['name']
    return render_template("user.html", name )
app.run(debug=True) # run server

