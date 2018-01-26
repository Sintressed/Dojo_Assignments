from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'SecretKey' # you need to set a secret key for security purposes
# routing rules and rest of server.py  
import random
@app.route('/')
def index():       
    return render_template("index.html") 
    session['root'] = random.randrange(0, 101)
@app.route('/users', methods=['POST'])
def create_user():
    session['x'] = 'GUESS!!'
    if session['root'] != int(request.form['guess']):
        if session['root'] >int(request.form['guess']):
            session['x'] = 'too low! Try Again!'            
        elif session['root'] < int(request.form['guess']):
            session['x'] = 'Too High! Try Again!'                                 
    elif session['root'] == int(request.form['guess']):
        session['x'] = 'YOU DID IT!! PUT IN A NUMBER AND CLICK HERE TO PLAY AGAIN!>>'
        session['root'] = random.randrange(0, 101)
    return redirect('/')
app.run(debug=True)
