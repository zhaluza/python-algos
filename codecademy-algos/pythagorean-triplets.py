# Given a list of numbers, determine whether three numbers in the list can form a Pythagorean triplet (the square of one number equals the sum of two other squared numbers)

# brute force solution


def pythTrip(list):
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


print(pythTrip([3, 4, 5]))  # true
print(pythTrip([4]))  # false
print(pythTrip([5, 4, 3, 2]))  # true
