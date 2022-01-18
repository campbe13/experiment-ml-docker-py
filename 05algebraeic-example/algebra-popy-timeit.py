'''
simple example calculate
f(x,y,z)  = x + 2y + 3z
p.campbell
2022-01-06

'''
def f(x,y,z): 
    print("in f()",x ,y,z)
    return x + (2*y) + (3*z)
def mainfunc() :
    test = [ 5, 6, 10 ]
    # plain old python 
    print("using plain old python: \nresult: {} from x,y,z values  {}".format(f(test[0],test[1],test[2]), test))
    test =  [10, 10, 10]
    print("using plain old python: \nresult: {} from x,y,z values  {}".format(f(test[0],test[1],test[2]), test))

    print("using plain old python: \nresult: {} from x,y,z values  {}".format(f(3,2,1), [3,2,1]))
import timeit
print ("TIMED ", timeit.Timer(mainfunc).timeit(number=2))