import ast
import operator

# Map allowed operators safely to avoid unsafe eval() vulnerabilities
ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg  # Supports negative numbers like -5
}

def safe_eval_ast(node):
    """Recursively parses an Abstract Syntax Tree node to evaluate math safely."""
    if isinstance(node, ast.Constant):  # Primitive number
        return node.value
    elif isinstance(node, ast.BinOp):  # Binary operation (e.g., A + B)
        left = safe_eval_ast(node.left)
        right = safe_eval_ast(node.right)
        if type(node.op) in ALLOWED_OPERATORS:
            if isinstance(node.op, ast.Div) and right == 0:
                raise ZeroDivisionError("Math Error: Division by zero is undefined.")
            return ALLOWED_OPERATORS[type(node.op)](left, right)
    elif isinstance(node, ast.UnaryOp):  # Unary operation (e.g., -5)
        operand = safe_eval_ast(node.operand)
        if type(node.op) in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[type(node.op)](operand)
    
    raise ValueError("Invalid Expression Elements Detected.")

def evaluate_expression(expression):
    """Sanitizes, parses, and executes mathematical string expressions safely."""
    # Sanitize whitespace and validate characters
    cleaned_expr = expression.replace(" ", "")
    if not cleaned_expr:
        return "Error: Empty Expression"

    allowed_chars = set("0123456789+-*/().")
    if not set(cleaned_expr).issubset(allowed_chars):
        return "Security Error: Prohibited characters detected."

    try:
        # Parse the string into a safe mathematical node structure
        tree = ast.parse(cleaned_expr, mode='eval')
        result = safe_eval_ast(tree.body)
        
        # Format floating points cleanly
        if isinstance(result, float) and result.is_integer():
            return int(result)
        return round(result, 4)

    except ZeroDivisionError as zde:
        return str(zde)
    except (SyntaxError, ValueError, KeyError):
        return "Syntax Error: Malformed mathematical statement."
    except Exception:
        return "Runtime Error: Unable to process mathematical syntax."

def main():
    """Main loop tailored for fluid Pydroid terminal usage."""
    print("=" * 45)
    print("     CORE MATHEMATICAL EVALUATION ENGINE     ")
    print("=" * 45)
    print("Supports: +, -, *, /, brackets (), decimals")
    print("Type 'exit' or 'quit' to terminate system.")
    print("-" * 45)

    history = []

    while True:
        user_input = input("\nCalc > ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            print("\nShutting down Evaluation Engine. Systems offline.")
            break
            
        if user_input.lower() == 'history':
            print("\n--- Session Calculation History ---")
            for item in history[-5:]: # Display last 5 computations
                print(item)
            continue

        if not user_input:
            continue

        output = evaluate_expression(user_input)
        print(f"Result: {output}")
        
        # Store clean executions in local history state
        if "Error" not in str(output):
            history.append(f"{user_input} = {output}")

if __name__ == "__main__":
    main()
