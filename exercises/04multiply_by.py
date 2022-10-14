# Write a function called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a function,
# need a return statement, need a for loop to iterate over the array.
#
# Example function call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]




def multiply_by(array,num):
   i = 0
   for val in array:
    array[i] = val*num
    i += 1
    print(array)

print(multiply_by([2,4,5], 3))