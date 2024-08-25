from flask import Flask, request, jsonify

app = Flask(__name__)

# POST method
@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    user_id = "Rishav_Srivastav_11102001"  
    email = "rishav.srivastav2021@vitstudent.ac.in"  
    roll_number = "21BKT0088"  

    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]

    # Get the highest lowercase alphabet
    lowercase_alphabets = [x for x in alphabets if x.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }
    return jsonify(response)

# GET method
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
