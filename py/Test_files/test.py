import anybox.testing.datetime
from datetime import datetime
import time

datetime.set_now(datetime(2001, 01, 01, 3, 57, 0))

print datetime.now()
print datetime.today()

print datetime.fromtimestamp(time.time())
print datetime.real_now()
datetime.real_now()
print datetime.now()



print False
print str(True)

x = (x **2 for x in range(20))
print x

x = list(x)
print x

colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print(coloured_things)

x=[1,2,3,4]
x.extend([5,6])
print x
x.append([7,8])
print x

print "this is a string".split()

print "this is a string"
print sorted("this is a string".split())

print sorted("this Is a String".split())

print sorted("this Is a String".split(), key=lambda word: word.lower())
print str.lower("Hello")[::-1]
print sorted("this Is a String".split(), key=lambda word: word.lower()[::-1])


word="abcDzX"
print word.lower()[::-1]

#str=u'\xa56'
str='sgrh'
str.encode('ascii','ignore')
str.decode()

range(7)
['a','b','c','d','e','f','g']
range(0)
print range(0)
range(7)
['a','b','c','d','e','f','g']
print range(1)
print range(6)

(a,b,c,d)=range(4)
print range(d)
print b
print c

print sorted("hello this is sodexis".split())
print ("hello this is sodexis".split())
print ("hello this is sodexis")
print sorted("hey!, this is me".split())


#num = input("Enter the number")   
num=int(5)
if num==5:
    print "Number is Right"
if num != 5:
    print "its not 5"
    
zx=max(2,3,7,89,1)
print  ("is the max number  ",zx)
    
xz=min (5347,4635,47856)
print ("Min numb is ",xz)<1

print abs(12.4)
print abs(-12.4)

print max('Gun','Pistol','Xylaphone')
print min('Gun','Pistol','Xylaphone')
print max('gun','Pistol','Xylaphone')
print min('gun','Pistol','Xylaphone')

print pow(2,4)
print 2**4

print min(max(4,5,6),max(7,8,9))
print abs(max(-2,-3,-19))


