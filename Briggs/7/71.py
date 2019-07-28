def testfunc(myname):
    print('\nПривет, %s\n' % myname)

testfunc('Python')

#*************************************************
def testfunc2(fname, lname):
    print("Привет, %s %s\n" %(fname, lname))

testfunc2("New", "Python")

Fname="NEW"
Lname="Python"
testfunc2(Fname,Lname)
#**************************************************

def savings(pocket_money, paper_route, spending):
    return pocket_money + paper_route - spending

print(savings(100, 20, 40))
#**************************************************

someVar=100
def varTest():
    someVar=200
    someVar+=200
    print(someVar)

varTest()
print(someVar)