import mysql.connector
from mysql.connector import Error
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def registration_form():
    return render_template('registration.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Retrieve form data
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='mydb'
        )

        cursor = connection.cursor()

        # Insert user data into the database
        insert_query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        data = (username, email, password)
        cursor.execute(insert_query, data)

        connection.commit()

        return "Registration successful"

    except Error as e:
        return "Error: " + str(e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run()
