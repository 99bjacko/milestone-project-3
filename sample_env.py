import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "users-secret-key")
os.environ.setdefault("MONGO_URI", "users-mongo-URI")
os.environ.setdefault("MONGO_DBNAME", "users-db-name")