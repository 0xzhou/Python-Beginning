# pickel

import pickle

a_dict={'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}

"""
file=open('a','wb')
pickle.dump(a_dict,file)
file.close()
"""

with open('a','rb') as file: # 自动关闭文件
    #file=open('a','rb')
    a_dict1=pickle.load(file)
    #file.close()
print(a_dict1)
