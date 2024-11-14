# Starting the program
run = input("Welcome, do you wanna start the app? yes/no: ").lower()
while run != 'yes':
    if run == 'no':
        quit()
    else:
        print("Please answer with 'yes' or 'no'.")
    run = input("Welcome, do you wanna start the app? yes/no: ").lower()

print()
print("Program is starting...")
print()

# Function to check if the number is odd and prime
def main():
    while True:
        num_str = input("Enter an integer: ")
        
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
main()
# Call the function to execute
keep_going = input("Do you want to check another number? yes/no: ").lower()
while keep_going != 'yes':
    if keep_going == 'no':
        print()
        print(f"Thank you and goodbye.")
        quit()
    else:
        print("Please answer with 'yes' or 'no'.")
        keep_going = input("Do you want to check another number? yes/no: ").lower()

def ice_floe():
    while True:
        reading_1 = input("Enter the first reading: ")
        if reading_1.isdigit():
            num = int(reading_1)
            break
        else:
            print("Invalid input. Please enter an integer.")
    print(f"First Reading: {reading_1}")
ice_floe()
