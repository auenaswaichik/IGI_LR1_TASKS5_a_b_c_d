# Import required modules
import CustomInput as custom_input  # Custom module for handling user input validation
import math  # Math module for mathematical operations

def get_numbers():
    """
    Collects a list of numbers from user input until 0 is entered.
    
    Returns:
        list: A list of entered numbers (excluding the terminating 0)
    """
    print("Enter list of numbers")  # Prompt user for input
    x = 0  # Variable to store current input
    list_of_numbers = []  # List to store all entered numbers
    
    while True:
        x = custom_input.input_float()  # Get float input from user
        
        if x == 0:  # Check for termination condition (0)
            break
            
        list_of_numbers.append(x)  # Add number to list if not zero
    
    return list_of_numbers

def get_fabs_numbers(list_of_numbers):
    """
    Generator function that yields numbers from the input list.
    
    Args:
        list_of_numbers (list): List of numbers to process
        
    Yields:
        float: Each number from the input list
    """
    for x in list_of_numbers:
        yield x  # Yield each number in the list

def get_sum_between(l, r, list_of_numbers):
    """
    Calculates the sum of positive numbers between indices l and r (inclusive).
    
    Args:
        l (int): Left boundary index
        r (int): Right boundary index
        list_of_numbers (list): List of numbers to process
        
    Returns:
        float: Sum of positive numbers in the specified range
    """
    result = 0  # Initialize sum counter
    
    # Iterate through the specified range of indices
    for i in range(l, r + 1):
        if list_of_numbers[i] > 0:  # Check if number is positive
            result += list_of_numbers[i]  # Add positive numbers to sum
    
    return result

def get_multiplication_between(l, r, list_of_numbers):
    """
    Calculates the product of all numbers between indices l and r (inclusive).
    
    Args:
        l (int): Left boundary index
        r (int): Right boundary index
        list_of_numbers (list): List of numbers to process
        
    Returns:
        float: Product of all numbers in the specified range
    """
    result = 1  # Initialize product (start with 1 for multiplication)
    
    # Iterate through the specified range of indices
    for i in range(l, r + 1):
        result *= list_of_numbers[i]  # Multiply all numbers in range
    
    return result

def start():
    """
    Main function that executes the program workflow:
    1. Gets numbers from user
    2. Finds absolute values
    3. Determines min/max positions
    4. Calculates sum and product between min/max
    5. Prints results
    """
    # Step 1: Get list of numbers from user
    list_of_numbers = get_numbers()
    
    # Step 2: Create list of absolute values using generator
    list_of_fabs_numbers = [val for val in get_fabs_numbers(list_of_numbers)]
    
    # Step 3: Find indices of max and min absolute values
    max_index = list_of_fabs_numbers.index(max(list_of_fabs_numbers))
    min_index = list_of_fabs_numbers.index(min(list_of_fabs_numbers))
    
    # Determine left and right boundaries (order matters for range)
    l_index = min(max_index, min_index)
    r_index = max(max_index, min_index)
    
    # Step 4: Calculate and print results
    print("Sum of positive elements between min and max values is:", 
          get_sum_between(l_index, r_index, list_of_numbers))
    print("Multiplication of elements between min and max values is:", 
          get_multiplication_between(l_index, r_index, list_of_numbers))