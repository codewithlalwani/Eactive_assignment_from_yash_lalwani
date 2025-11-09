from flask import Flask, render_template, request, redirect, url_for, abort
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'MaHuJiyan@661'
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return render_template('user.html', users=users)

@app.route('/users/<int:id>')
def user_detail(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cur.fetchone()
    if user:
        return render_template('user_detail.html', user=user)
    else:
        abort(404)

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", (name, email, role))
        mysql.connection.commit()
        return redirect(url_for('users'))
    return render_template('new_user.html')

@app.errorhandler(404)
def not_found(e):
    return "User or resource not found", 404

if __name__ == '__main__':
    app.run(debug=True)
