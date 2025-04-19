# Import custom input module for handling user input validation
import CustomInput as custom_input

def decorator_it(func):
    """
    Decorator function that adds input prompts around the decorated function.
    
    Args:
        func (function): The function to be decorated
        
    Returns:
        function: The wrapped function with added prompts
    """
    def new_funct():
        # Print message before executing the decorated function
        print("Enter list of numbers")
        
        # Call the original function
        result = func()
        
        # Print message after execution
        print("Numbers were entered")
        return result
    
    return new_funct
        
@decorator_it
def get_numbers():
    """
    Collects a list of integers from user input until 0 is entered.
    Uses the decorator to display input prompts.
    
    Returns:
        list: A list of entered integers (excluding the terminating 0)
    """
    x = 0  # Variable to store current input
    list_of_numbers = []  # List to accumulate numbers
    
    while True:
        # Get integer input from user
        x = custom_input.input_int()
        
        # Check for termination condition (0)
        if x == 0:
            break
            
        # Add number to list
        list_of_numbers.append(x)

    return list_of_numbers

def get_result_numbers_list(numbers: list):
    """
    Counts the number of even numbers in a list.
    
    Args:
        numbers (list): List of integers to analyze
        
    Returns:
        int: Count of even numbers in the input list
    """
    result = 0  # Counter for even numbers

    for x in numbers:
        # Check if number is even (divisible by 2)
        if x % 2 == 0:  # Removed redundant int(2) since 2 is already an integer
            result += 1  # Increment counter

    return result

def start():
    """
    Main function that orchestrates the program flow:
    1. Gets numbers from user
    2. Counts even numbers
    3. Prints the result
    """
    # Get list of numbers from user (decorated with input prompts)
    numbers = get_numbers()
    
    # Count even numbers in the list
    ammount = get_result_numbers_list(numbers)
    
    # Print the result (fixed typo in output message)
    print("Amount of even numbers is", ammount)