def test(ar,*args,**kwargs):
    print ar
    for i in args:
        print "in Args",i
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "%s == %s" %(key,value)
test(1,2,3,"99",name="viki",name1="anna")


