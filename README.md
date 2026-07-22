# Template Backend Mini Project FastAPI

# Description
Project ini digunakan sebagai template pembuatan backend menggunakan FastAPI

# Tech Stack
Python version: 3.9.0
Server: FastAPI
Database: MongoDB (Default)

# Installation
install project dengan command berikut:

\`\`\`python
# Install dependencies
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# Running project
uvicorn app.main:app --reload

Setelah aplikasi berjalan, akses Swagger di:
Open http://localhost:8000/docs

# Folder Structure

app/core:
Berisi komponen inti aplikasi seperti:
-Koneksi database
-Konfigurasi (.env, settings)
-Logging
-Limiter, dll
