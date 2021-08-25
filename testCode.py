

mySentence = 'loves the color'

color_list = ['red','blue','green','pink','black']

# .format adds the color_list item to the printed string
def color_function(name):
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name,mySentence,i)
        lst.append(msg)
    return lst

# Jesse is the argument added in the name section in the above block.
lst = color_function('Jesse')
for i in lst:
    print(i)
    
def get_name():
    go = True
    while go:
        name = input('What is your name?')
        if name == '':
            print("You need to provide your name.")
        elif name == 'Jesse':
            print("Jesse, you are hecka handsome today but you cant use this software.")
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()

cars = ['bmw','volvo','chevy','ford','nissan']
x = cars.count('')
print(x)

y = lambda a : a + 10
print(y(5))

# {} placeholders call the objects from the parentheses below and plug them into the string.
location1 = "Portland"
location2 = "Maui"
location3 = "Sacramento"
print("I flew from {} to {} to {}.".format(location1, location2, location3))
