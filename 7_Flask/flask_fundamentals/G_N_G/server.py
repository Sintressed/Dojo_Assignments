from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'SecretKey' # you need to set a secret key for security purposes
# routing rules and rest of server.py  
@app.route('/')
def index():        
    return render_template("index.html")
import random  
x = random.randrange(0, 101)
@app.route('/users', methods=['POST'])
def create_user():
    session['root'] = x
    if session['root'] != request.form['guess']:
        if session['root'] > request.form['guess']:
            session.pop('voice')            
            session['voice'] = "Too Low"           
        elif session['root'] < request.form['guess']:
            session.pop('voice')                        
            session['voice'] = "Too  High"  
    elif session['root'] == request.form['guest']:
        print 'hello'
    return redirect('/')
app.run(debug=True)
