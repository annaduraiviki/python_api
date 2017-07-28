import uuid
import pdb

a=[10,2,3,4,6,7,45,77,88,99,0,11,1]
uuidtest=[2]
while (a)>0:
    if a==[]:
        pdb.set_trace()
        print "a is empty"
        pass
    else:
        i=a.pop()
        pdb.set_trace()
        print uuid.uuid4().hex
        uuidtest.append(i)
        print uuidtest

