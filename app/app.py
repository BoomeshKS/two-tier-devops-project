from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    "host": os.getenv("DB_HOST", "db"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "root"),
    "database": os.getenv("DB_NAME", "myapp")
}

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hello from Flask and MySQL'")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0]
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
