from flask import Flask, render_template, redirect, request
from config import db
from models import User, Equipment, Status, Admin, Condition, Transaction


def root():
    # dojoList = Dojo.query.all()
    return render_template('index.html')


def register():
    return render_template('addUser.html')


def addUser():
    print('request', request.form)
    newUser = User(
        first_name=request.form['firstName'],
        last_name=request.form['lastName'],
        email=request.form['email'],
        user_name=request.form['userName'],
        password=request.form['pw1'])

    print(newUser)
    db.session.add(newUser)
    db.session.commit()
    return redirect('/')


def checkUser():
    print("*"*50)
    found = False
    result = User.query.filter_by(user_name=request.form['userName']).first()
    print('results', result)
    print("*"*50)
    if result:
        found = True
    return render_template('partials/username.html', found=found)


def nav():
    print("Working")
    return render_template('partials/nav.html')


def newEquip():
    return render_template('addEquipment.html')


def addEquipment():
    newEquip = Equipment(
        equip_id=request.form['equipId'],
        manufacture=request.form['manufacture'],
        model=request.form['model'],
        serial=request.form['serial']
    )
    db.session.add(newEquip)
    db.session.commit()
    return redirect('/')


def checkoutPage():
    equip = Equipment.query.all()
    con = Condition.query.all()
    print("*"*50)
    print('equip', equip)
    print('conditions', con)
    print("*"*50)
    return render_template('/checkout.html', equip=equip, conditions=con)


def equipments():
    equip = Equipment.query.all()
    return render_template('/equipments.html', equip=equip)


def equipmentDetails():
    return render_template('/equipmentDetails.html')


def users():
    return render_template('/users.html')


def userDetails():
    return render_template('/userDetails.html')


def transaction():
    return render_template('/transactionDetail.html')
