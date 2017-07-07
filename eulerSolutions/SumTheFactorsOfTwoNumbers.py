'''
Created on Jul 6, 2017

@author: Malachi Woodlee
@note: Project Euler


If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

a, b = 3, 5
counter = 0
runningSum = 0
while counter<1000:
    if counter % a == 0 or counter % b ==0:
        runningSum = runningSum + counter
    counter+=1
print(runningSum)
