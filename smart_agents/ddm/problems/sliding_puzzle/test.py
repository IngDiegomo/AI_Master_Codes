# Define your function with two arguments
def func(x, y):
    return x * y

#plan = [lambda y, x=10: func(x, y), lambda y, x='24': func(x, y), lambda y, x=25: func(x, y)]

action = lambda x=20, y = 25: func(x,y)

print(action)

# Access the x argument of the first lambda function in the plan
#x_value_first = plan[0].__defaults__[0]
#print(x_value_first)  # This will print 1

# Access the x argument of the second lambda function in the plan
#x_value_second = plan[1].__defaults__[0]
#print(x_value_second)  # This will print 3