"""
Temperature Conversion Script
Tuesday, 29th August 2023.

This script allows the user to convert temperatures between Celsius and Fahrenheit units. The user provides a temperature value and specifies the input unit (C or F). The script then calculates the conversion and displays the result along with the original and target units.

Usage:
- Run the script.
- Enter the temperature value and unit (C or F) when prompted.
- The script will calculate and display the converted temperature.
- You can choose to continue converting temperatures or exit the script.

Formulas:
- Celsius to Fahrenheit: F = (C * 9/5) + 32
- Fahrenheit to Celsius: C = (F - 32) * 5/9
"""




while True:
    try:
        #taking input
        user_input = float(input("Enter Temperature: "))
        unit = input("Enter Unit (C/F): ").upper()

        #input validation and conversion
        if unit == 'C':
            unit = 'Celsius'
            converted = (user_input * 9/5) + 32
            new_unit = 'Farenheit'
        elif unit == 'F':
            unit = 'Farenheit'
            converted = (user_input - 32) * 5/9
            new_unit = 'Celsius'
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
            continue  #restart the loop

        #printing the result
        print(f"{user_input} Degree {unit} is equal to {converted:.2f} Degree {new_unit}")
        
        #asking if the user wants to continue 
        again = input("Do you want to convert another temperature? (Yes/No): ").capitalize()
        if again != 'Yes':
            break  #exit the loop
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Exiting the temperature converter.")
