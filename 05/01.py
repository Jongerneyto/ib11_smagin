n = int(input())
k = int(input())
Fizz = Buzz = False
for i in range(n, k):
    if i % 3 == 0:
        print('Fizz')
        Fizz = True
    elif i % 5 == 0:
        print('Buzz')
        Buzz = True
    else:
        print(i)
if Fizz and Buzz:
    print('FizzBuzz')