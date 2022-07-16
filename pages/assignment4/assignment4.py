import json
from flask import Blueprint, render_template
from flask import Flask, redirect, url_for
from flask import request, session, jsonify, json
import mysql.connector
import requests
from app import app

assignment4 = Blueprint('assignment4', __name__,
                        static_folder='static',
                        static_url_path='/pages/assignment4',
                        template_folder='templates')




# ------------------------------------------------- #
# ------------- DATABASE CONNECTION --------------- #
# ------------------------------------------------- #


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='route',
                                         database='ex4')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# --------------------------Part A---------------------------#


@assignment4.route("/assignment4")
def assignment_4_func():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment4.html', users=query_result)


# -------------------- INSERT --------------------- #

@assignment4.route("/assignment4insert", methods=['GET', 'POST'])
def insert_user():
    nickname = request.form['user_nickname']
    email = request.form['user_email']
    first_name = request.form['user_first_name']
    last_name = request.form['user_last_name']
    password = request.form['user_password']

    session['INSERTED'] = True
    session['DELETED'] = False
    session['UPDATE'] = False

    user_exist = "select * FROM users WHERE user_nickname='%s';" % nickname
    users_list = interact_db(user_exist, query_type='fetch')
    if len(users_list) > 0:
        session['insert_message'] = "sorry, we already have this user "
    else:
        query = "INSERT INTO users(user_nickname, user_email, user_first_name, user_last_name, user_password) VALUES " \
                "('%s','%s','%s','%s','%s')" % (nickname, email, first_name, last_name, password)
        interact_db(query=query, query_type='commit')
        session['insert_message'] = "registration succeeded"
    return redirect('/assignment4')


# ----------------------------------- UPDATE --------------------------------------#

@assignment4.route("/assignment4update", methods=['POST'])
def update_user():
    nickname = request.form['user_nickname']
    email = request.form['user_email']
    first_name = request.form['user_first_name']
    last_name = request.form['user_last_name']
    password = request.form['user_password']
    session['INSERTED'] = False
    session['UPDATE'] = True
    session['DELETED'] = False
    session['update_message'] = "update succeeded"
    user_exist = "select * FROM users WHERE user_nickname='%s';" % nickname
    users_list = interact_db(user_exist, query_type='fetch')
    if len(users_list) > 0:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             passwd='route',
                                             database='ex4')
        updateCursor = connection.cursor()
        updateCursor.execute('''
            UPDATE users
            SET user_first_name = %s, user_last_name = %s, user_email = %s, user_password = %s
            WHERE user_nickname = %s
            ''', (email, first_name, last_name, password, nickname))
        connection.commit()
        session['update_message'] = "update succeeded"
    else:
        session['update_message'] = "sorry, user not exist"
    return redirect("/assignment4")


# -------------------- DELETE --------------------- #

@assignment4.route("/assignment4delete", methods=['POST'])
def delete_user():
    nickname = request.form['user_nickname']
    session['INSERTED'] = False
    session['UPDATE'] = False
    session['DELETED'] = True

    check_query = 'select * from users'
    before_change_users = interact_db(check_query, query_type='fetch')

    session['delete_message'] = "user deleted"

    query = "DELETE FROM users WHERE user_nickname='%s';" % nickname
    interact_db(query, query_type='commit')

    check_query = 'select * from users'
    after_change_users = interact_db(check_query, query_type='fetch')
    if len(before_change_users) > len(after_change_users):
        session['delete_message'] = "delete user succeeded"
    else:
        session['delete_message'] = "sorry, user not exist"
    return redirect("/assignment4")

# -------------------- assignment4_users_PartB --------------------- #



# -------------------------------------------------------------




