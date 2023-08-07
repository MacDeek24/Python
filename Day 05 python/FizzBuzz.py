# Fizz buzz 
# number is Divisible by 3 then Fizz and 5 then Buzz If both then fizzbuzz
for i in range(1,101):
    if (i % 3 ==0) and (i % 5==0):
        i = "FizzBuzz"
    elif i % 3 ==0:
        i = "Fizz"
    elif i % 5 ==0:
        i = "Buzz"
    
    print(i)