import sys
class FileSystem():
 
#     def __init__(self, files, folders, devices):
#         self.files = files
#         self.folders = folders
#         self.devices = devices
    def mul(self,x,y,o,*args,**kwargs):
        self.o=o
        kwargs={('a',"A"),(x),(y),(o),}
        print kwargs
        args=("1",x,kwargs)
        print args
        print x * y
        print (zip(args,kwargs))
a=FileSystem()
num=24*56
for i in range(num):
    
    a.mul(2,3,"Harry")
 
print(sys.getsizeof( FileSystem ))

class FileSystem1():
 
    __slots__ = ['x', 'y', 'o']
    
    def mul1(self,x,y,o,*args,**kwargs):
        self.o=o
        kwargs={('a',"A"),(x),(y),(o),}
        print kwargs
        args=("1",x,kwargs)
        print args
        print x * y
        print (zip(args,kwargs))
a=FileSystem1()
num=24*56
for i in range(num):
    
    a.mul1(2,2,"Gotcha")
 
print(sys.getsizeof( FileSystem1 ))