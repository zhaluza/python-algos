# Given a non-empty array of integers, every element appears twice except for one. Find that single one.


def single_number(nums):
    cache = {}
    for num in nums:
        if not num in cache:
            cache[num] = 1
        else:
            cache[num] += 1

    for key in cache:
        if cache[key] == 1:
            return key


list1 = [2, 2, 1]
list2 = [4, 1, 2, 1, 2]
print(single_number(list1))
print(single_number(list2))
