from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes (Restrict in production)

# Your API key
API_KEY = "2659b401f8f78fa93f836342"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest"

@app.route('/convert_currency', methods=['POST'])
def convert_currency():
    try:
        # Parse user input
        data = request.json
        from_currency = data.get('from_currency', '').upper().strip()
        to_currency = data.get('to_currency', '').upper().strip()
        amount = data.get('amount', '')

        # Validate inputs
        if not from_currency or not to_currency:
            return jsonify({'error': 'Please provide valid "from_currency" and "to_currency".'}), 400
        if not amount or not isinstance(amount, (int, float)) or float(amount) <= 0:
            return jsonify({'error': 'Amount must be a positive number.'}), 400

        amount = float(amount)  # Ensure it's converted to float

        # Fetch exchange rates
        response = requests.get(f"{BASE_URL}/{from_currency}")
        if response.status_code != 200:
            return jsonify({'error': 'Failed to fetch exchange rates. Check your API key or internet connection.'}), 500

        exchange_data = response.json()

        # Check if conversion rates are available
        if "conversion_rates" not in exchange_data:
            return jsonify({'error': 'Conversion rates not available for the provided currency.'}), 500

        conversion_rates = exchange_data["conversion_rates"]
        if to_currency not in conversion_rates:
            return jsonify({'error': f'Currency "{to_currency}" is not supported.'}), 400

        # Perform the conversion
        converted_amount = amount * conversion_rates[to_currency]

        # Return the result
        return jsonify({
            'from_currency': from_currency,
            'to_currency': to_currency,
            'amount': amount,
            'converted_amount': converted_amount,
            'rate': conversion_rates[to_currency]
        })

    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(port=5001, debug=True)
