#A = print(int(input('Enter reference lef file scale:')))
#B = print(int(input('Enter generated lef file scale:')))
A = 5;
B = 2;

def isfloat(value):
	try:
		float(value)
		return True
	except ValueError:
		return False	

with open('../library/osu050/osu050_stdcells.lef') as osu:
	for line in osu:
		#print(line, end='')
		tabins = line.replace('  ', ' TAB#  ')
		#line.startswith((' ', '\t'))
		#print(tabins, end='')
		data = tabins.split()

		for temp in data:
			tempc = temp[:len(temp)-1]
			if(',' in temp == True):
				tempc = temp.replace(',', '')
			#print("penanda"+temp)
			if(temp == 'TAB#'):
				print('  ', end = '')
			elif(tempc.isalpha() == False and tempc.isdigit() == True):
				print(int(tempc)*B//A, end = " ")
			elif(tempc.isalpha() == False and isfloat(tempc) == True):
			#	print("dibagi"+temp);
				print(round(float(tempc)*B/A,3), end = " ")
			else:
				print(temp, end = " ");

		print()
	
