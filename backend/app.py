from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)
 

DB_NAME = "feedback.db"
@app.route("/submit-feedback", methods=["POST"])
def submit_feedback():
    data = request.get_json()
    print(" FRONTEND SENT:", data)  

    if not data:
        return jsonify({"error": "No data received"}), 400

    text = data.get("text")
    category = data.get("category")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (text, category, timestamp) VALUES (?, ?, ?)",
                   (text, category, timestamp))
    conn.commit()
    conn.close()

    print("📦 SAVED:", text, category, timestamp)

    return jsonify({"message": "Feedback submitted successfully!"}), 200


     

@app.route("/get-feedback", methods=["GET"])
def get_feedback():
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("SELECT id, text, category, timestamp FROM feedback ORDER BY id DESC")
        rows = c.fetchall()
        conn.close()

        feedback_list = [{
            "id": row[0],
            "text": row[1],
            "category": row[2],
            "timestamp": row[3]
        } for row in rows]


        return jsonify({"feedback": feedback_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
