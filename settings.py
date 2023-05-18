from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Инициализируем приложение Flask
app = Flask(__name__, template_folder="templates")

# Создаем DSN для СУБД в конфигурации Flask app
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://sveta:0310@localhost:5432/sv"

# Обязательно
app.secret_key = "0jd092190d09120edj=23124234o"

# Создаем объект для работы с SQLAlchemy
db = SQLAlchemy(app)
