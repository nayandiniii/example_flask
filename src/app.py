from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'nsn'
app.config['MYSQL_PASSWORD'] = 'nsn0407'
app.config['MYSQL_DB'] = 'userdata_db'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Insert user data into MySQL database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()

        return 'Data submitted successfully'

if __name__ == '__main__':
    app.run(debug=True)
