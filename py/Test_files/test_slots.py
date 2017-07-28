# import ipython_memory_usage.ipython_memory_usage as imu
class MyClass(object):
        __slots__ = ['name', 'identifier']
        def __init__(self, name, identifier):
                self.name = name
                self.identifier = identifier
                
num = 100*100
x = [MyClass(1,1) for i in range(num)]
print x

class MyClass2(object):
        def __init__(self, name, identifier):
                self.name = name
                self.identifier = identifier

num = 100*100
x = [MyClass2(1,1) for i in range(num)]
print x
