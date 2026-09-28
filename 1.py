a = int(input())
if a>0: print("Число", a, "положительное")
else: print("Число", a, "отрицательное")


b = int(input())
c = int(input())
if b>c: print(b,"большее")
elif c>b: print(c,"большее")
else: print(b,"равно",c)


a = int(input())
b = int(input())
x = int(input())
s = list()
for i in range(a,b+1): s.append(i)
if x in s: print("Попадает")
else: print("Не попадает")
