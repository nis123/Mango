import os
from flask import Flask, render_template, request, url_for, send_from_directory, json
import pymysql.cursors

app = Flask(__name__)

"""
hackru_pass = os.environ['HACKRU_PASS']

connection = pymysql.connect(host='mangodb.c3all2cpsbip.us-east-1.rds.amazonaws.com',
                             user='mango',
                             password=hackru_pass,
                             db='mangodb')
                             


@app.route('/')
def home():
    try:
        with connection.cursor() as cursor:
            # Create a new record
            cursor.execute("INSERT INTO user (email, pwd) VALUES (%s, %s)", ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM user"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
    finally:
        return render_template('index.html')
        """



@app.route('/')
def home():
    return render_template('index.html');
    
@app.route('/login', methods=['POST'])
def login():
    username =  request.form['email'];
    password = request.form['password'];
    return json.dumps({'status':'OK','username':username,'password':password});


app.run(host='0.0.0.0',
        port=int(os.getenv('PORT', 3000)))
