print()
print('The FiveThirtyEight Riddler - 03/13/2020')
print('https://fivethirtyeight.com/features/can-you-get-another-haircut-already/')
print('Coded with <3 by Daniel Blessing')

print('Riddler Express: ')

print('After 2^10, what is the next whole number power of 2 that comes closer to a power of 10?')

x = 2**10
y = 10**3
def pctDiff(x,y):
	return float(abs(x-y))/ y * 100
	
def closestPowTen(x):
	numDigits = len(str(x))
	minPctDiff = min(pctDiff(x,10**(numDigits-1)),pctDiff(x,10**numDigits))
	return minPctDiff

for i in range(10,100):
	if closestPowTen(2**i) <= 2.4:
		pass
		#print(i)

print('2^93 and 10^28 are closer then 2^10 and 10^4')

print('')
print('Riddler Classic: What is the average wait time for a haircut with a set of parameters?')


import random
import numpy as np

def haircut():
	return(random.uniform(0,15))
	
def waitTiff():
	return(random.random() <= 0.25)

def barbers():
	wait = []
	for i in range(4):
		wait.append(haircut())
	return(wait)

def cutDone(x):
	x = np.array(x)
	x = x-min(x)
	return(x)

def basicHairSimul(x):
	avgTotWaitTime = []
	for i in range(x):
		cusTiff = waitTiff()
		totWaitTime = 0
		brbers = barbers()
		if cusTiff:
			totWaitTime = brbers[0] + 15
		else:
			totWaitTime += min(brbers)
			brbers = cutDone(brbers)
			
			if brbers[0] == 0:
				totWaitTime += 15
			else:
				totWaitTime += brbers[0] 
		avgTotWaitTime.append(totWaitTime)
	return np.array(avgTotWaitTime).mean()

simul = 10**6
print('The average wait time for {} hairucts is {:.6} minutes'.format(simul,basicHairSimul(simul)))