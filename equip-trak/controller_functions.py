from flask import Flask, render_template, redirect, request, flash, session
from config import app
from mysqlconnection import MySQLConnection
from validate_email import validate_email
from flask_bcrypt import Bcrypt

app.secret_key = 'shhdonttellanyone'
bcrypt = Bcrypt(app)


def root():
    return render_template('index.html')


def register():
    return render_template('addUser.html')


def login():
    mySql = MySQLConnection('equip-trak')
    query = 'SELECT * FROM users WHERE user_name = %(user)s'
    data = {'user': request.form['userName']}
    pw_hash = mySql.query_db(query, data)
    if pw_hash:
        pw_hash = pw_hash[0]
    session['userId'] = pw_hash['id']
    session['fName'] = pw_hash['first_name']
    session['lName'] = pw_hash['last_name']
    session['email'] = pw_hash['email']
    if bcrypt.check_password_hash(
            pw_hash['password'], request.form['password']):
        session['login'] = True
        return redirect('/checkout')
    else:
        flash('Wrong Password')
    return redirect('/')


def addUser():
    session['fName'] = request.form['firstName']
    session['lName'] = request.form['lastName'],
    session['email'] = request.form['email']
    session['user_name'] = request.form['userName']

    is_valid = True
    if len(request.form['firstName']) < 1:
        flash("Please enter in your First Name")
    elif not request.form['firstName'].isalpha():
        is_valid = False
        flash('First Name is not a valid entry')

    if len(request.form['lastName']) < 1:
        flash("Please enter in your Last Name")
    elif not request.form['lastName'].isalpha():
        is_valid = False
        flash('Last Name is not a valid entry')

    if not validate_email(request.form['email']):
        is_valid = False
        flash('Please enter in a valid email.')

    if is_valid:
        mySql = MySQLConnection('equip-trak')
        query = 'SELECT count(user_name) as "UserCreated" FROM users WHERE user_name = %(user)s'
        data = {'user': request.form['email']}
        UserCreated = mySql.query_db(query, data)
        UserCreated = UserCreated[0]['UserCreated'] > 0
    if UserCreated:
        is_valid = False
        flash('Email has been taken, please use a different email.')

    SpecialSym = ['$', '@', '#', '%', '!', '^', '&', '*', '(', ')']
    if len(request.form['pw1']) < 5:
        flash("Please enter a password with 5 or more characters")
        is_valid = False
    elif request.form['pw1'] != request.form['pw2']:
        flash('Your passwords does not match')
        is_valid = False
    elif len(request.form['pw1']) < 6:
        flash('length should be at least 6')
        is_valid = False
    elif len(request.form['pw1']) > 20:
        flash('length should be not be greater than 20')
        is_valid = False
    elif not any(char.isdigit() for char in request.form['pw1']):
        flash('Password should have at least one numeral')
        is_valid = False
    elif not any(char.isupper() for char in request.form['pw1']):
        flash('Password should have at least one uppercase letter')
        is_valid = False
    elif not any(char.islower() for char in request.form['pw1']):
        flash('Password should have at least one lowercase letter')
        is_valid = False
    elif not any(char in SpecialSym for char in request.form['pw1']):
        flash('Password should have at least one of the symbols $@#')
        is_valid = False

    if is_valid:
        mySql = MySQLConnection('equip-trak')
        query = 'INSERT INTO users (first_name, last_name, email, password, user_name, created_on, updated_on) ' +\
            'VALUES (%(fn)s, %(ln)s, %(em)s, %(pw)s, %(un)s,  now(), now())'
        pw = bcrypt.generate_password_hash(request.form['pw1'])

        data = {'fn': request.form['firstName'], 'ln': request.form['lastName'],
                'em': request.form['email'], 'pw': pw, 'un': request.form['userName']}
        mySql.query_db(query, data)
        flash('User created!')
        return redirect('/')

    return redirect('/register')


def checkUser():
    print("*"*50)
    found = False
    mySql = MySQLConnection('equip-trak')
    query = 'select * from users WHERE user_name = %(un)s'
    data = {'un': request.form['user_name']}
    result = mySql.query_db(query, data)
    if result:
        found = True
    return render_template('partials/username.html', found=found)


def nav():
    print("Working")
    return render_template('partials/nav.html')


def newEquip():
    return render_template('addEquipment.html')


def addEquipment():
    mySql = MySQLConnection('equip-trak')
    query = 'INSERT INTO equipments (equip_id, model, manufacturer, serial, created_on, updated_on) VALUES( %(eq)s, %(md)s, %(man)s, %(ser)s, now(), now())'
    data = {'eq': request.form['equipId'], 'md': request.form['model'],
            'man': request.form['manufacturer'], 'ser': request.form['serial']}
    mySql.query_db(query, data)
    return redirect('/checkout')


def checkoutPage():
    mySql = MySQLConnection('equip-trak')
    query = 'select * from equipments ORDER BY equip_id'
    equip = mySql.query_db(query)
    mySql = MySQLConnection('equip-trak')
    query = 'select * from conditions'
    con = mySql.query_db(query)
    return render_template('/checkout.html', equip=equip, conditions=con)


def equipments():
    mySql = MySQLConnection('equip-trak')
    query = 'select equipments.id as ID, equipments.equip_id as "Equipment ID", manufacturer, model, serial, first_name, last_Name, transactions.checkout_time from equipments LEFT JOIN (select equip_id, max(transactions.id) as last_trans FROM equipments LEFT JOIN transactions on equipments.id = equipments_id GROUP BY equip_id) as lastTrans ON equipments.equip_id = lastTrans.equip_id LEFT JOIN transactions ON transactions.id = lastTrans.last_trans LEFT JOIN users on users.id = transactions.checkout_user_id'
    myEquip = mySql.query_db(query)
    return render_template('/equipments.html', equip=myEquip)


def equipmentDetails(myId):
    mySql = MySQLConnection('equip-trak')
    query = 'select * from equipments WHERE id = %(id)s'
    data = {'id': myId}
    equip = mySql.query_db(query, data)
    return render_template('/equipmentDetails.html', equip=equip)


def getEquip():
    print(request.form)
    mySql = MySQLConnection('equip-trak')
    query = 'select * from equipments left join status on status_id = status.id  WHERE equip_id	= %(eId)s'
    data = {'eId': request.form['equipId']}
    results = mySql.query_db(query, data)
    results = results[0]
    print(results)
    if results['status.id'] == 1:
        mySql = MySQLConnection('equip-trak')
        query = 'select * from transactions LEFT JOIN users ON users.id = checkout_user_id WHERE equipments_id= %(eId)s and isnull(checkin_user_id)'
        data = {'eId': results['id']}
        trans = mySql.query_db(query, data)
        trans = trans[0]
    else:
        trans = ''
        print('trans empty', trans)

    return render_template('partials/checkout.html', equip=results, trans=trans)


def users():
    mySql = MySQLConnection('equip-trak')
    query = 'select * from users'
    users = mySql.query_db(query)
    return render_template('/users.html', users=users)


def userDetails(userId):
    mySql = MySQLConnection('equip-trak')
    query = 'select * from users WHERE id = %(id)s'
    data = {'id': userId}
    user = mySql.query_db(query, data)
    return render_template('/userDetails.html', user=user)


def transaction():
    return render_template('/transactionDetail.html')


def equipOut():
    print(request.form)
    mySql = MySQLConnection('equip-trak')
    query = 'INSERT INTO transactions (equipments_id, checkout_user_id, checkout_condition_id, checkout_comment, checkout_time, created_on, updated_on) VALUES (%(eId)s, %(uId)s, %(con)s, %(com)s, now(), now(), now())'
    # %(eId)s, %(uId)s, %(con)s, %(com)s
    data = {'eId': request.form['equipId'], 'uId': request.form['userId'],
            'con': request.form['conditions'], 'com': request.form['comments']}
    mySql.query_db(query, data)
    print("*"*60)
    mySql = MySQLConnection('equip-trak')
    query = 'UPDATE equipments SET status_id = 1 WHERE id = %(eId)s'
    # data = {'eId': request.form['equipId']}
    mySql.query_db(query, data)
    return redirect('/checkout')


def equipIn():
    mySql = MySQLConnection('equip-trak')
    query = 'UPDATE transactions SET checkin_user_id = %(uId)s, checkin_condition_id = %(con)s, checkin_comment = %(com)s, checkin_time=now(), updated_on=now() WHERE id = %(tId)s'
    data = {'eId': request.form['equipId'], 'uId': request.form['userId'],
            'con': request.form['conditions'], 'com': request.form['comments'], 'tId': request.form['trans_id']}
    mySql.query_db(query, data)
    print("*"*60)
    mySql = MySQLConnection('equip-trak')
    query = 'UPDATE equipments SET status_id = 2 WHERE id = %(eId)s'
    # data = {'eId': request.form['equipId']}
    mySql.query_db(query, data)
    return redirect('/checkout')
