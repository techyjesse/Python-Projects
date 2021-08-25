num1 = 12
key = True

if num1 == 12:
    if key:
        print('Num1 is equal to Twelve and they have the key!')
    else:
        print('Num1 is equal to Twelve and they do not have the key!')
elif num1 < 12:
    print('Num1 is less than Twelve!')
else:
    print('Num1 is NOT equal to Twelve!')



# for loop
i = 0
for i in range(10):
    print("() iteration through the loop.".format(i))
    if i == 6:
        break
    i += 1


# while loop
i = 0
while i < 10:
    print("() iteration through the loop.".format(i))
    i += 1


# if statement in a while loop
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1
    if i == 6:
        continue

    
# else statement in a while loop
i = 2
while i < 6:
    print(i)
    i += 2
else:
    print("i is no longer less than 6")


#enumerate means to determine the index number of/or to memntion things one by one. len provides the number of character in the string.
name = 'Python'
print(len(name))
for i in enumerate(name):
    print(i)
    
    
