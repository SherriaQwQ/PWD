password = 'a123456'
x = 3
pwd = password
while True:
    pwd = input('Please enter your password: ')
    if pwd == password:
        print('ENTER SUCCESFULLY!')
        break
    else:
        x = x - 1
        print('Please try it again, you have', x, 'chances.')
        if x == 0:
            break
