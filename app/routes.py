from app import app
from flask import render_template, request
from app.db_connection import open_db_connection


@app.route("/", methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        category_name = request.form['name']
        connection, cursor = open_db_connection()
        cursor.execute(f'insert into category (name) values (\'{category_name}\');')
        connection.commit()
        cursor.close()
        connection.close()
    connection, cursor = open_db_connection()
    cursor.execute('select * from category;')
    categories = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("home.html", categories=categories)