from getconn import get_connection

def check_login(role, password):
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = "SELECT * FROM users WHERE role=%s AND password=%s"
        cur.execute(query, (role, password))

        user = cur.fetchone()

        cur.close()
        conn.close()

        if user:
            return True
        else:
            return False

    except Exception as e:
        print("❌ Error in login:", e)
        return False
