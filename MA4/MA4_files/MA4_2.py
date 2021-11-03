#!/usr/bin/env python3

from integer import Integer
# import matplotlib.pyplot as plt
import time
# from numpy import *

def fib_py(n):
	if n<=1:
		return n
	else:
		return (fib_py(n-1) + fib_py(n-2))

def main():
	
	#C++ timings
	nc = []
	tc = []
	for n in range(30,45):
		f = Integer(n)
		tstart = time . perf_counter ()
		f.fib()
		tstop = time . perf_counter ()
		ttaken = tstop - tstart
		tc.append(ttaken)
		nc.append(n)
	print(tc)
# 	# fib 47
# 	f = Integer(47)
# 	tstart = time . perf_counter ()
# 	f.fib()
# 	tstop = time . perf_counter ()
# 	print (f" Measured time in C++ : {tstop - tstart } seconds ")


		
	# Python timings
	np = []
	tp = []
	for n in range(30,45):
		tstart = time . perf_counter ()
		fib_py(n)
		tstop = time . perf_counter ()
		ttaken = tstop - tstart
		np.append(n)
		tp.append(ttaken)
	print(tp)
		
		
# 	plt.plot(nc,tc)
# 	plt.savefig("C++ timing.png")
# 	plt.plot(np,tp)
# 	plt.savefig("python timing.png")
	
	
# 	f = Integer(10)
# 	tstart = time . perf_counter ()
# 	f.fib()
# 	tstop = time . perf_counter ()
# 	print (f" Measured time in C++ : {tstop - tstart } seconds ")

	# f = Integer(5)
	# print(f.get())
	# f.set(7)
	# print(f.get())

if __name__ == '__main__':
	main()