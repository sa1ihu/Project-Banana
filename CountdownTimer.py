"""
SimpleSecondsTimer
Wed, August 30, 2023.

This script is a lightweight command-line tool designed to provide a minimalistic solution for setting and tracking countdown timers in seconds.
Users input the desired countdown duration in seconds, and the script offersa real-time countdown display that updates every second until the countdown reaches zero.
This straightforward script is particularly suited for scenarios where a quick and precise countdown is needed, such as timing short cooking intervals, monitoring presentation durations, or implementing simple interval exercise during workouts.
"""





import time

def countdown_timer(total_seconds):
    while total_seconds >= 0:
        # display remaining seconds with 1 decimal place
        print(f"{total_seconds:.2f}s left", end='\r')  # '\r' moves cursor to start of line, updating the result on the same line
        total_seconds -= 0.1  # Decrement by 0.1 seconds for better simulation lol
        time.sleep(0.1)  # Wait for 0.1 seconds
        print(" " * 15, end='\r')


#getting user input/error handling
while True:
    try:
        user_input = float(input("Enter seconds: "))
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a valid number.")



#calling the function
countdown_timer(user_input
