from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required,login_user,logout_user, current_user
from .models import Student
##from flask import blueprint, render_template, request, redirect, url_for, flash 

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html')

@views.route('/search',methods=['GET','POST'])
@login_required
def students():
    # Query all student records
    students = Student.query.all()
    # Pass them to the template
    return render_template('searchstudent.html', details=students)

@views.route('/search-s', methods=['GET', 'POST'])
@login_required
def specific():
    students = []  # default empty

    if request.method == 'POST':
        data = request.form.get('data')

        if data:
            # Try matching roll number
            studentsroll = Student.query.filter(Student.rollnr.ilike(f"%{data}%")).all()
            if studentsroll:
                flash('Success! We got a roll-Number', category='success')
                return render_template('searchstudent.html', details=studentsroll)

            # Try matching firstname
            studentsname = Student.query.filter(Student.firstname.ilike(f"%{data}%")).all()
            if studentsname:
                flash('Success! We got First-Names', category='success')
                return render_template('searchstudent.html', details=studentsname)

            # Try matching lastname
            studentslastname = Student.query.filter(Student.lastname.ilike(f"%{data}%")).all()
            if studentslastname:
                flash('Success! We got last-Names', category='success')
                return render_template('searchstudent.html', details=studentslastname)

            # Try matching age
            studentsage = Student.query.filter(Student.age.ilike(f"%{data}%")).all()
            if studentsage:
                flash('Success! We got Ages', category='success')
                return render_template('searchstudent.html', details=studentsage)

            # Try matching gender
            studentsgender = Student.query.filter(Student.gender.ilike(f"%{data}%")).all()
            if studentsgender:
                flash('Success! We got Genders', category='success')
                return render_template('searchstudent.html', details=studentsgender)

            # Try matching email
            studentsemail = Student.query.filter(Student.email.ilike(f"%{data}%")).all()
            if studentsemail:
                flash('Success! We got Emails', category='success')
                return render_template('searchstudent.html', details=studentsemail)

            # Try matching phone number
            studentsphonenr = Student.query.filter(Student.phonenr.ilike(f"%{data}%")).all()
            if studentsphonenr:
                flash('Success! We got Mobile  Numbers', category='success')
                return render_template('searchstudent.html', details=studentsphonenr)

            # If no matches found
            flash('Student does not exist!', category='error')
        else:
            # Empty input: return all students
            flash('Failed to get student data', category='error')
            students = Student.query.all()

    return render_template('searchstudent.html', details=students)


    
   
        
        
    



