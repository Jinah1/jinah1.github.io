from math import sqrt

print('Pythagorean theorem calculator.')
print('Assume the sides are a, b, c and c is the hypotenuse')
formula = input('Which side (a, b, c) do you wish to calculate? side> ')
if formula == 'c':
	side_a = float(input('Input the length of side a: '))
	side_b = float(input('Input the length of side b: '))
	side_c = sqrt(side_a * side_a + side_b * side_b)
	print('The length of side c is: ', side_c)
elif formula == 'a':
    side_b = float(input('Input the length of side b: '))
    side_c = float(input('Input the length of side c: '))
    side_a = sqrt((side_c * side_c) - (side_b * side_b))
    print('The length of side a is', side_a)
elif formula == 'b':
    side_a = float(input('Input the length of side a: '))
    side_b = float(input('Input the length of side c: '))
    side_c = sqrt(side_c * side_c - side_a * side_a)
    print('The length of side b is', side_b)
else:
	print('Please select a side between a, b, c')