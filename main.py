import psycopg2
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)    

# COnnect to the database
def connect():
    try:
        connection = psycopg2.connect(
            password = "password",
            host = "localhost",
            port = 5432,
            database = "postgres",
            user = "postgres"
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        logger.error("Error while connecting to PostgreSQL", error)
        return None
    

# List available databases
def list_databases(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
        databases = cursor.fetchall()
        logger.info("Available databases:")
        for db in databases:
            logger.info(db[0])
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        logger.error("Error while listing databases", error)

# List available databases
def list_databases(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
        databases = cursor.fetchall()
        logger.info("Available databases:")
        for db in databases:
            logger.info(db[0])
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        logger.error("Error while listing databases", error)

if __name__ == "__main__":
    connection = connect()
    if connection:
        logger.info("Connected to PostgreSQL")
        list_databases(connection)
        connection.close()
    else:
        logger.error("Failed to connect to PostgreSQL")