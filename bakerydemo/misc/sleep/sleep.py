from django.db import connection

def sleep():
    with connection.cursor() as cursor:
        cursor.execute("SELECT pg_sleep(2);")