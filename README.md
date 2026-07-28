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

# Folder Structure

app/
-app/models: Tempat menyimpan struktur data yang dipakai untuk aplikasi.
-app/modules: Berisi alur atau proses aplikasi, dan di kelompokan berdasarkan fitur masing-masing.
-app/routes: Berisi definisi untuk semua endpoint API, jadi kalau ada request masuk diarahin dan ditentukan disini.
-app/main: File utama untuk menjalankan aplikasinya.