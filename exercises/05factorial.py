# Write a function to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example function call
#
# factorial(5)
#
# > 120
#






def factorial(n):
    store = n
    answer = 1
    while store > 0:
       answer *= store
       store -= 1
       print(answer)


factorial(5)