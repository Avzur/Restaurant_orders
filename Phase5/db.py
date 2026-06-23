import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "integration_DB",
    "user": "postgres",
    "password": "AYALA10"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def execute_query(sql, params=None, fetch=True):
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, params)
            if fetch:
                result = cur.fetchall()
                print(f"DEBUG execute_query result: {result}")
                return result
            conn.commit()
            return cur.rowcount
    except Exception as e:
        print(f"DEBUG ERROR: {e}")
        conn.rollback()
        raise e
    finally:
        conn.close()

def execute_many(sql, data):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.executemany(sql, data)
        conn.commit()
    finally:
        conn.close()

def call_procedure(sql, params=None):
    conn = get_connection()
    notices = []
    try:
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cur:
            cur.execute(sql, params)
            notices = conn.notices[:]
        return True, notices
    except Exception as e:
        return False, [str(e)]
    finally:
        conn.close()

def call_function(sql, params=None):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            result = cur.fetchone()
            return True, result[0] if result else None, conn.notices[:]
    except Exception as e:
        return False, None, [str(e)]
    finally:
        conn.close()

def test_connection():
    try:
        conn = get_connection()
        conn.close()
        return True, "Connected"
    except Exception as e:
        return False, str(e)
