# Assignment-for-Backend-Developer-Intern
FastAPI To-Do List Application
This project is a simple RESTful API built with FastAPI and SQLite to manage a "To-Do List". It allows users to create, read, update, and delete to-do items. The project is designed to meet assignment requirements while also being easy to understand and use.

Project Setup
1. Clone the Repository
First, clone this repository to your local machine:
git clone https://github.com/Jeevan-S1008/Assignment-for-Backend-Developer-Intern

cd dirextory name
2. Set Up a Virtual Environment (optional but recommended)
Setting up a virtual environment helps isolate dependencies for this project:

python3 -m venv venv
`venv\Scripts\activate`
3. Install Required Packages
Install FastAPI, Uvicorn, and SQLAlchemy:

pip install fastapi[all] uvicorn sqlalchemy

4. Run the Application
Use Uvicorn to start the FastAPI server on your local machine:

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

The app should now be running at http://127.0.0.1:8000.

