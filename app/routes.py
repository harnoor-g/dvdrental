from app import app
from flask import render_template, request
from app.db_connection import open_db_connection


@app.route("/", methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        connection, cursor = open_db_connection()
        if 'create' in request.form:
            category_name = request.form['category']
            cursor.execute(f'insert into category (name) values (\'{category_name}\');')
            connection.commit()
        elif 'update' in request.form and request.form['new_category'] != '':
            new_category_name = request.form['new_category']
            category_id = request.form.get('update')
            cursor.execute(f'update category set name=\'{new_category_name}\' where category_id={category_id};')
            connection.commit()
        elif 'delete' in request.form:
            category_id = request.form.get('delete')
            cursor.execute(f'delete from category where category_id={category_id};')
            connection.commit()
        cursor.close()
        connection.close()
    connection, cursor = open_db_connection()
    cursor.execute('select * from category;')
    categories = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("home.html", categories=categories)