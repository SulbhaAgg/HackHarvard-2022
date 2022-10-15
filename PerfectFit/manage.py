#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import django
import sys
import logging
import os
import psycopg
from psycopg.errors import ProgrammingError

def exec_statement(conn, stmt):
    try:
        with conn.cursor() as cur:
            cur.execute(stmt)
            row = cur.fetchone()
            conn.commit()
            if row: print(row[0])
    except ProgrammingError:
        return


def main():

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PerfectFit.settings')
    try:

        from django.core.management import execute_from_command_line
        # Connect to CockroachDB
        connection = psycopg.connect("postgresql://sulbha:Pmo-LxUwu6LMUsKHkmRS2w@free-tier11.gcp-us-east1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dchasm-bleater-2370"
        , application_name="$ docs_quickstart_python")

        statements = [
            # Clear out any existing data
            "DROP TABLE IF EXISTS messages",
            # CREATE the messages table
            "CREATE TABLE IF NOT EXISTS messages (id UUID PRIMARY KEY DEFAULT gen_random_uuid(), message STRING)",
            # INSERT a row into the messages table
            "INSERT INTO messages (message) VALUES ('Hello world!')",
            # SELECT a row from the messages table
            "SELECT message FROM messages"
        ]

        for statement in statements:
            exec_statement(connection, statement)

        # Close communication with the database
            connection.close()
    

        
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()