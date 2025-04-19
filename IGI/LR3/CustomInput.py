def input_float():
    """
    Prompts the user for input and attempts to convert it to a float.
    If conversion fails, displays an error message and recursively prompts again.
    
    Returns:
        float: The valid float number entered by the user
    """
    try:
        # Attempt to read user input and convert to float
        float_input = float(input())
        return float_input
    except ValueError:
        # Handle case where conversion to float fails
        print("Your input was incorrect, please try again.")
        # Recursively call the function to get valid input
        return input_float()


def input_int():
    """
    Prompts the user for input and attempts to convert it to an integer.
    If conversion fails, displays an error message and recursively prompts again.
    
    Returns:
        int: The valid integer entered by the user
    """
    try:
        # Attempt to read user input and convert to integer
        int_input = int(input())
        return int_input
    except ValueError:
        # Handle case where conversion to integer fails
        print("Your input was incorrect, please try again.")
        # Recursively call the function to get valid input
        return input_int()