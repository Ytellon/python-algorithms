condition = True

while condition:
    name = input("Enter your name: ")
    print(f'Your name is {name}')

    if name == 'stop':
        break
    
print('Done')