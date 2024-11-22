# Function to check if the number is odd and prime
def prime():  # Prime algorithm implemented by me
    while True:
        num_str = input("Enter an integer: ")
        print()
        # Check if input is a valid integer
        if num_str.isdigit():
            num = int(num_str)
            
            # Check if the number is odd
            is_odd = (num % 2 != 0)
            
            # Check if the number is prime
            is_prime = num > 1
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            
            # Print results
            if is_odd and is_prime:
                print(f"{num} is an odd and prime number.")
            elif is_odd:
                print(f"{num} is odd but not prime.")
            elif is_prime:
                print(f"{num} is prime but not odd.")
            else:
                print(f"{num} is neither odd nor prime.")
            break  # Exit the loop after one valid input
        else:
            print("Invalid input. Please enter an integer.")

# Ice Floe Volume Calculation
def ice_floe():
    # Collecting three readings for the freeboard (height of ice above the waterline)
    readings = []
    for i in range(3):
        while True:
            reading = input(f"Enter freeboard height reading {i + 1}: ")
            if reading.isdigit():
                readings.append(int(reading))
                break
            else:
                print("Invalid input. Please enter an integer.")
    
    # Calculate the average freeboard
    average_freeboard = sum(readings) / len(readings)
    print(f"Average freeboard: {average_freeboard:.1f}")
    
    # Get the length and breadth
    while True:
        reading_1 = input("Enter the Length: ")
        if reading_1.isdigit():
            num1 = int(reading_1)
            break
        else:
            print("Invalid input. Please enter an integer.")
    
    while True:
        reading_2 = input("Enter the Breadth: ")
        if reading_2.isdigit():
            num2 = int(reading_2)
            break
        else:
            print("Invalid input. Please enter an integer.")
    
    return num1, num2, average_freeboard  # Return average freeboard

# Calculate the volume using the thickness and area
def floe_volume(num1, num2, average_freeboard):
    # Calculate thickness (9 times the average freeboard)
    thickness = average_freeboard * 9
    
    # Calculate volume (Area * Thickness)
    volume = num1 * num2 * thickness
    return volume

# Output the volume
def volume_op():
    # Get the values from the ice_floe function
    num1, num2, average_freeboard = ice_floe()  # Get average freeboard
    volume = floe_volume(num1, num2, average_freeboard)  # Pass the average freeboard
    print(f"The Ice Floe volume is: {volume:.1f} cubic metres")
    print()

def main():
    first_run = True  # Flag to check if it's the first run

    while True:  # Main loop to keep asking if the user wants to restart
        if first_run:
            print("- Odd And Prime numbers checker and Ice Floe Volume Calculator Program -")
            print()
            run = input("Welcome, do you wanna start the app? yes/no: ").lower()
            while run != 'yes':
                if run == 'no':
                    print("Goodbye! Exiting the program.")
                    quit()
                else:
                    print("Please answer with 'yes' or 'no'.")
                run = input("Welcome, do you wanna start the app? yes/no: ").lower()

            first_run = False  # Set flag to False after the first run

        # Start the program tasks
        print("Odds and Prime Program is starting...")
        print()
        prime()  # Prime number check
        print()
        print("Ice Floe Calculator starting...")
        print()
        volume_op()  # Calculate and output volume

        # Ask if the user wants to run the program again
        while True:  # Loop to keep asking for a valid input
            run_again = input("Do you want to run the program again? yes/no: ").lower()
            if run_again == 'no':
                print("Goodbye! Exiting the program.")
                exit() # Ends the running
            elif run_again == 'yes':
                break  # Exit the loop and continue the program
            else:
                print("Invalid input. Please answer with 'yes' or 'no'.")

# Make sure main() runs first when this script is executed
if __name__ == "__main__":
    main()
