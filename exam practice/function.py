# def calc_sum (a, b):
#     return a + b

# sum=calc_sum (1, 9)

# sum=calc_sum (38, 1)
 
# print(sum)

# print("Helan", end=" ")
# print("George")


#WAF to convert usd into npr
# def converter(usd_val):
#     npr_val = usd_val * 128
#     print(usd_val, "USD", npr_val, "NPR")

# converter (1000000)


#WAF to find a factorial
# def calc_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *=i
#     print(fact)

# calc_fact(8)

# def is_odd_or_even(number):
#     if number %2 == 0:
#         return "even"
#     else:
#         return "odd"

# number=93930
# result = is_odd_or_even(number)
# print(f"The given number {number} is {result}.")



# def calc_odd_even(num):
#     if num %2 == 0:
#         return "even"
#     else: 
#         return"odd"
    
# num=7
# result = calc_odd_even(num)
# print(f"The given number {num} is {result}.")


# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg=sum / 3
#     print(avg)
   

# calc_avg(1, 2, 3)

# def calc_oddeven(a):
#     if a %2 == 0:
#         print("even")
#     else:
#         print("odd")
        
# calc_oddeven(7)

# def calc_fact(a):
#     fact = 1
#     for i in range (1, a+1):
#         fact *= i
#     print(fact)

# calc_fact(3)

# def calc_prod(a , b):
#     prod = a*b
#     print(prod)

# calc_prod(2,3)

# def calc_add(a, b):
#     add = a+b
#     print(add)

# calc_add(3,4)


# def calc_oddeven(num):
#     if num %2 == 0:
#         print("even")
#     else:
#         print("odd")
    
# calc_oddeven(10)


# def calc_fact(a):
#     fact = 1
#     for i in range (1, a+1):
#         fact *= i
#     print(fact)
# calc_fact(5)


# num=int(input("Enter a number:"))

# def calc_oddeven(num):
#     if num %2 == 0:
#         return (f"The given number {num} is even")
#     else:
#         return (f"The given number {num} is odd")
    
# print(calc_oddeven(num))


# num=int(input("Enter a number:"))
# def calc_oddeven(num):
#     if num %2 == 0:
#         print("even")
#     else:
#         print("odd")
    
# calc_oddeven(9)



# def calc_sum(a, b):
#     total = a+b
#     return total

# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter a second number:"))

# result= calc_sum(num1, num2)
# print(f"The sum of the given numbers is {result} ")


# def calc_prod(a, b):
#     prod=a*b
#     return prod

# num1=int(input("Enter a first number:"))
# num2=int(input("Enter a second number:"))

# result = calc_prod(num1, num2)
# print(f"The product of a given numbers is {result}")

# def calc_fact(n):

#     fact = 1
#     for i in range (1, n+1):
#         fact *= i 
#     return fact

# num = int (input("Enter a Number:"))
# result = calc_fact(num)
# print(f"The factorial of given number is {result}")

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
num=int(input("Enter a number:"))
result=calc_fact(num)
print(f"The factorial of given number is {result}.")
