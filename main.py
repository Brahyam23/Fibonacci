#La sucesion de Fibonacci suma el numero actual con el numero anterior 1,1,2,3,5
print ("=====================================")
print ("Bienvenido a la sucesion de Fibonacci")
print ("=====================================")

n1,n2=0,1
while n2<=1597:
    print(n1, n2, sep=" ",  end=" ")
    n1+=n2
    n2+=n1
