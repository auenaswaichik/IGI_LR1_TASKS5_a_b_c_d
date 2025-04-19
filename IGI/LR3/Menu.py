# Importing all the task modules and custom input module
import Task1 as task_1
import Task2 as task_2
import Task3 as task_3
import Task4 as task_4
import Task5 as task_5
import CustomInput as custom_input

def start_menu():
    """
    Displays a menu to select and run different tasks.
    The menu runs in a loop until the user chooses to exit (option 0).
    """
    while True:
        # Display menu prompt
        print("Enter number of task, that gonna be run(or 0 to stop programm):\n1)Get cos of x with iterations\n2)Count ammount of odd numbers in array\n3)Count punctuation marks in sentance\n4)Get words, that ends at vowel letter. Get avarage words length and words with this length. Get every seventh words.\n5)Get sum of positive numbers and multiplication of numbers between numbers in array by module.")
        
        # Get user input for task selection
        task_num = custom_input.input_int()

        # Check user input and execute corresponding task
        if task_num == 0:
            # Exit the program
            break
        elif task_num == 1:
            # Run Task 1
            task_1.start()
        elif task_num == 2:
            # Run Task 2
            task_2.start()
        elif task_num == 3:
            # Run Task 3
            task_3.start()
        elif task_num == 4:
            # Run Task 4
            task_4.start()
        elif task_num == 5:
            # Run Task 5
            task_5.start()
        else:
            # Handle invalid input
            print("Your input were incorrect.")