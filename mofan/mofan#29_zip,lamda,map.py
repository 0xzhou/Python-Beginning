# zip:
a=[1,2,3]
b=[4,5,6]
c=list(zip(a,b)) #合并后返回一个tupel列表
print(c)

for i,j in c:
    print(i/2,j*2)

print(list(zip(a,a,b)))

def func1(x,y):
    return(x+y)
# lambda:
func2=lambda x,y:x+y # 定义一个简单的方程，simple
func2(2,3)

# map: 是把函数和参数绑定在一起
map(func1,[1],[2]) # output is a object
print(list(map(func1,[1],[2])))

print(list(map(func1,[1,3],[2,5])))
