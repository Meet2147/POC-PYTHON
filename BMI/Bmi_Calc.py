class Member:
    pass

a = Member()

a.name = str(input('Enter your name'))
a.weight_kg = int(input('Enter your weight in Kgs'))
a.height_m = float(input('Enter your height in m'))

x = a.name
y = a.weight_kg
z = a.height_m
def __bmi_calc__(x, y, z):
    bmi = y / (z ** 2)
    print (bmi)
    if bmi < 25:
       return x + " is not overweight"
    else:
       return x + " is overweight"
result = __bmi_calc__(x, y, z)
print(result)






