import copy

a=[1,2,3]
b=a

print(id(a))
print(id(b))
print(id(a)==id(b))

a[2]=4
print(b)

# 浅复制：
c=copy.copy(a)
print(id(c)==id(a))
c[1]=2222
print(a)

#
a=[1,2,[3,4]]
d=copy.copy(a)
print(id(a)==id(d))

#
e=copy.deepcopy(a)
print(id(e[2])==id(a[2]))

