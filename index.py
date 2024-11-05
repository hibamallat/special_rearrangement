numbers_list = []
even_num = []
odd_num = []

def special_rearrangement(nums):
    for i in range (len(nums)):
        if nums[i] % 2 == 0:
            even_num.append(nums[i])
        else:
            odd_num.append(nums[i])

    rearrange_list = even_num + odd_num
    return rearrange_list
try:
    for i in range (8):
        num = int(input("Please enter a number to include it in the list: "))
        numbers_list.append(num)
        if num == 0:
            numbers_list.remove(num)
            break

    print("Numbers list:", numbers_list)

    print("Rearrange list:", special_rearrangement(numbers_list))
except ValueError:
    print("INVALID: Enter a number")