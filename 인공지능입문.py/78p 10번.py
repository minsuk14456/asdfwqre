def func1() :
    var = 100


def func2() :
    global var
    var = 200


var = 0
func1()
print(var)
func2()
print(var)