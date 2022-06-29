from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '8989'
app.config['MYSQL_DB'] = 'cdac'

mysql = MySQL(app)

@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT  * FROM Cluster''')
    rv = cur.fetchall()
    return render_template('dmoind.html', students=rv )

# @app.route('/')
# def Index():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT  * FROM Cluster")
#     data = cur.fetchall()
#     cur.close()


if __name__ == '__main__':
    app.run(debug=True)