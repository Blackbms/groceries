from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                user=os.getenv("DB_USER", "postgres"),
                password=os.getenv("DB_PASSWORD", "password"),
                host=os.getenv("DB_HOST", "localhost"),
                port=os.getenv("DB_PORT", "5432"),
                database=os.getenv("DB_NAME", "postgres")
            )
            logger.info("Connected to PostgreSQL")
        except (Exception, psycopg2.Error) as error:
            logger.error("Error while connecting to PostgreSQL", error)

    def close(self):
        if self.connection:
            self.connection.close()
            logger.info("Connection to PostgreSQL closed")

    def create_item(self, item_name):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO items (name) VALUES (%s)", (item_name,))
            self.connection.commit()
            cursor.close()
            logger.info(f"Item '{item_name}' created successfully")
        except (Exception, psycopg2.Error) as error:
            logger.error("Error while creating item", error)

    def list_items(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, name FROM items")
            items = cursor.fetchall()
            cursor.close()
            return items
        except (Exception, psycopg2.Error) as error:
            logger.error("Error while listing items", error)
            return []

    def purge_tables(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
            self.connection.commit()
            cursor.close()
            logger.info("All tables purged successfully")
        except (Exception, psycopg2.Error) as error:
            logger.error("Error while purging tables", error)

@app.route('/')
def index():
    db = Database()
    db.connect()
    items = db.list_items()
    db.close()
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['POST'])
def add_item():
    item_name = request.form['item_name']
    db = Database()
    db.connect()
    db.create_item(item_name)
    db.close()
    return redirect(url_for('index'))

@app.route('/purge_tables', methods=['POST'])
def purge_tables():
    db = Database()
    db.connect()
    db.purge_tables()
    db.close()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')