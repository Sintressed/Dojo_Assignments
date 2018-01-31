from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
    arr = ['first_name','last_name','email','password','confirm_password']
    for i in range(0,5):
        x = 0
        if len(request.form[arr[i]]) < 1:
            flash('{name} cannot be blank,'.format(name = arr[i]))
            x = x -1
        elif len(request.form[arr[i]]) > 1:
            x = x + 1
    f_name = str(request.form['first_name'])
    l_name = str(request.form['last_name'])
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        x = x -1        
    elif not str.isalpha(f_name):
        flash('names do not contain digits, fix it')
        x = x -1 
    elif not str(l_name):
        flash('names do not contain digits, fix it')
        x = x -1 
    elif not request.form['password'] == request.form['confirm_password']:
        flash('passwords do not match!')
        x = x -1 
    if len(request.form['password']) > 8:
        flash('password cannot be longer than 8 characters') 
        x = x -1 
    elif x >= 1:
        flash("Form was submitted!")
    print 'name',x
    return redirect('/')

app.run(debug=True)