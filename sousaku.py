a = int(input("計算方法はどうしますか？(+ → 1 - → 2 / → 3 * → 4)"))
if a == 1:
    e,f,g = (int(x) for x in input("三つの数字を入れてください。 e f g :").split())
    print("答えは{}".format(e+f+g))

if a == 2:
    h,i,j = (int(x) for x in input("三つの数字を入れてください。 h i j :").split())
    print("答えは{}".format(h-i-j))

if a == 3:
    k,l,m = (int(x) for x in input("三つの数字を入れてください。 k l m :").split())
    print("答えは{}".format(k/l/m))

if a == 4:
    n,o,p = (int(x) for x in input("三つの数字を入れてください。 n o p :").split())
    print("答えは{}".format(n*o*p))


