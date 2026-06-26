# single-student-api-fastapi
A simple FastAPI project to fetch a single student's details using a dynamic path parameter.

# 👨‍🎓 Single Student API using FastAPI

## 📌 Project Description

This is a simple FastAPI project that returns the details of a single student using a dynamic path parameter.

The user provides a student ID in the URL, and the API returns the corresponding student's information.

---

## 🚀 Features

- FastAPI
- GET Method
- Dynamic Path Parameter
- Dictionary Data
- JSON Response

---

## 📂 Endpoint

GET /students/{id}

Example:

/students/1

---

## 📤 Sample Response

```json
{
    "id": 1,
    "name": "Ali",
    "age": 20,
    "department": "Computer Science"
}
```

---

## 📤 If Student Not Found

```json
{
    "message": "Student not found"
}
```

---

## 🛠️ Technologies Used

- Python
- FastAPI
- Uvicorn

---

## ▶️ Run the Project

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 👨‍💻 Author

Ghansham Das
