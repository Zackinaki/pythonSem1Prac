# * 4. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если
#  разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на
#  два прямоугольника).
# in
# 3 2 4
# out
# yes

# in
# 3 2 1
# out
# no

n = int(input("Vvedite razmer plitki: \n"))
m = int(input("Vvedite razmer plitki: \n"))
k = int(input("Vvedite kol-vo dolek: \n"))

if k % n == 0 or k % m == 0:
    print("yes")
else:
    print("no")
