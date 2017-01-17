from math import log as l
n=input()
N=n*int(l(n)+l(l(n)))
a=range(2,N)
for i in range(int(n**.5)+1):
 a=filter(lambda x:x%a[i] or x==a[i],a)
print a[:n]
