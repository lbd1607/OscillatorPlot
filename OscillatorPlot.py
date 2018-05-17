# -*- coding: utf-8 -*-

import sys
import oscillator as osc
import matplotlib.pyplot as plt
from os import path
import os
#!/usr/bin/env python

#Laura Davis
#This program demonstrates a scientific
#simulation using scripting in Python with SciPy.
#It uses the program matplotlib to create
#an oscillator graph.

	
def main():

    
    m = osc.Oscillator('m')
    b = osc.Oscillator('b')
    c = osc.Oscillator('c')
    func = osc.Oscillator('y')
    A = osc.Oscillator('A')
    w = osc.Oscillator('w')
    y0 = osc.Oscillator('y0')
    tstop = osc.Oscillator('tstop')
    dt = osc.Oscillator('dt')
    case = 'tmp1'
    screenplot = 1

    ioPar = [m, b, c, func, A, w, y0, tstop, dt]
	
    dest = "osc_"

    #read the variables from the command line one-by-one
    while len(sys.argv) > 1:
		option = sys.argv[1];              del sys.argv[1]
		if option == '-m':
			m = float(sys.argv[1]);		   del sys.argv[1]
		elif option == '-b':
			b = float(sys.argv[1]);		   del sys.argv[1]
		elif option == '-c':
			c = float(sys.argv[1]);		   del sys.argv[1]
		elif option == '-func':
			func = sys.argv[1];			   del sys.argv[1]
		elif option == '-A':
			A = float(sys.argv[1]);		   del sys.argv[1]
		elif option == '-w':
			w = float (sys.argv[1]);	   del sys.argv[1]
		elif option == '-y0':
			y0 = float(sys.argv[1]);	   del sys.argv[1]
		elif option == '-tstop':
			tstop = float(sys.argv[1]);	   del sys.argv[1]
		elif option == '-dt':
			dt = float(sys.argv[1]);	   del sys.argv[1]
		elif option == '-noscreenplot':
			screenplot = 0;
		elif option == '-case':
			case = sys.argv[1];			   del sys.argv[1]
		else:
			print sys.argv[0],': invalid option', option
			sys.exit(1)
			
    printTerms(dest, case, ioPar)
    mainTwo(case, ioPar, screenplot, m, b, c, func, A, w, y0, dt)
		
def printTerms(dest, case, ioPar):

	if not(path.isfile(dest + case)):
		f = open('sim.dat', 'w')
		f.write("\n".join(map(str, ioPar)))
		f.close()
	else:
		f = open('sim.dat', 'w')
		f.write("\n".join(map(str, ioPar)))
		f.close()
			
#Put path to your folder for this program in destination
if __name__== '__main__':
	destination = ("...\\folderName\\")
		
def mainTwo(case, ioPar, screenplot, m, b, c, func, A, w, y0, dt):
    osc.Oscillator()
    cmd = 'oscillator %s.i' % (case)
    failure = os.system == 0
    if failure:
        print 'Running the oscillator code failed'; sys.exit(1)
		
plt.plot("sim.dat")

plt.show()

	
main()
