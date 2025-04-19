# Import required libraries
import pandas  # For data manipulation and DataFrame operations
import CustomInput as custom_input  # Custom module for handling user input
import math  # For mathematical operations and constants

def calculate_sin(x, eps):
    """
    Calculate the Taylor series approximation of sin(x) up to a specified precision (eps).
    
    Args:
        x (float): The input value for which to calculate sin(x)
        eps (float): The precision/error tolerance for the approximation
    
    Returns:
        pandas.DataFrame: A table containing iteration details including:
                         - Current term value
                         - Iteration count
                         - Current approximation
                         - Math library's sin(x) value
                         - Precision target
    """
    
    # Initialize DataFrame to store calculation results with columns:
    # X: Current x^n term value
    # N: Iteration count
    # F(x): Current term contribution
    # Math F(x): Cumulative approximation
    # Eps: Precision target
    table = pandas.DataFrame([[0.0, 0, 0.0, 0.0, 0.0]], 
                            columns=['X', 'N', 'F(x)', 'Math F(x)', 'Eps'])
    
    # Initialize variables for Taylor series calculation
    sing = 1  # Sign alternator (+1/-1)
    fact = 1  # Factorial accumulator (1, 6, 120... for 1!, 3!, 5!...)
    fact_counter = 2  # Counter for factorial calculation
    pow_x = x  # x^n term accumulator (x, x^3, x^5...)
    f_x = 0.0  # Current term value
    math_f_x = 0.0  # Cumulative sum of terms (approximation)
    iteration = 0  # Iteration counter

    while True:
        # Calculate current term: (-1)^n * x^(2n+1)/(2n+1)!
        f_x = sing * (pow_x / fact)
        math_f_x += f_x  # Add current term to approximation
        iteration += 1  # Increment iteration count
        
        # Append current iteration results to DataFrame
        table = pandas.concat([table, 
                             pandas.DataFrame([[pow_x, iteration, f_x, math_f_x, eps]], 
                             columns=table.columns)], 
                             ignore_index=True)
        
        # Termination conditions:
        # 1. Maximum iterations (500) reached to prevent infinite loops
        # 2. Current term smaller than precision target (eps)
        if (iteration > 500) or math.fabs(f_x) < eps:
            break

        # Update variables for next term calculation:
        # Factorial part: Multiply two numbers to jump to next odd factorial
        fact *= fact_counter
        fact_counter += 1
        fact *= fact_counter
        fact_counter += 1
        
        # Power part: Multiply x^2 to get next odd power
        pow_x *= x
        pow_x *= x
        
        # Alternate the sign for next term
        sing *= (-1)

    return table


def start():
    """
    Main function to execute the sin(x) approximation.
    Handles user input and displays results.
    """
    
    # Get user input for x value
    print("Enter X: ")
    x = custom_input.input_float()
    
    # Get user input for precision (epsilon)
    print("Enter exp:")
    eps = custom_input.input_float()

    # Calculate sin(x) approximation using Taylor series
    table = calculate_sin(x, eps)

    # Display results table
    print(table)