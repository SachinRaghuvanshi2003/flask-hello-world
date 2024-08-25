from flask import Flask, request, jsonify

app = Flask(__name__)

USER_ID = "ayush_gautam_14122003"
EMAIL = "ayushrajput1144@gmail.com"
ROLL_NUMBER = "21BIT0230"

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get('data', [])

    numbers = []
    alphabets = []
    highest_lowercase_alphabet = []

    highest_char = None

    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower():
                if highest_char is None or item > highest_char:
                    highest_char = item

    if highest_char:
        highest_lowercase_alphabet.append(highest_char)

    response = {
        "is_success": True,
        "user_id": USER_ID,
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }

    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
