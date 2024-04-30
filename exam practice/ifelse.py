# def is_prime(n):
#     if n <=1:
#         return False #number less than or equal to 1 are not prime
#     for i in range (2, n):
#         if n %i == 0:
#             return False
#     return True
    
# n = int(input("Enter a number: "))
# if is_prime(n):
#     print(f"{n} is the prime number")
# else:
#     print(f"{n} is not a prime number")

def is_prime(n):
    if n <=1:
        return False
    for i in range (2, n):
        if n %i == 0:
            return False
        
    return True

n= int(input("Enter a number: "))
if is_prime(n):
    print(f"{n} is the prime number.")
else:
    print(f"{n} is not the prime number.")