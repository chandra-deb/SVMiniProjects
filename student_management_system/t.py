class P:
    pass

a = [P(), P()]
for i in a:
    print(i)

l = a[0]
l.name = 'New'
m = a[1]
m.name='Few'
for i in a:
    print(i.name)
