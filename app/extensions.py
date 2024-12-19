import psycopg2
from flask_jwt_extended import JWTManager

jwt = JWTManager()

DB_CONFIG = {
    'host': 'autorack.proxy.rlwy.net',
    'port': '56784',
    'database': 'railway',
    'user': 'postgres',
    'password': 'EfOFAAZabDkkMOuuBrvHpwFILlrPUsHF'
}

def get_db_connection():
    connection = psycopg2.connect(
        dbname=DB_CONFIG['database'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port']
    )
    return connection

def execute_query(query, params=None):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            connection.commit()
            return cursor.fetchall()
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        connection.close()

query = "SELECT * FROM public.items LIMIT 5"
result = execute_query(query)
print(result)