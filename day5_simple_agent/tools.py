def calculator(expression: str):
    """
    Simple calculator tool that evaluates a math expression
    """
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"