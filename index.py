numbers_list = []
even_numbers = []
odd_numbers = []

def special_rearrangement(nums):
    for i in range (len(nums)):
        if nums[i] % 2 == 0:
            even_numbers.append(nums[i])
        else:
            odd_numbers.append(nums[i])

    ordered_list = even_numbers + odd_numbers
    return ordered_list
try:
    for i in range (8):
        num_user = int(input("Please enter a number to add to the list (enter -1 to stop): "))
        numbers_list.append(num_user)
        if num_user == -1:
            numbers_list.remove(num_user)
            break

    print("List of added numbers:", numbers_list)

    print("Arranged list (Even first, then Odd):", special_rearrangement(numbers_list))

except ValueError:
    print("INVALID: Enter a valid number")
