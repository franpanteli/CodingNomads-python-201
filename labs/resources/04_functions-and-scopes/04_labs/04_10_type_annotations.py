# Add type annotations to the three functions shown below.
"""Syntax:
    def greet(greeting: str, name: str) -> str:
        """Generates a greeting."""
        sentence = f"{greeting}, {name}! How are you?"
        return sentence
"""

def multiply(num1: float, num2: float) -> float:
    return num1 * num2

def greet(greeting: str, name: str) -> str:
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def shopping_list(*args: str) -> tuple:
    [print(f"* {item}") for item in args]
    return args
