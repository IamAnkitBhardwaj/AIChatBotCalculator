from flask import Flask, request, jsonify
from flask_cors import CORS
from instruction_bot import get_instruction_response  # Import the instruction chatbot logic

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    user_input = data.get('input', '').strip().lower()

    try:
        if "add" in user_input or "+" in user_input:
            numbers = [float(n) for n in user_input.replace("+", " ").split() if n.replace('.', '', 1).isdigit()]
            result = sum(numbers)
        elif "subtract" in user_input or "-" in user_input:
            numbers = [float(n) for n in user_input.replace("-", " ").split() if n.replace('.', '', 1).isdigit()]
            result = numbers[0] - sum(numbers[1:])
        elif "multiply" in user_input or "*" in user_input:
            numbers = [float(n) for n in user_input.replace("*", " ").split() if n.replace('.', '', 1).isdigit()]
            result = 1
            for num in numbers:
                result *= num
        elif "divide" in user_input or "/" in user_input:
            numbers = [float(n) for n in user_input.replace("/", " ").split() if n.replace('.', '', 1).isdigit()]
            if len(numbers) == 2:
                result = numbers[0] / numbers[1]
            else:
                return jsonify({'error': 'Please provide two numbers for division.'})
        elif "power" in user_input or "^" in user_input:
            base, exp = map(float, user_input.replace("^", " ").split())
            result = pow(base, exp)
        elif "sin" in user_input:
            import math
            angle = float(user_input.replace("sin", "").strip())
            result = math.sin(math.radians(angle))
        elif "cos" in user_input:
            import math
            angle = float(user_input.replace("cos", "").strip())
            result = math.cos(math.radians(angle))
        elif "tan" in user_input:
            import math
            angle = float(user_input.replace("tan", "").strip())
            result = math.tan(math.radians(angle))
        else:
            result = "Unsupported operation. Try 'add', 'subtract', 'multiply', 'divide', 'power', 'sin', 'cos', or 'tan'."

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/instructions', methods=['POST'])
def instructions():
    data = request.json
    user_input = data.get('input', '').strip()
    response = get_instruction_response(user_input)  # Call function from instruction_bot
    return jsonify({'result': response})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
