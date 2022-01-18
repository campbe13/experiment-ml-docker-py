'''
ssimple example using plain old python to determine 
when to wear a coat 


p.campbell
2022-01-13

'''
def checktemp(temp): 
    if temp < 10:
        return 'a coat'
    else:
        return 'none'
        
test = [ 5, 6, 10, 15, 35]

print("using plain old python:")
for i in test:
    print("When it's {} degrees  wear {}".format(i, checktemp(i)))
