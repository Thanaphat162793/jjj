def factorial(n):
    result = 1
    while n >= 2:
        result = result*n
        n = n-1
    return result
    
n = int(input('Enter the values: '))
va = factorial(n)
print(f'{va}>= 2')

