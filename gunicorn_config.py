from dotenv import load_dotenv
from os import environ

load_dotenv()

# Get the PORT environment variable and convert it to an integer with a default value of 8000
port = int(environ.get("PORT", 8000))

workers = 4
bind = f"127.0.0.1:{port}"
worker_class = "uvicorn.workers.UvicornWorker"

# gunicorn -c gunicorn_config.py app:app
