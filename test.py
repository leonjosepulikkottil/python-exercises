#!/bin/python
result = 0

for i in range (1,1001):
        result = result + pow(i,i)

result=str(result)
l=len(result)
print result[l-10:l]

