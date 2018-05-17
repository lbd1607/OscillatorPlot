# -*- coding: utf-8 -*-

#Laura Davis 5 July 2017

#This program uses scipy to simulate an oscillator.

import scipy, numpy
import sys

class Oscillator:
    def __init__(self, **kwargs):
        #initialize parameters from arguments
        self.p = {'m':1.0, 'b':0.7, 'c':5.0, 'func': 'y',
                  'A': 5.0, 'w': 2*numpy.pi, 'y0': 0.2, 'tstop': 30.0, 'dt': 0.05}
        self.p.update(kwargs)
        
    def scan(self):
        #Read parameters from standard input
        read = sys.stdin.readline
        numpy.self.p = {'m': float(read()), 'b': float(read()),
                  'c': float(read()), 'func': read().strip(),
                  'A': float(read()), 'w': float(read()), 
                  'y0': float(read()), 'tstop':float(read()),
                  'dt': float(read())}
        
    def solve(self):
        #solve system
        
        self._fy = {'y': _fy, 'y3': _fy3, 'siny': _fsin}
        #set initial conditions
        self.y0 = [self.p['y0'], 0.0]
        #call scipy solver
        from scipy.numpy import sequence
        self.t = sequence(0, self.p['tstop'], self.p['dt'])
        
        from scipy.integrate import odeint
        self.yvec = odeint(self.f, self.y0, self.t)
        
        self.y = self.yvec[:, 0]    #y(t)
        #write t and y(t) to sim.dat file
        f = open('sim.dat', 'w')
        for y, t in zip(self.y, self.t):
            f.write("%s %s\n" % (t, y))
        f.close()
        
    def f(self, y, t):
        #Right-hand side of the equation
        p = self.p
        return [y[1], 
                (p['A']*numpy.cos(p['w']*t) - p['b']*y[1] -
                 p['c']*self._fy[p['func']](y[0]))/p['m']]
    
    def _fy     (y): return y
    def _fy3    (y): return y + y**3/6.0
    def _fsin   (y): return numpy.sin(y)
    
