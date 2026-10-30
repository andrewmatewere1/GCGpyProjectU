# GCG Student Registration

A Flask student management application with user authentication and student record management.

## Features

- Create a user account from the sign-up panel
- Sign in using an email address or username
- Securely store passwords using Werkzeug password hashing
- Register new student records
- Search all student records
- Search students by roll number, first name, last name, age, gender, email, or phone number
- Log out of the application

## Requirements

- Windows
- Python 3.10 or newer
- Flask
- Flask-Login
- Flask-SQLAlchemy

## Installation

1. Open PowerShell in the project directory.

2. Create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Running the Application

Start the Flask development server:

```powershell
python main.py
```

Open the application in a browser:

```text
http://127.0.0.1:5000/auth/login
```

The home route is protected, so users must sign in before accessing it.

## Creating an Account

1. Open the sign-in page.
2. Select **Sign Up**.
3. Enter a username, email address, and password.
4. Select **Register**.
5. Sign in using either the username or email address and password.

The account is stored in the `user` table in the SQLite database. Passwords are hashed before they are stored.

## Using the Application

After signing in, use the home page to:

- Register a student
- Search for students
- Log out

Student registration requires:

- First name
- Last name
- Roll number
- Age
- Email address
- Phone number
- Gender

Names must contain at least three characters. Roll numbers must contain exactly five characters, phone numbers must contain exactly ten digits, and registered ages must be at least 18.

## Main Routes

| Route | Access | Description |
|---|---|---|
| `/auth/login` | Public | Sign in and display the account form |
| `/auth/register-user` | Public | Create a new user account |
| `/auth/logout` | Logged in | Sign out of the application |
| `/` | Logged in | Home page and main menu |
| `/auth/sign-up` | Logged in | Register a student |
| `/search` | Logged in | Display and search all students |
| `/search-s` | Logged in | Search students by entered information |

## Database

The application uses SQLite through Flask-SQLAlchemy.

The database tables are:

- `user` - authentication accounts
- `student` - registered student records

The application database is located under the project's `instance` directory.

## Project Structure

```text
GCGpyProjectU/
|-- main.py
|-- requirements.txt
|-- instance/
|   `-- database.db
`-- website/
    |-- __init__.py
    |-- auth.py
    |-- models.py
    |-- views.py
    |-- static/
    |   |-- scripts/
    |   `-- stylesheet/
    `-- templates/
```
