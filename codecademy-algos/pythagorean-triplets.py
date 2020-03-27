# Given a list of numbers, determine whether three numbers in the list can form a Pythagorean triplet (the square of one number equals the sum of two other squared numbers)

# brute force solution


def pythTripBrute(list):
    # sort the list (so that all elements are in ascending order)
    # nest three loops, like a true level 10 engineer
    # Use each loop to place a pointer
    # square each number
    # add the two smallest together and see if they equal the larger square
    # If so, return true
    # Return false at the end
    list.sort()
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            for k in range(i+2, len(list)):
                if list[i] ** 2 + list[j] ** 2 == list[k] ** 2:
                    return True
    return False


# print(pythTripBrute([3, 4, 5]))  # true
# print(pythTripBrute([4]))  # false
# print(pythTripBrute([5, 4, 3, 2]))  # true

def pythTrip(list):

    # make a copy of the list
    # sort the list
    # iterate through the list and square all numbers
    # iterate backwards through the list
        # nest a while loop with two pointers
        # one pointer at start, the next before the last pointer
        # see if the two pointers equal the last number
        # if the sum is too large, decrement the outer loop
        # otherwise move the pointers

    list_copy = list.copy()
    list_copy.sort()
    for i in range(len(list_copy)):
        list_copy[i] = list_copy[i] ** 2

    i = len(list_copy) - 1
    while i >= 0:
        pointer1 = 0
        pointer2 = i - 1
        while pointer1 < pointer2 and pointer2 < i:
            if list_copy[pointer1] + list_copy[pointer2] == list_copy[i]:
                return True
            elif list_copy[pointer1] + list_copy[pointer2] < list_copy[i]:
                pointer1 += 1
            elif list_copy[pointer1] + list_copy[pointer2] > list_copy[i]:
                pointer2 -= 1
        i -= 1
    return False


print(pythTrip([3, 4, 5]))  # true
print(pythTrip([4]))  # false
print(pythTrip([5, 4, 7, 1, 9, 3, 2]))  # true
