password_save = '123456'
password_pass = ''
repeats = 0

while password_save != password_pass:
    password_pass = input('Enter password: ')
    repeats += 1
    if repeats == 3:
        break
    
print('Password is correct')