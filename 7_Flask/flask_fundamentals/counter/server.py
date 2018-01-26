from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'SecretKey' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/users', methods=['POST'])
def create_user():
    session['root'] = session['root'] + 1   
    return redirect('/')
app.run(debug=True)