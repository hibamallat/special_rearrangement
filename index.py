numbers_list = [2,3,1,4,5]
even_num = []
odd_num = []

def special_rearrangement(nums):
    for i in nums:
        if i % 2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)
    rearrange_list = even_num + odd_num
    return rearrange_list
print("Numbers list:", numbers_list)
list = special_rearrangement(numbers_list)
print("Rearrange list:", list)
