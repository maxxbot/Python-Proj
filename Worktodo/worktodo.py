#Prime95 worktodo.txt file generator

import math
import numpy

prange = 100000
    

primes = []
for possiblePrime in range(127, prange + 1):

	isPrime = True
	for num in range(2, int(possiblePrime ** 0.5) + 1):
		if possiblePrime % num == 0:
			isPrime = False
			break
	if isPrime:
		primes.append(possiblePrime)
    
 
for i in range(len(primes)):
	print(primes[i])

with open('worktodo.txt', 'w') as wf:
	wf.write('[Worker #1]\n\n')
	for i in range(0 , len(primes), 4):
		wf.write('AdvancedTest=' + str(primes[i]) + '\n')
	wf.write('[Worker #2]\n\n')
	for i in range(1 , len(primes), 4):
		wf.write('AdvancedTest=' + str(primes[i]) + '\n')
	wf.write('[Worker #3]\n\n')
	for i in range(2 , len(primes), 4):
		wf.write('AdvancedTest=' + str(primes[i]) + '\n')
	wf.write('[Worker #4]\n\n')
	for i in range(3 , len(primes), 4):
		wf.write('AdvancedTest=' + str(primes[i]) + '\n')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
