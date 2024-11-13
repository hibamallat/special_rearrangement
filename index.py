def special_rearrangement(nums):
     # Initialize two lists to store even and odd numbers separately
    even_numbers = []
    odd_numbers = []

    for i in range (len(nums)):
        if nums[i] % 2 == 0 :  # Check if the number is even
            even_numbers.append(nums[i])
        else:
            odd_numbers.append(nums[i])

    # Combine even numbers first, then odd number
    ordered_list = even_numbers + odd_numbers

    return ordered_list 

try:
    numbers_list = []  # Initialize an empty list for user input
    print("Enter -1 to stop")
    for i in range (8):
        num_user = int(input("Please enter a number to add to the list: "))
        numbers_list.append(num_user)
        if num_user == -1:
            numbers_list.remove(num_user)  # Remove -1 from the list
            break

    print("List of added numbers:", numbers_list)

    # Call the function to arrange numbers and print the result
    print("Arranged list (Even first, then Odd):", special_rearrangement(numbers_list))

except ValueError:
    print("INVALID: Enter a valid number")
