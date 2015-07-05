# this example is given through www.pythontab.com
import os

def main(x):
	print "convert %s to num" % (x) 
	lambda x:sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])

if __name__=='__main__':
	result = main("192.168.1.1")
	print "result = %s" % result
