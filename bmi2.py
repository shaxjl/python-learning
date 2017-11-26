height = input('height:')
weight = input('weight')

BMI = float(weight)/(float(height) * float(height))*10000
print('bmi is %f' % (BMI) )
if BMI <= 18.5:
	print('过轻')
elif BMI <= 25:
	print('正常')
elif BMI <= 28:
	print('过重')
elif BMI <= 32:
	print('肥胖')
else:
	print('严重肥胖')
