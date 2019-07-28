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

#переменная до фу-ии =100
#перменная внутри фу-ии изменилась
#переменная после фу-ии осталась как и до вхождения в фу-ию
someVar=100
def varTest():
    someVar=200
    someVar+=200
    print(someVar)

varTest()
print(someVar)
#*********************************************************

def vartest2():
    fVar =10
    sVar=20
    return fVar*sVar *someVar

print(vartest2())
#********************************************************

def spaceship_building(cans):
    total_cans=0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print('Неделя %s, банок: %s' % (week, total_cans))

spaceship_building(2)
spaceship_building(13)
