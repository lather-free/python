#!/usr/bin/python

import string
import math

strn=raw_input("enter number:")
m=string.atoi(strn)
print "number is:", m

n1=math.sqrt(m)
n2=math.ceil(n1)
print n1,n2
n=int(n2)
t=[[0]*n for i in range(n)]

#for m
mrow=-1
mcol=-1
cnt=0
lrow=0
hrow=n-1
lcol=0
hcol=n-1
val=n*n
if (1):
	#up side:[lrow][lcol to hcol]
	tcol=lcol
	while (tcol <= hcol):
		#t[lrow][tcol]=val
		if m == val:
		  mrow=lrow
		  mcol=tcol
		  print 'debug', mrow, mcol
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
				print 'debug1', mrow, mcol
				break
			val=val-1
			trow=trow+1
		
	if mrow < 0 and val==m:
		mrow=hrow
	elif mrow < 0:
		print 'error',val,m
		
	print 'final',mrow,mcol,val
else:
	print 'error!'		
	

#for 1
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
		
	lrow=lrow+1
	if lrow==hrow and lcol==hcol:
		break
	
	trow=lrow
	#right side:[lrow to hrow][hcol]
	while (trow <= hrow):
		t[trow][hcol]=val
		val=val-1
		trow=trow+1
		
	hcol=hcol-1
	if lrow==hrow and lcol==hcol:
		break
	
	tcol=hcol
	#down side:[hrow][hcol to lcol]
	while (tcol>=lcol):
		t[hrow][tcol]=val
		val=val-1
		tcol=tcol-1
		
	hrow=hrow-1
	if lrow==hrow and lcol==hcol:
		break
	
	trow=hrow
	#left side:[hrow to lrow][lcol]
	while (trow>=lrow):
		t[trow][lcol]=val
		val=val-1
		trow=trow-1
	
	lcol=lcol+1
	if lrow==hrow and lcol==hcol:
		break

t[lrow][lcol]=val		
cnt=0
while (cnt < n):
	print t[cnt]
	cnt=cnt+1

print mrow, mcol, lrow,lcol, hrow, hcol, val

print 'result is', abs(mrow-lrow)+abs(mcol-lcol)