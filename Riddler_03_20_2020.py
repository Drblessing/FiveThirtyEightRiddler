print()
print('The FiveThirtyEight Riddler - 03/20/2020')
print('Coded with <3 by Daniel Blessing')
print('https://fivethirtyeight.com/features/how-many-sets-of-cards-can-you-find/')
print('Riddler Express: ')

print('''A quantity is continually decreasd 10 percent then increased 10 percent.
What term in this sequence is more than 50 percent less than the original quantity?
''' )

import math 
x = 1 
for i in range(1000):
	x = 0.9*1.1*x
	if x < 0.5:
		#print(i)
		break


print('Answer: 69 days')

print()
print('Riddler Classic: ')

print('1. There are 81 unique four-dimensional objects. Each dimension has 3 possible values.')
print('A set is 3 objects with all alike or all different diemsnions.')
print('What is the maximum number of objects such that there are no sets among them?')

def objects():
	x = []
	for a in range(3):
		for b in range(3):
			for c in range(3):
				for d in range(3):
					x.append([a,b,c,d])
	return x

listOfObj = objects()


