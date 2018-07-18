def func() :
    (a ,b) = ('1', 3)
    if type(a) == type('a') :
        raise TypeError
    else :
        c = a + b
        return c

try :
    func()
except TypeError :
    print ('TypeError')
else :
    print (func())