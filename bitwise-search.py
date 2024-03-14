import math

def function_of_x(x):
    return x**3 - math.sin(x)

start_interval = 0
end_interval = 1
length_interval = end_interval - start_interval
step = length_interval / 4
epsilon = 0.2
reverse = False
x = 0
flag = 1

while epsilon < step: # 0.2 > 0.25
    if reverse:
        x = start_interval - step
    else:
         x = start_interval + step # 0.25

    while function_of_x(x) > function_of_x(x + step): # f(0.25) > f(0.5)
        x += step
        if reverse:
            start_interval = x - step
        else:
            start_interval = x + step
        step /= 4
        flag *= -1
        if flag < 0:
            reverse = True
        else:
            reverse = False

else:
    print(x, function_of_x(x))