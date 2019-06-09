try:
    file=open('eeee','r+')
except Exception as e: # 接受错误并保存在e中
    print(e)
    response= input('Do you want create the new one')
    if response== 'y':
        file=open('eeee','w') # 创建新文件
    else:
        pass
else: # try successfully
    file.write('ssss')
file.close()

    
