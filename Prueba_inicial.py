import fileinput


lines = []
for line in fileinput.input():
    lines.append(line)
suma = 0
for num in lines:
    suma+= float(num)

if suma.is_integer():
    print(int(suma))
else:
    print(suma)

#lol
