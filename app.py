from flask import Flask, render_template, redirect, url_for, request, session, jsonify,sessions
import mysql.connector,requests, json

# ------------------------------------assignment4_PartA-----------------------------#


app = Flask(__name__)
app.secret_key = '123'

from pages.assignment4.assignment4 import assignment4
app.register_blueprint(assignment4)

@app.route('/')
def mainHome():
    session['INSERTED'] = False
    session['DELETED'] = False
    session['UPDATE'] = False
    return render_template('Home.html')

@app.route('/usersList')
def users_list():
    session['UPDATE'] = False
    session['INSERTED'] = False
    session['DELETED'] = False
    return render_template('users_list.html')


@app.route('/Home')
def home():
    session['UPDATE'] = False
    session['INSERTED'] = False
    session['DELETED'] = False
    customer_registrated = True ##For now, currently no entry restriction
    if customer_registrated:
        return redirect(url_for("assignment3_1"))
    else:
        return 'You have to log-In'

@app.route('/Contact_Us')
def about():
    session['UPDATE'] = False
    session['INSERTED'] = False
    session['DELETED'] = False
    return render_template('Contact_Us.html')


@app.route('/assignment3_1')
def assignment3_1():
    session['UPDATE'] = False
    session['INSERTED'] = False
    session['DELETED'] = False
    return render_template('assignment3_1.html', user={'firstname': "דן", 'lastname': "ישראלי", 'gender': "m"},
                            Details=['29', 'עמק חפר','ישראל'], newFeed='בקרוב באתר, הקרמשניט המפורסם של סבתא רוזליה')

    @app.route('/assignment3_2', methods=['GET', 'POST'])
    def go_to_assignment3_2():
        session['INSERTED'] = False
        session['DELETED'] = False
        session['UPDATE'] = False
    return render_template('assignment3_2.html', parameters=request.args)




@app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2():
    session['INSERTED'] = False
    session['DELETED'] = False
    session['UPDATE'] = False
    return render_template('assignment3_2.html')



@app.route('/search')
def search_form():
    users = [
        {
            "user_id": "1",
            "user_nickname": "Adamico",
            "user_email": "adam.levin@reqres.in",
            "user_first_name": "Adam",
            "user_last_name": "Levin",
            "user_password": "12345678",
            "user_avatar": "https://static01.nyt.com/images/2018/07/08/fashion/05LIST-INYT2/05LIST-INYT2-superJumbo.jpg?quality=75&auto=webp"
        },
        {
            "user_id": "2",
            "user_nickname": "Galush",
            "user_email": "gal.gadot@reqres.in",
            "user_first_name": "Gal",
            "user_last_name": "Gadot",
            "user_password": "87654321",
            "user_avatar": "https://media.todaybirthdays.com/1985/04/30/gal-gadot.jpg"
        },
        {
            "user_id": "3",
            "user_nickname": "Billush",
            "user_email": "billie.elish@reqres.in",
            "user_first_name": "Billie",
            "user_last_name": "Eilish",
            "user_password": "12345673",
            "user_avatar": "https://media.todaybirthdays.com/2021/03/03/billie-eilish.jpg"
        },
        {
            "user_id": "4",
            "user_nickname": "Danush",
            "user_email": "dana.international@reqres.in",
            "user_first_name": "Dana",
            "user_last_name": "Internatinal",
            "user_password": "12345679",
            "user_avatar": "https://images.maariv.co.il/image/upload/f_auto,fl_lossy/c_fill,g_faces:center,w_948/522954"
        },
        {
            "user_id": "5",
            "user_nickname": "Naftul",
            "user_email": "naftali.benette@reqres.in",
            "user_first_name": "Naftali",
            "user_last_name": "Benette",
            "user_password": "12345678",
            "user_avatar": "https://www.gov.il/BlobFolder/roleholder/bennett/he/%D7%91%D7%A0%D7%982.jpg"
        },
        {
            "user_id": "6",
            "user_nickname": "Lirani",
            "user_email": "liran.Hultza-Afora@reqres.in",
            "user_first_name": "Liran",
            "user_last_name": "Hultza-Afora",
            "user_password": "12344678",
            "user_avatar": "https://img.mako.co.il/2014/08/13/boker_keshet_130814_liran_i.jpg"
        }
    ]
    if 'searchinput' in request.args:
        search = request.args['searchinput']
    else:
        search = ""
    if search == "":
        return render_template('assignment3_2.html', search=users)
    flag = False
    for user in users:
        if user['user_first_name'] == search or user['user_email'] == search:
            flag = True
            return render_template('assignment3_2.html', searchIsfound=user)
    if not flag:
        return render_template('assignment3_2.html', searchNotfound="Item not found!")


@app.route('/register', methods=['POST'])
def register_form():
    if 'username' in request.form:
        user_name = request.form['user_first_name']
        user_nickname = request.form['user_nickname']
    else:
        user_first_name, user_nickname = '', '', '', ''
    session['user_first_name'] = user_first_name
    session['user_nickname'] = user_nickname
    return render_template('assignment3_2.html', user_first_name=user_first_name, user_nickname=user_nickname)


@app.route('/logout')
def logout():
    if 'user_first_name' in session:
        session.pop('user_first_name', None)
        session.pop('user_nickname', None)
        return redirect(url_for('assignment3_2'))



##-----------------------------------------------assignment_4------------------------------------#


# ----------------------------------- PART B --------------------------------------




@app.route('/assignment4/outer_source')
def assignmen4_2_def():
    return render_template('assignment4_2.html')



@app.route('/assignment4/outer_source/json')
def assignment4_2_def_json():
    number = request.args['number']
    res = requests.get("https://reqres.in/api/users/{}".format(number))
    response = jsonify(res.json())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/assignment4/users')
def assignment4_2_users_def():
        query = 'select  user_id, user_nickname, user_first_name, user_last_name, user_email from users;'
        users = interact_db(query=query, query_type='fetch')
        response = []
        for user in users:
            response.append({
                "user_id": user[0],
                "user_nickname": user[1],
                "user_first_name": user[2],
                "user_last_name": user[3],
                "user_email": user[4]
            })
        return jsonify(users)
        #return render_template('users.html', users=json.dumps(response))




@app.route('/assignment4_3/restapi/', defaults={'user_id':1})
@app.route('/assignment4_3/restapi/<int:user_id>')
def get_users_def(user_id):
    query = 'select  user_id,user_nickname,user_first_name,user_last_name,user_email from users where user_id=%s;' % user_id
    query_result = interact_db(query=query, query_type='fetch')
    response = "User doesn't exist. Please enter a correct id!"
    if len(query_result) != 0:
        response = query_result
        response = jsonify(response)
    return response



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



if __name__ == "__main__":
    app.run()
