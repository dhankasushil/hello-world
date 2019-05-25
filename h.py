print("Hello World")

i=1
while i<6 :
	i+=1
	print(i)


def fib(x) :
	if(x==0):
		return 1
	elif x==1:
		return 1
	else:
		return fib(x-1)+fib(x-2)

print("Enter number")

y=int(input())

print(fib(y))

def my_func(n):
	return lambda a : a*n


mydouble=my_func(3)

print(mydouble(2))
