# 🏥 Django Healthcare Backend API

A secure and RESTful backend system for a healthcare application using **Django**, **Django REST Framework**, **PostgreSQL**, and **JWT authentication**. This system supports user registration, login, and full CRUD operations for patients and doctors, including a patient-doctor mapping feature.

---

## 🎯 Objective

Build a backend system that:

- Registers and authenticates users using JWT.
- Allows authenticated users to manage (add, edit, delete, view) patient and doctor records.
- Enables assignment of doctors to patients.
- Uses environment variables for sensitive configurations.
- Stores data securely using PostgreSQL.

---

## 🛠️ Tech Stack

| Technology         | Purpose                        |
|--------------------|--------------------------------|
| Python             | Backend Language               |
| Django             | Web Framework                  |
| Django REST Framework | API Development             |
| PostgreSQL         | Database                       |
| Simple JWT         | Secure Authentication          |
| python-dotenv      | Environment Variable Management|
| venv               | Virtual Environment (Python)   |

---

## ⚙️ Project Setup (Windows)

Follow the steps below to set up the project locally on **Windows**:

### 1. Clone the Repository

```bash
git clone https://github.com/Mahvish16/HealthCare
cd healthcare-backend
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, you can manually create it with:

```bash
pip freeze > requirements.txt
```

Example contents:

```
Django>=4.0
djangorestframework
djangorestframework-simplejwt
psycopg2-binary
python-dotenv
```

### 4. Create `.env` File in Project Root

Create a file named `.env` in the root of your project and add the following environment variables:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True

DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

---

## 🔐 Authentication (JWT)

After logging in, you will receive:

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

Include the access token in headers for protected routes:

```
Authorization: Bearer <access_token>
```

---

## 🔗 API Endpoints

### 🔑 Authentication

| Method | Endpoint                | Description            |
|--------|-------------------------|------------------------|
| POST   | `/api/auth/register/`   | Register new user      |
| POST   | `/api/auth/login/`      | User login (get token) |

---

### 🧑‍⚕️ Patient APIs

| Method | Endpoint                   | Description                            |
|--------|----------------------------|----------------------------------------|
| POST   | `/api/patients/`           | Add a new patient (Auth required)      |
| GET    | `/api/patients/`           | Get all patients created by the user   |
| GET    | `/api/patients/<id>/`      | Get a specific patient by ID           |
| PUT    | `/api/patients/<id>/`      | Update a patient's details             |
| DELETE | `/api/patients/<id>/`      | Delete a patient                       |

---

### 👨‍⚕️ Doctor APIs

| Method | Endpoint                   | Description                            |
|--------|----------------------------|----------------------------------------|
| POST   | `/api/doctors/`            | Add a new doctor (Auth required)       |
| GET    | `/api/doctors/`            | Get all doctors created by the user    |
| GET    | `/api/doctors/<id>/`       | Get a specific doctor by ID            |
| PUT    | `/api/doctors/<id>/`       | Update a doctor's details              |
| DELETE | `/api/doctors/<id>/`       | Delete a doctor                        |

---

### 🔁 Patient-Doctor Mapping APIs

| Method | Endpoint                             | Description                                  |
|--------|--------------------------------------|----------------------------------------------|
| POST   | `/api/mappings/`                     | Assign a doctor to a patient                 |
| GET    | `/api/mappings/`                     | Get all patient-doctor mappings              |
| GET    | `/api/mappings/<patient_id>/`        | Get doctors assigned to a specific patient   |
| DELETE | `/api/mappings/<id>/`                | Remove doctor from a patient                 |

---

## ✅ Testing APIs

You can test APIs using:

- Postman
- Thunder Client
- curl or any HTTP client

Example header for authorized requests:

```
Authorization: Bearer your_access_token_here
```

---

## 📁 Project Structure

```
healthcare-backend/
├── core/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
├── healthcare_backend/
│   ├── settings.py
│   ├── urls.py
├── manage.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📄 .gitignore

```
*.pyc
__pycache__/
venv/
.env
backup
db.sqlite3
```

---


---

## 📜 License

This project is created for educational and showcasing purposes.

---

## 🚀 All Set! Happy Coding!
