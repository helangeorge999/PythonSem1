# a="3"
# for i in range (10):
#     print(a+a)\

# for i in range (9):
#     print("Hello World")


# cities =["Kathmandu", "Pokhara", "Butwal", "Surkhet"]
# for i in cities:
#     print (i, end=" ")

# for i in range (2):
#     x=int(input("Please enter a number between 1 to 100: "))
#     if 1<=x<=100:
#         print("valid no", x)
#         break

#     else:
#         print("Invalid Number!, Try again")


# n=5
# for i in range (n):
#     for j in range (n):
#         print("*", end="  ")

#     print()

# n=int(input("Enter a number of row:"))
# m=int(input("Enter a number of column:"))
# for i in range (n):
#     for j in range (m):
#         print("*", end='  ')
#     print()



# n=int(input("Enter a number of row:"))
# m=int(input("Enter a number of column:"))

# for i in range (n):
#     for j in range(i+1):
#         print("*", end='  ')

#     print()


# n=5;
# for i in range (n):
#     for j in range(i, n):
#         print("*", end='  ')

#     for j in range(i+1):
#         print(" ", end="  ")
#     print()

# n=5
# for i in range (n):
#     for j in range(i+1):
#         print(" ", end="  ")
#     for j in range (i,n):
#         print("*", end="  ")
   
#     print()

# n=5
# for i in range (n):
#     for j in range (i+1):
#         print(" ", end="  ")
#     for j in range (i,n-1):   
#         print("*", end="  ")
#     for j in range (i,n):
#         print("*", end="  ")
#     print()

n=5
for i in range (n-1):
    for j in range (i,n):
        print(" ",end="  ")
    for j in range (i):
        print("*", end="  ")
    for j in range (i+1):
        print("*", end="  ")
    print()

for i in range (n):
    for j in range (i+1):
        print(" ", end="  ")
    for j in range (i,n-1):   
        print("*", end="  ")
    for j in range (i,n):
        print("*", end="  ")
    print()

   
