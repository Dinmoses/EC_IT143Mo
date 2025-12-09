from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect('people.db')

@app.route('/')
def index():
    return "Welcome to the Users Database API! Use /revise?username=<name>[&auth=<level>]"

@app.route('/revise')
def revise():
    username = request.args.get('username')
    new_auth = request.args.get('auth')

    if not username:
        return jsonify({"error": "Missing 'username' parameter"}), 400

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, username, year, auth FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    if not user:
        conn.close()
        return jsonify({"error": "User not found", "username": username}), 404

    # Update authorization if 'auth' provided
    if new_auth is not None:
        try:
            auth_val = int(new_auth)
        except ValueError:
            conn.close()
            return jsonify({"error": "Invalid 'auth' value (must be an integer)"}), 400

        cursor.execute("UPDATE users SET auth=? WHERE username=?", (auth_val, username))
        conn.commit()

        cursor.execute("SELECT id, username, year, auth FROM users WHERE username=?", (username,))
        updated = cursor.fetchone()
        conn.close()
        return jsonify({
            "message": "Authorization updated",
            "user": {
                "id": updated[0],
                "username": updated[1],
                "year": updated[2],
                "auth": updated[3]
            }
        }), 200

    # If not updating, just return the user record
    conn.close()
    return jsonify({
        "user": {
            "id": user[0],
            "username": user[1],
            "year": user[2],
            "auth": user[3]
        }
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
