# Course Registration System

A **Django-based web application** that allows users (students and administrators) to manage course registration efficiently.  
This project demonstrates key Django concepts such as models, views, templates, authentication, and CRUD operations.

---

## Features

✅ User authentication (login, logout, register)  
✅ Students can view available courses  
✅ Students can register or unregister for courses  
✅ Admin users can add, edit, and delete courses  
✅ Search functionality for courses  
✅ Responsive design with dynamic templates  

---

## Tech Stack

- **Python 3.10+**
- **Django 5.x**
- **SQLite3** (default database)
- **HTML5 / CSS3 / Bootstrap**
- **Git & GitHub** for version control

---

## Installation & Setup

Follow these steps to run the project locally 👇

### 1️ Clone the Repository
```bash
git clone https://github.com/musahhabib04/course_registration.git
cd course_registration
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv venv
# Activate:
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Mac/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```

🌐 Visit the app in your browser:  
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Folder Structure

```
course_registration/
│
├── accounts/              # User authentication (login, register, logout)
├── courses/               # Course management app
├── course_registration/   # Main project folder (settings, URLs, WSGI)
├── templates/             # HTML templates
├── static/                # CSS, JS, and images
├── db.sqlite3             # SQLite database
├── manage.py              # Django CLI entry point
└── requirements.txt       # Python dependencies
```

---

## Future Enhancements

- Add user roles (Student, Instructor, Admin)
- Course categories and prerequisites
- Enrollment analytics dashboard
- Email notifications for registration updates

---

## Author

**Habib Musah**  
💼 [LinkedIn](https://www.linkedin.com/in/habib-musah-5498bb161)  
💻 [GitHub](https://github.com/musahhabib04)

---

⭐ *If you like this project, give it a star on GitHub!*  
🖤 Built with passion using Django & Python.
