'''
Created on Jul 6, 2017

@author: malachi woodlee
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
sumOfFibNums, fibNum, fibNumA, fibNumB = 0,0, 1, 1

while(fibNum<4000000):
    fibNum = fibNumA + fibNumB
    if fibNum%2==0:
        sumOfFibNums = sumOfFibNums + fibNum 
    fibNumA = fibNumB
    fibNumB = fibNum
print(sumOfFibNums)
    
