from app import app
from flask import render_template
from app.db_connection import open_db_connection

@app.route("/")
def home():
    connection, cursor = open_db_connection()
    cursor.execute('select * from category;')
    categories = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("home.html", categories=categories)