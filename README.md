# Flask Notes App

The Flask Notes App is a simple web application built with Flask, Flask-Login, Flask-SQLAlchemy, and Bootstrap. It allows users to sign up, log in, add new notes, and delete their own notes. Here's how the project works and what it does:

## How It Works

1. Users can sign up or log in to access the app.
2. Upon signing up or logging in, users are redirected to the home page.
3. The home page displays a list of the user's notes, if any.
4. Users can add a new note by entering text in the provided textarea and clicking the "Save" button.
5. To delete a note, users can click the "X" button next to the respective note.
6. If a note is too short (less than 1 character), an error message will be displayed.
7. Users can log out by clicking the "Logout" link in the navigation bar.

## What It Does

The Flask Notes App provides a user-friendly interface for managing notes. It allows users to:

- Create an account and securely log in.
- View their existing notes on the home page.
- Add new notes with a minimum length check.
- Delete their own notes.
- Receive flash messages for success and error notifications.
- The app ensures that users can only access their own notes, enhancing data privacy and security.

The project is a useful starting point for building more complex web applications with Flask, and it demonstrates the integration of Flask extensions like Flask-Login for user authentication and Flask-SQLAlchemy for database management.


## File Structure

```
flask-notes-app/
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── models.py
│   └── views.py
├── static/
│   └── js/
│       └── index.js
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   └── sign-up.html
└── database.db
```


## Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, feel free to open an issue or submit a pull request.

