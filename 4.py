 # Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print "a/b result in 0"
	else:
		print c

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


#output

#Syntax Error: Because Print keyword need Parentheses for printing something
#first occur DivisionByZero Exception then haldled by except but there also a exception of Syntax error.
#so first Syntax Error and code not run
