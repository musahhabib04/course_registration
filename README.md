# course_registration
# Course Registration System (Django Project)

This is a Django-based web application that allows users (students and administrators) to manage course registration.  
It is designed to demonstrate core Django concepts such as models, views, templates, and authentication.


## Features

-  User authentication (login, logout, register)
-  Students can view available courses
-  Students can register or unregister for courses
-  Admin users can add, edit, and delete courses
-  Search functionality for courses
-  Dynamic templates with responsive design


## Tech Stack

- **Python 3.10+**
- **Django 5.x**
- **SQLite3** (default database)
- **HTML5 / CSS3 / Bootstrap**
- **Git & GitHub** for version control

---

## Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/musahhabib04/course_registration.git
cd course_registration
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a superuser (admin)
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server
```bash
python manage.py runserver
```

Now open your browser and go to: `http://127.0.0.1:8000/`



##  Future Enhancements

- Add user roles (Student, Instructor, Admin)
- Course categories and prerequisites
- Enrollment analytics dashboard
- Email notifications for registration updates

---

## Author

**Habib Musah**  
- 🌍 [LinkedIn](https://www.linkedin.com/in/habib-musah-5498bb161)  
- 💻 [GitHub](https://github.com/musahhabib04)


