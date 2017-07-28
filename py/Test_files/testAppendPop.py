elements=[22,34,56,77,11,1,6,2,34,123,56,345,23,657,854,45,111]
odd=[]
even=[]
print elements
while len(elements)>0:
    element=elements.pop()
    if (element %2==0):        
        even.append(element)
        print even
    else:
        odd.append(element)
        print odd      
        print "count",elements.count(element)
    print "now the elements contains",elements    






# while len(elements)>0:
#     for element in elements:
#         if (element %2==0):        
#             even.append(element)
#             print even
#         else:
#             odd.append(element)
#             print odd
#     print "now the elements contains",elements    