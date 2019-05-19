test='This is my first test.\nThis is next line.\nThis is last line'
print(test)


# open('filename','the way: r,w,a')
my_file=open('my_file.txt','w')
my_file.write(test)
my_file.close() # clode the file

# how can we change the PATH


# edit the file
append_test='\nThis is appended file.'
my_file=open('my_file.txt','a') # 'a'=append
my_file.write(append_test)
my_file.close()

print('\n\n')
file=open('my_file.txt','r') # read
content=file.read()
print(content)

file2=open('my_file.txt','r')
list1=file2.readlines()
print(list1)
