formula = input(": ")

#
x, y, z = formula.split(" ")

#
x_float= float(x)
z_float= float(z)

#
if y == "+":
    result = x_float + z_float
elif y == "-":
    result = x_float - z_float
elif y == "/":
    result = x_float / z_float
elif y == "*":
    result = x_float * z_float

print (result)
