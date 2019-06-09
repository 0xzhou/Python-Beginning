char_list=['a','a','b','b','c','c','d','d','d']

print(set(char_list)) # 序列可能改变，类似返回字典
print(type(set(char_list)))

sentence='Welcome Back to This Tutorial'
print(set(sentence)) # 区分大小写，空格也算

# print(set[char_list,sentence]) # wrong

unique_char=set(char_list)
unique_char.add('x') # 添加元素, 不能添加list
print(unique_char)
# unique_char.clear() #清除元素

print(unique_char.remove('x')) # 只是一个动作，返回值为None; 但是删除没有的元素会报错
print(unique_char)

print(unique_char.discard('y')) # 删除没有的元素不会报错
print(unique_char)

set1=unique_char
set2={'a','e','i'}
print(set2.difference(set1)) ## 返回set2中独有的
print(set1.intersection(set2))
print(set1.difference(set2))





