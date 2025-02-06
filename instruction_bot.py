def get_instruction_response(user_input):
    """
    Generates responses for user queries about how to use the chatbot calculator.
    """
    user_input = user_input.lower()

    if "add" in user_input:
        return "To add numbers, type: 'add 5 10' or '5 + 10'."
    elif "subtract" in user_input:
        return "To subtract numbers, type: 'subtract 10 5' or '10 - 5'."
    elif "multiply" in user_input:
        return "To multiply numbers, type: 'multiply 3 7' or '3 * 7'."
    elif "divide" in user_input:
        return "To divide numbers, type: 'divide 20 4' or '20 / 4'."
    elif "power" in user_input:
        return "To calculate powers, type: 'power 2 3' or '2 ^ 3' (2 to the power of 3)."
    elif "sin" in user_input:
        return "To calculate sine of an angle, type: 'sin 45'."
    elif "cos" in user_input:
        return "To calculate cosine of an angle, type: 'cos 60'."
    elif "tan" in user_input:
        return "To calculate tangent of an angle, type: 'tan 30'."
    elif "hi" in user_input or "hello" in user_input or "hlo" in user_input or "hey" in user_input:
        return ("hi.. you are welcome to AI Chatbot Calculator. Now tell me what help you want.")
    elif "help" in user_input or "how" in user_input:
        return (
            "Supported operations: add (+), subtract (-), multiply (*), divide (/), "
            "power (^), sin, cos, tan. Type your query like 'add 5 10' or 'sin 45'."
        )
    
    elif "contact us" in user_input or "contact" in user_input or "" in user_input or "email" in user_input:
        return ("hi..do you want to contact us? if you want to contact us please send your enquiry on +91 8287920575.")
    elif "about" in user_input or "about us" in user_input or "chatbot" in user_input or "ai chatbot" in user_input:
        return ("hi.. you are welcome to AI Chatbot Calculator. we are ai baseed advance chat bot calculator to solve ypur problem.")
    else:
        return "Sorry, I didn't understand your query. Try asking about add, subtract, multiply, divide, or trigonometric operations."
