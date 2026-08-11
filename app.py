from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data matching course schedule
work_plan = [
    {
        "id": 1,
        "week": "W1–W2",
        "topic": "APIs & Backend Basics (Node.js / Flask)",
        "project": "Build a REST API",
        "activity": "Whiteboard Challenge",
        "duration": "3 hrs"
    }
]

# GET Request
@app.route('/api/plan', methods=['GET'])
def get_plan():
    return jsonify({
        "status": "success",
        "total_records": len(work_plan),
        "data": work_plan
    }), 200

# POST Request
@app.route('/api/plan', methods=['POST'])
def add_plan():
    new_data = request.json
    if not new_data or 'week' not in new_data:
        return jsonify({"error": "Please provide required fields!"}), 400
        
    new_data['id'] = len(work_plan) + 1
    work_plan.append(new_data)
    
    return jsonify({
        "message": "New plan added successfully!",
        "added_item": new_data
    }), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
