from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User, Student, db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_or_email = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        user = User.query.filter(
            (User.email == username_or_email.lower()) |
            (User.firstname == username_or_email)
        ).first()

        if user:
            is_hashed = user.password.startswith(('scrypt:', 'pbkdf2:'))
            password_is_valid = (
                check_password_hash(user.password, password)
                if is_hashed
                else user.password == password
            )
            if password_is_valid:
                if not is_hashed:
                    user.password = generate_password_hash(password)
                    db.session.commit()
                login_user(user)
                flash('Login Successful', category='success')
                return redirect(url_for('views.home'))
            flash('Invalid Password', category='error')
        else:
            flash('User Does Not Exist!', category='error')

    return render_template("signIn-signUp.html")


@auth.route('/register-user', methods=['POST'])
def register_user():
    username = request.form.get('username', '').strip()
    email = request.form.get('mail', '').strip().lower()
    password = request.form.get('passwordR', '')

    if len(username) < 3:
        flash('Username must be at least 3 characters long', category='error')
    elif len(email) < 4 or '@' not in email:
        flash('Enter a valid email address', category='error')
    elif len(password) < 6:
        flash('Password must be at least 6 characters long', category='error')
    elif User.query.filter_by(email=email).first():
        flash('Email is already registered', category='error')
    elif User.query.filter_by(firstname=username).first():
        flash('Username is already registered', category='error')
    else:
        db.session.add(User(
            firstname=username,
            email=email,
            password=generate_password_hash(password)
        ))
        db.session.commit()
        flash('Account created successfully. You can now sign in.', category='success')

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
@login_required
def signup():
    if request.method == 'POST':
        email = request.form.get('mail')
        firstname = request.form.get('name')
        lastname = request.form.get('surname')
        rollnr = request.form.get('rollnr')
        gender = request.form.get('gender')
        phonenr = request.form.get('phonenr')
        age = request.form.get('age')

        email_inuse = Student.query.filter_by(email=email).first()
        rollnr_inuse = Student.query.filter_by(rollnr=rollnr).first()
        phonenr_inuse = Student.query.filter_by(phonenr=phonenr).first()

        if email_inuse:
            flash('Email Is Already In Use', category='error')
        elif phonenr_inuse:
            flash('Phone Number Already Exists', category='error')
        elif rollnr_inuse:
            flash('Roll Number Already Exists', category='error')
        elif len(firstname) < 3:
            flash('Name must be at least 3 characters long', category='error')
        elif any(char.isdigit() for char in firstname):
            flash('Enter Valid Name', category='error')
        elif len(lastname) < 3:
            flash('lastname must be at least 3 characters long', category='error')
        elif any(char.isdigit() for char in lastname):
            flash('Enter Valid lastname', category='error')
        elif len(rollnr) != 5:
            flash('Enter Valid Roll Number', category='error')
        elif gender == "":
            flash('Select a gender', category='error')
        elif len(email) < 4:
            flash('Enter Valid Email', category='error')
        elif len(phonenr) != 10:
            flash('Enter Valid Phone Number', category='error')
        elif int(age) < 18:
            flash('Oops you are too young', category='error')
        else:
            db.session.add(Student(
                firstname=firstname,
                lastname=lastname,
                rollnr=rollnr,
                gender=gender,
                email=email,
                phonenr=phonenr,
                age=age
            ))
            db.session.commit()
            flash('Student Info Registered Successfully', category='success')

    return render_template("register-student.html")
