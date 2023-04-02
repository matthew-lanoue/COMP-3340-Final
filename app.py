from flask import Flask , render_template, url_for, request 
from flask_mysqldb import MySQL 

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask-test'

mysql = MySQL(app)


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        if request.form['submit']=='Login':

            cursor = mysql.connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS tempTable (name VARCHAR(255) NOT NULL,  password VARCHAR(255) NOT NULL);''')
            cursor.execute('''INSERT INTO tempTable  VALUES(%s,%s)''',(name,password))
            mysql.connection.commit()
            cursor.close()
            return f"Done!!"
        elif request.form['submit']=='Sign Up':
            return f"Signing UP"
        
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
