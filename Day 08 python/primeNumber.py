n=int(input("Check a Number is prime OR Not :"))
def prime_Check(number=n):
    primeNum=True
    for i in range(2,number):
        if number%i ==0:
            primeNum=False
            break
        
    if primeNum:
        print("It's a Prime Number")
    else:
        print("It's not a Prime Number")

prime_Check(n)
