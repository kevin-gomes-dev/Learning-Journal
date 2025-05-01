def give_fizz(n):
    if n%15 == 0:
        return 'FizzBuzz'
    if n%3 == 0:
        return 'Fizz'
    if n%5 == 0:
        return 'Buzz'
    return n

def doit(n):
    for i in range(1,n+1):
        print(give_fizz(i))
doit(3)