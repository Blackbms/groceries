import psycopg2
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                user="postgres",
                password="password",
                host="localhost",
                port="5432",
                database="postgres"
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
            logger.info("Available items:")
            for item in items:
                logger.info(f"ID: {item[0]}, Name: {item[1]}")
            cursor.close()
        except (Exception, psycopg2.Error) as error:
            logger.error("Error while listing items", error)

if __name__ == "__main__":
    db = Database()
    db.connect()
    db.create_item("Eggs")
    db.list_items()
    db.close()