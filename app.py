from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Arun", "course": "Python"},
    {"id": 2, "name": "Kumar", "course": "Java"}
]

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)

    if student:
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "course": data["course"]
    }

    students.append(new_student)
    return jsonify(new_student), 201

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()
    student["name"] = data.get("name", student["name"])
    student["course"] = data.get("course", student["course"])

    return jsonify(student)

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    global students

    student = next((s for s in students if s["id"] == student_id), None)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    students.remove(student)
    return jsonify({"message": "Student deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)