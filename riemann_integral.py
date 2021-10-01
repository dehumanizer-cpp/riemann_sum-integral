import os

def func(x):

	return pow(x,2)#Function

#integral
a=int(input("lower limit: "))
b=int(input("upper limit: "))


#Riemann sums
for n in range(1,pow(10,9)):#As n approaches infinity
	delta_x=(b-a)/n
	xi=0
	for i in range(0,n):
		xi+=func(a+i*delta_x)*delta_x

	print(xi)
#Rieman sums

#result
os.system("cls")
print(round(xi,2))#Approximate Value