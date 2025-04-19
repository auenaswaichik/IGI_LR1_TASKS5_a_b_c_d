# Define a sample string for text processing tasks
task_string = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."

def remove_punctuation_marks(task_string):
    """
    Removes common punctuation marks from a string.
    
    Args:
        task_string (str): Input string containing punctuation marks
        
    Returns:
        str: String with punctuation marks removed
    """
    result = ''  # Initialize an empty string to store the result
    
    # Iterate through each character in the input string
    for x in task_string:
        # Check if the character is a punctuation mark
        if x == ',' or x == '.' or x == '!' or x == '?' or x == ':' or x == ';':
            continue  # Skip punctuation marks
        
        # Add non-punctuation characters to the result
        result = result + x
    
    return result

def get_vowels_words(list_of_words):
    """
    Counts how many words in a list end with a vowel (a, e, i, o, u, y).
    
    Args:
        list_of_words (list): List of words to analyze
        
    Returns:
        int: Number of words ending with a vowel
    """
    result = 0  # Initialize vowel-ending word counter
    symbol = ''  # Variable to store the last character of each word
    
    # Check each word in the list
    for x in list_of_words:
        symbol = x[-1]  # Get the last character of the word
        
        # Check if the last character is a vowel
        if symbol == 'e' or symbol == 'y' or symbol == 'u' or symbol == 'i' or symbol == 'o' or symbol == 'a':
            result += 1  # Increment counter if vowel found
    
    return result
        
def get_avg_len_and_words(list_of_words):
    """
    Calculates the average word length and finds all words with that length.
    
    Args:
        list_of_words (list): List of words to analyze
        
    Returns:
        tuple: (average_word_length, list_of_words_with_that_length)
    """
    ammount_of_words = len(list_of_words)  # Count total words
    sum_of_words_len = 0  # Initialize total length counter
    
    # Calculate total length of all words
    for x in list_of_words:
        sum_of_words_len += len(x)
    
    # Calculate average word length (using integer division)
    avg_word_len = int(round(sum_of_words_len / ammount_of_words))
    
    result = []  # Initialize list for words with average length
    
    # Find all words with length equal to the average
    for x in list_of_words:
        if len(x) == avg_word_len:
            result.append(x)
    
    return avg_word_len, result

def get_every_seventh_word(list_of_words):
    """
    Extracts every seventh word from the list (starting from index 6).
    
    Args:
        list_of_words (list): List of words to process
        
    Returns:
        list: Every seventh word in the original list
    """
    # Slice the list to get every 7th element starting from index 6
    return list_of_words[6:len(list_of_words):7]

def start():
    """
    Main function that executes all text processing tasks:
    1. Removes punctuation from the sample string
    2. Splits into individual words
    3. Counts words ending with vowels
    4. Calculates average word length
    5. Extracts every seventh word
    """
    # Step 1: Remove punctuation marks from the sample string
    string_without_shtuki = remove_punctuation_marks(task_string)
    
    # Step 2: Split the cleaned string into a list of words
    list_of_words = string_without_shtuki.rsplit(" ")
    
    # Step 3: Count and print words ending with vowels
    print("Words that ends at vowel letter is:", get_vowels_words(list_of_words))
    
    # Step 4: Calculate and print average word length and matching words
    avg, list_words = get_avg_len_and_words(list_of_words)
    print("Avarage word length and words with this length is:", avg, '\n', list_words)
    
    # Step 5: Extract and print every seventh word
    print("Every seventh word is:", get_every_seventh_word(list_of_words))