def create_list(user_numbers):
    add_numbers = True
    while add_numbers:
        user_numbers.append(int(input("\nPlease enter a number:\n")))
        keep_asking = int(input(""" 
Pick an option:
(1) Add another number
(2) Don't add anymore                                
"""))
        if keep_asking == 1:
            continue
        else:
            add_numbers = False
    return user_numbers


def min_and_max(user_numbers, output_list):
    user_numbers.sort()
    output_list.append(user_numbers[0])
    output_list.append(user_numbers[-1])
    return output_list


print("""
Greetings!
I will take a list of numbers that you provide as an input.
I will then output the smallest and largest numbers from your input as an array.
Let's begin!      
""")


active = True
user_numbers = []
output_list = []

while active:
    user_numbers = create_list(user_numbers)
    output_list = min_and_max(user_numbers, output_list)
    print("\nThe smallest and largest numbers are: " + str(output_list))
    user_cont = int(input("""
Would you like to try again with a new batch of numbers?
(1) Yes
(2) No
Enter the number of the option you desire:              
"""))
    if user_cont == 1:
        user_numbers = []
        output_list = []
    else:
        print("\nGoodbye!")
        active = False
