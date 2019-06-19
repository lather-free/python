
#notes: this script is based on python3
'''
the algorithm is:
setp1. find position of m, which is tagged as {mrow, mcol};
setp2. find position of 1, which is tagged as {lrow, lcol}
setp3. final reslt is: abs(mrow-lrow)+abs(mcol-lcol).

#setp1.1 there are two methods to calculate the position of m
method1: to count one by one
method2: use formular

setp2.1 there are two methods to calculate the position of 1:
method1: to count one by one;
method2: use the formular;
by default we use mothod1
'''

import string
import math

strn=input("enter number:")
#m=string.atoi(strn)
m=int(strn)
print('number is: {0:10d}'.format(m))

#construct a nxn matrix
n1=math.sqrt(m)
n2=math.ceil(n1)
n=int(n2)
t=[[0]*n for i in range(n)]
print('nxn matrix, n is:{0:10d}'.format(n))

#step1: for m, find position of m. 
#mrow: row number of m
#mcol: col number of m

#setp1, method1
mrow=-1
mcol=-1
cnt=0
lrow=0
hrow=n-1
lcol=0
hcol=n-1
val=n*n

#up side:[lrow][lcol to hcol]
tcol=lcol
while (tcol <= hcol):
	#t[lrow][tcol]=val
	if m == val:
	  mrow=lrow
	  mcol=tcol
	  print ('debug', mrow, mcol)
	  break
	else:
		val=val-1
		tcol=tcol+1

if mrow < 0:
	lrow=lrow+1
	trow=lrow
	#right side:[lrow to hrow][hcol]
	while (trow <= hrow):
		if m==val:
			mrow=trow
			mcol=hcol
			print ('debug1', mrow, mcol)
			break
		val=val-1
		trow=trow+1

if mrow < 0 and val==m:
	mrow=hrow
elif mrow < 0:
	print ('error',val,m)
	
print ('position of {0:10d} is: '.format(val),mrow,mcol)

#setp1, method2
val=n*n
m_d=val-m
if m_d<n :
    mrow=0
    mcol=m_d
else:
    #print('position1 of {0:10d} is:'.format(m),m%n+1, n-1)
    mcol=n-1
    mrow=m_d-mcol
print('position1 of {0:10d} is:'.format(m),mrow,mcol)

#step2: mothod1: count one by one
cnt=0
lrow=0
hrow=n-1
lcol=0
hcol=n-1
val=n*n
while (lrow < hrow):
	#up side:[lrow][lcol to hcol]
	tcol=lcol
	while (tcol <= hcol):
		t[lrow][tcol]=val
		val=val-1
		tcol=tcol+1
	#update	
	lrow=lrow+1
	if lrow==hrow and lcol==hcol:
		break
	
    #right side:[lrow to hrow][hcol]
	trow=lrow
	while (trow <= hrow):
		t[trow][hcol]=val
		val=val-1
		trow=trow+1
	#update	
	hcol=hcol-1
	if lrow==hrow and lcol==hcol:
		break
	
    #down side:[hrow][hcol to lcol]
	tcol=hcol
	while (tcol>=lcol):
		t[hrow][tcol]=val
		val=val-1
		tcol=tcol-1
	#update	
	hrow=hrow-1
	if lrow==hrow and lcol==hcol:
		break
	
    #left side:[hrow to lrow][lcol]
	trow=hrow
	while (trow>=lrow):
		t[trow][lcol]=val
		val=val-1
		trow=trow-1
	#update
	lcol=lcol+1
	if lrow==hrow and lcol==hcol:
		break

t[lrow][lcol]=val	
print('position of {0:10d} is: '.format(1), lrow, lcol)

'''
#step2, method2: use the formular
#for 1, find position of 1
lrow = int(n/2)
lcol = lrow-1+n%2
print('position1 of {0:10d} is: '.format(1), lrow, lcol)
'''

''' debug:
cnt=0
while (cnt < n):
	print (t[cnt])
	cnt=cnt+1
'''

print ('spiral result is', abs(mrow-lrow)+abs(mcol-lcol))