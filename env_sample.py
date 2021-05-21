import os

os.environ.setdefault("IP", "0.0.0.0.")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "any_secret_key")
os.environ.setdefault("DEBUG", "True")  # False after deployed
os.environ.setdefault("DEVELOPMENT", "True")  # only when working locally
os.environ.setdefault("DB_URL", "postgresql:///taskmanager")  # only when working locally
