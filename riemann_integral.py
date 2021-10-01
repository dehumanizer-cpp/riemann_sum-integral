import os

def func(x):

	return pow(x,2)#Function

#integral
a=int(input("lower limit: "))
b=int(input("upper limit: "))


#Riemann sums
for n in range(1,pow(10,9)):#As n approaches infinity
	delta_x=(b-a)/n
	val=0
	for i in range(0,n):
		val+=func(a+i*delta_x)*delta_x

	print(val)
#Rieman sums

#result
os.system("cls")
print(round(val,2))#Approximate Value
