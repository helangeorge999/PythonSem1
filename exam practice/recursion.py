# def show(n):
#     if n==0:
#         return
#     print(n)
#     show(n-1)
   

# show(10)

# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     return fact(n-1)*n
# print(fact(6))


# def calc_sum(n):
#     if (n==0):
#         return 0
#     return calc_sum(n-1) + n
# sum=calc_sum(10)
# print(sum)



# def calc_prod(n):
#     if (n==0):
#         return 1
#     return calc_prod(n-1) * n
# prod=calc_prod(3)
# print(prod)

# def print_list(list, idx=0):
#     if (idx==len(list)):
#         return
#     print(list [idx],)
#     print_list(list, idx+1)

# heroes = ["Thor", "Spider Man", "Ironman", "Captain America", "Deadpool", "Antman"]

# print_list(heroes)

def print_list(list, idx=0):
    if idx == len(list):
        return
    print(list[idx], end=" ")
    print_list(list, idx+1)

cities =["Kathmandu", "Pokhara", "Butwal", "Surkhet"]

print_list(cities)