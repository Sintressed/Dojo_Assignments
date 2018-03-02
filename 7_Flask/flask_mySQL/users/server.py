from flask import Flask, request, redirect, render_template, session,flash
from mysqlconnection import MySQLConnector
import datetime
import re
import md5

app = Flask(__name__)
app.secret_key = 'Secret'
mysql = MySQLConnector(app,'users_db')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')

@app.route('/users')
def main():
    users_list = mysql.query_db("select *,DATE_FORMAT(info.created_at, '%b %D,%Y') from info")
    return render_template('index.html',users = users_list)
@app.route('/users/new')
def new():
    return render_template('new.html')
@app.route('/users/<id>')
def identify(id):              
    users_list = mysql.query_db("select *,DATE_FORMAT(info.created_at, '%b %D,%Y') AS Date from info" )
    id = int(id) - 1
    return render_template('id.html',id = id,users=users_list)
@app.route('/users/<id>/edit')
def edit_id(id):
    id = int(id) - 1
    users_list = mysql.query_db("select *,DATE_FORMAT(info.created_at, '%b %D,%Y') AS Date from info" )
    return render_template('edit.html', id = id,users=users_list)
#@app.route('/users/<id>/destroy')
#post routes
#def destroy():
    #return render_template('edit.html')
@app.route('/users/create')
#from '/users/new'
def create():
    return redirect('''user['id']''')
@app.route('/users/<id>', methods = ['POST'])
#from  '/users/<id>/edit'
def post_id(id):
    query = "UPDATE info SET first_name = :first, last_name = :last, email_address = :email, created_at = NOW() WHERE id = :id"
    data = {
        "first": request.form['first_name'],
        "last": request.form['last_name'],
        "email": request.form['email_address'],
        "id": id
    }
    print mysql.query_db(query, data)
    mysql.query_db(query, data)
    print 'yes'
    return redirect('/users/<id>', id = id)
app.run(debug=True)