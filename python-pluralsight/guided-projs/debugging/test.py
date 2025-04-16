import pdb, test2

def fun2(a,b):
    print("in fun2 a,b")
    print("Nothing problematic here. Done")
    

print("Start")
pdb.set_trace()
fun2(1,2)
test2.fun(1,0)
print("End")