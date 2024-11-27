import random
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/assign-numbers', methods=['POST'])
def assign_numbers():
    # Parse input data
    data = request.get_json()
    names = data.get('names', [])
    iterations = data.get('iterations', 1)  # Default to 1 iteration if not provided

    if not names:
        return jsonify({"error": "No names provided"}), 400
    if iterations < 1:
        return jsonify({"error": "Iterations must be at least 1"}), 400

    # Initialize variables
    assignments = []

    # Perform multiple iterations
    for _ in range(iterations):
        numbers = list(range(1, len(names) + 1))
        random.shuffle(numbers)
        assignments = [{"name": name, "number": number} for name, number in zip(names, numbers)]

    # Save final results to a file
    with open("final_results.txt", "w") as file:
        for assignment in assignments:
            file.write(f"{assignment['name']} -> {assignment['number']}\n")

    # Return the final assignment
    return jsonify({"final_assignments": assignments})

@app.route('/download-results', methods=['GET'])
def download_results():
    return send_file("results.txt", as_attachment=True)  # Sends the text file for download
if __name__ == '__main__':
    app.run(debug=True)
