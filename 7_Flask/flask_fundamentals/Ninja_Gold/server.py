from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'SecretKey' # you need to set a secret key for security purposes
# routing rules and rest of server.py  
import random
@app.route('/')
def index():       
    return render_template("index.html") 
    session['gold'] = 0
@app.route('/process_money', methods=['POST'])
def Gold():
    session['voice'] = 'gained'
    session['color'] = 'green'
    if request.form['action'] == 'house':
        session['place'] = 'House'
        session['rangold'] = random.randrange(2, 6) 
        session['gold'] = session['gold'] +  session['rangold']  
        session['quote'] = session['quote'] + 'you earned {gold} golds from the {place}!'.format(place = session['place'],gold = session['rangold'])
    elif request.form['action'] == 'casino':
        session['place'] = 'Casino'
        session['rangold'] = random.randrange(0,51)
        session['ran'] = random.randrange(0,2)
        if session['ran'] == 0:
            session['gold'] = session['gold'] - session['rangold']
            session['voice'] = 'Lost'
            session['color'] = 'red'
            session['quote'] = session['quote']  + '<h3>you entered a {place}... and lost {gold} golds...ouch</h3><br>'.format(place = session['place'],gold = session['rangold'])             
        elif session['ran'] == 1:
            session['gold'] = session['gold'] + session['rangold']   
            session['quote'] = session['quote'] + 'you earned {gold} golds from the {place}!'.format(place = session['place'],gold = session['rangold'])           
    elif request.form['action'] == 'farm':
        session['place'] = 'Farm'
        session['rangold'] = random.randrange(10, 21) 
        session['gold'] = session['gold'] + session['rangold'] 
        session['quote'] = session['quote'] + 'you earned {gold} golds from the {place}!'.format(place = session['place'],gold = session['rangold'])             
    elif request.form['action'] == 'cave':
        session['place'] = 'Cave'
        session['rangold'] = random.randrange(5, 11)
        session['gold'] = session['gold'] + session['rangold']
        session['quote'] = session['quote'] + 'you earned {gold} golds from the {place}!'.format(place = session['place'],gold = session['rangold'])
    return redirect('/')
@app.route('/reset', methods = ['POST'])
def reset():
    session['gold'] = 0
    session['quote'] = ''
    return redirect('/')
app.run(debug=True)
