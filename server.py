from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows requests from frontend

# Available parking slots
parking_slots = [f"SLOT-{i}" for i in range(1, 21)]  # 20 slots
assigned_slots = set()

@app.route("/assign_slot", methods=["POST"])
def assign_slot():
    data = request.json
    if not data or "name" not in data or "phone" not in data or "vehicle" not in data:
        return jsonify({"error": "Invalid data"}), 400

    available_slots = [slot for slot in parking_slots if slot not in assigned_slots]
    
    if not available_slots:
        return jsonify({"error": "No slots available"}), 400

    assigned_slot = available_slots[0]  # Assign the first available slot
    assigned_slots.add(assigned_slot)

    return jsonify({"slot": assigned_slot})

if __name__ == "__main__":
    app.run(debug=True)
