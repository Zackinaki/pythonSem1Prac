# Найдите сумму цифр трехзначного числа.
# in
# 123
# out
# 6

# in
# 100
# out
# 1

n = int(input("Vvedite trehznachnoe chislo: \n"))

a = n % 10
b = (n//10) % 10
c = n//100

x = a+b+c
print("Summa cifr chisla", n, "ravna", x)
