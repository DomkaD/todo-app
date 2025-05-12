# Todo App – Backend API

This is a backend API for a mobile app where **parents assign tasks to their children** and track their completion and rewards.

## 🚀 Features

- JWT authentication system (parent-child model)
- Task creation, editing, status updates
- Automatic reward calculation for completed tasks
- Role-based access: parents vs children
- PostgreSQL database with SQLAlchemy ORM
- FastAPI async architecture
- Redis for caching and performance
- Dockerized for easy deployment

## 🛠 Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Redis
- Docker
- Git/GitHub

## 📁 Project Structure

```
todo/
├── app/
│   ├── main.py
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── services/
│   └── auth/
├── tests/
├── requirements.txt
└── Dockerfile
```

## ⚙️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/your_username/todo-app.git
cd todo-app
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root folder:

```
DATABASE_URL=postgresql://username:password@localhost:5432/todo
SECRET_KEY=your_jwt_secret
ALGORITHM=HS256
```

### 5. Run the app

```bash
uvicorn app.main:app --reload
```

API will be available at:  
http://localhost:8000/docs

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📦 Docker

```bash
docker build -t todo-api .
docker run -d -p 8000:8000 todo-api
```

---

## ✅ To Do

- Add role-based permissions
- Add email notifications
- Improve test coverage
- Frontend integration

---

## 📄 License

MIT License
