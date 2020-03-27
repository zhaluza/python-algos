# Write a function which prints every number from 0 up to the given input. If divisible by 3, print "Fizz" instead of the number. If divisible by 5, print "Buzz". If input is divisible by 3 AND 5, print "FizzBuzz".


def fizzbuzz(num):
    # loop through every number from 0 up to the given input
    # if a number is divisible by 3 and 5, print 'FizzBuzz'
    # if it's divisible by 3, print 'Fizz'
    # if it's divisible by 5, print 'Buzz'

    for i in range(0, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


print(fizzbuzz(20))
