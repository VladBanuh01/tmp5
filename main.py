print('hello')
a = {}
a.update({'name': 'vlad'})
print(a)
c = '''arfar
... argadgatg
... ategaethryhyr'''
c
'arfar\nargadgatg\nategaethryhyr'
print(c)
s1 = 'sava'
s2 = 'eggs'
print(s1 + s2)
print('spam' * 5)
s = 'savaeggs'
i = 6
while i < 15:
    print(i)
    i = i + 2
    pass
for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end='')

# Bytearray
bs2 = bytearray(b"hello world!")
print(bs[0])
print(bs2)
bs2[0] = 105
print(bs2)
# Numbers
x = 10
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(-x, -y)
print(abs(x), abs(y))
print(divmod(x, y))
print(x ** y)
print(pow(x, y, 3))

# Lists
l = [2, 4, 6]
