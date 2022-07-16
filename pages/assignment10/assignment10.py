
from flask import Blueprint, render_template, redirect, request
from interact_with_DB import interact_db


assignment10 = Blueprint('assignment10',
                         __name__,
                         static_folder='static',
                         template_folder='templates'
                         )


@assignment10.route('/assignment10')
def assignment10_def():
    query='select * from users;'
    name=''
    email=''
    users = interact_db(query=query, query_type='fetch')
    if 'name' in request.args:
        name = request.args['name']
        return render_template('assignment10.html', users=users, name=name)
    elif 'email' in request.args:
        email = request.args['email']
    return render_template('assignment10.html', users=users, email=email)









@assignment10.route('/insert_user', methods=['POST'])
def insert_user_func():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    qurey =" INSERT INTO users(name, email, password) VALUES ('%s', '%s', '%s');" % (name, email, password)
    interact_db(query=qurey, query_type='commit')
    return redirect('/assignment10?name='+name)


@assignment10.route('/delete_users', methods=['POST'])
def delete_users_func():
    email = request.form['email']
    qurey = " DELETE FROM users WHERE email='%s';" % email
    interact_db(query=qurey, query_type='commit')

    return redirect('/assignment10?email='+email)


@assignment10.route('/update_user', methods=['POST'])
def update_user_func():
    email = request.form['email']
    password = request.form['password']
    qurey = " UPDATE users SET password='%s' WHERE email ='%s' ;" % (password, email)
    interact_db(query=qurey, query_type='commit')
    return redirect('/assignment10?email='+email)






