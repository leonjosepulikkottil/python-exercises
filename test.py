
#!/bin/python
#programto find last ten digits of the series  1^1+2^2+3^3.....1000^1000
result = 0

for i in range (1,1001):
        result = result + pow(i,i)

result=str(result)
l=len(result)
print result[l-10:l]

