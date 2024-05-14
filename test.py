def fibinatschi(n):
    
    for n in range(n):
        if n %  3 ==  0 and n %  5 ==  0:
            print("FizzBuzz")
        elif n % 3 == 0 and n % 5 != 0:
            print("Fizz")
        elif n % 5 == 0 and n % 3 != 0:
             print("Buzz")
        elif n % 5 != 0 or n % 3 != 0:
            print(n)
    
def rowcount(n):
    for n in range(n+1):
        if n %  3 ==  0 and n %  5 ==  0:
            print("FizzBuzz")
        elif n % 3 == 0 and n % 5 != 0:
            print("Fizz")
        elif n % 5 == 0 and n % 3 != 0:
             print("Buzz")
        else:
            print(n)

rowcount(15)



