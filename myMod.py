#already written on my vs code but my system hangs

def reverse_text(text):
    """Reverse the input text."""
    return text[::-1]

def simple_calculator(a, b, operation):
    """Simple calculator with basic operations."""
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

# Example usage
if name == "__main__":
    print(reverse_text("Hello World"))
    print(simple_calculator(10, 5, 'add'))
