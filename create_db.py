from app import app, db
from models import Student, Major, User
from werkzeug.security import generate_password_hash
import datetime as dt

with app.app_context():
    db.drop_all()
    db.create_all()

    # Initial loading of majors
    majors = ['Accounting', 'Finance', 'Information Systems', 'International Business', 'Management', \
              'Operations Management & Business Analytics', 'Supply Chain Management']
    for each_major in majors:
        print(each_major)
        a_major = Major(major=each_major)
        db.session.add(a_major)
        db.session.commit()

    # Initial loading of students
    students = [
        {'first_name': 'Robert', 'last_name': 'Smith', 'major_id': 3,
         'birth_date': dt.datetime(2007, 6, 1), 'is_honors': 1},
        {'first_name': 'Leo', 'last_name': 'Van Munching', 'major_id': 6,
         'birth_date': dt.datetime(2008, 3, 24), 'is_honors': 0},
        {'first_name': 'Zachary', 'last_name': 'Byank', 'major_id': 3,
         'birth_date': dt.datetime(2004, 1, 1), 'is_honors': 0,
         'email': 'zbyank@terpmail.umd.edu'},
    ]

    for each_student in students:
        print(f'{each_student["first_name"]} {each_student["last_name"]} inserted into Student')
        a_student = Student(first_name=each_student["first_name"], last_name=each_student["last_name"],
                            major_id=each_student["major_id"], birth_date=each_student["birth_date"],
                            is_honors=each_student["is_honors"],
                            email=each_student.get("email"))
        db.session.add(a_student)
        db.session.commit()

    # Initial loading of users
    users = [
        {'username': 'zbyank', 'first_name': 'Zachary', 'last_name': 'Byank',
         'email': 'zbyank@terpmail.umd.edu',
         'password': generate_password_hash('zbyank'),
         'role': 'STUDENT'},
        {'username': 'admin', 'first_name': 'Site', 'last_name': 'Admin',
         'email': 'admin@umd.edu',
         'password': generate_password_hash('adminpw'),
         'role': 'ADMIN'},
        {'username': 'manager', 'first_name': 'Site', 'last_name': 'Manager',
         'email': 'manager@umd.edu',
         'password': generate_password_hash('managerpw'),
         'role': 'MANAGER'},
    ]

    for each_user in users:
        print(f'{each_user["first_name"]} {each_user["last_name"]} inserted into User')
        a_user = User(username=each_user["username"], first_name=each_user["first_name"],
                      last_name=each_user["last_name"], email=each_user["email"],
                      password=each_user["password"], role=each_user["role"])
        db.session.add(a_user)
        db.session.commit()