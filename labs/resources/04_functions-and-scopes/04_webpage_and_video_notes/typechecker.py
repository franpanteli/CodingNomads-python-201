def greet(greeting: str, name: str) -> str:
    """Generates a greeting."""
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

greet("Hello","John","Doe")
# greet("Hello","John","Doe","4")

# (base) francescapanteli@Mac 04_webpage_and_video_notes % mypy typechecker.py
# typechecker.py:6: error: Too many arguments for "greet"  [call-arg]
# typechecker.py:7: error: Too many arguments for "greet"  [call-arg]
# Found 2 errors in 1 file (checked 1 source file)
# (base) francescapanteli@Mac 04_webpage_and_video_notes %

#running mypy typechecker.py checks that the data types of the arguments being entered into the function when it is called are desired