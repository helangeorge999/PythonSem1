
# a="123abc"

# print(a.replace('w',""))

a="123abc"

b=a.maketrans("123","abc")

print(a.translate(b))