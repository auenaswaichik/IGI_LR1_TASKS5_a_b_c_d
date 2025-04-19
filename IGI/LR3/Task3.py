def get_result(input_str):
    """
    Counts the number of punctuation marks in a given string.
    
    Args:
        input_str (str): The input string to analyze for punctuation marks
        
    Returns:
        int: The count of punctuation marks found in the string
    """
    result = 0  # Initialize counter for punctuation marks

    for x in input_str:  # Iterate through each character in the string
        # Check if the character is one of the specified punctuation marks
        if x in {',', '.', '!', '?', ':', ';'}:
            result += 1  # Increment counter if punctuation mark is found

    return result

def start():
    """
    Main function that handles user interaction:
    1. Prompts user for input string
    2. Counts punctuation marks
    3. Displays the result
    """
    # Get input string from user
    input_str = input("Enter your string: ")
    
    # Count punctuation marks in the input string
    ammount = get_result(input_str)
    
    # Display the result (fixed typo 'ammount' to 'amount')
    print(f"Amount of punctuation marks is {ammount}")