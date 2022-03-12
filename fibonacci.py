"""
Fibonacci

Created on Mon Feb 28, 2022

@author: Th3-Al7ha10


"""
pos = input('Please enter the position of the number in Fibonacci sequence \n')

def fibonacci (k):

    if k==1:
        return 0
    else:
        return fibonacci(k-1) + k-1
    
for i in range (1,pos+1):
    print('{}e position: {}'.format(i,fibonacci(i)))
