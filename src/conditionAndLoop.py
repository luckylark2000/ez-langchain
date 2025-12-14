for i in range(1,10):
    if i%2==1:
        print(i)
    else:
        print(f'{i}是偶数')
print('------------------------')
a=0
list=[]
while a<20:
    if a**2>20:
        break
    else:
        list.append(a**2)
    a+=1

print(f'20以内的整数平方和:{list}')
print('------------------------')
for x in range(1,10,2):
    print(x)