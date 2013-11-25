def plus(arg1, arg2):
    print "arg1 is %r" % arg1
    print "arg2 is %r" % arg2
    print "and the sum is:", arg1 + arg2
    return arg1 + arg2

print "firstly, give the function numbers directly:"
plus(12, 23)

plus( plus(1,3), plus( plus(1, 2) ,5) )
