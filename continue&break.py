# continue&break:

# normal way
a=True
while a:
    b=input('Just type sth: ')
    if b=='1':
        a=False
    else:
        pass
print('Finish run.')

# new way

while True:
    b=input('Type sth:')
    if b=='1':
        break
    else:
        pass
print('finish the test2')
    

while True:
    b=input('Type sth:')
    if b=='1':
        continue ## jump out the loop
    else:
        pass
    print('I\'m test of continue')
print('finish the test2')
    
