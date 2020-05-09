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

l.append(4)
print(l)
l.extend([5, 6])
print(l)
l.insert(0, 0)
print(l)
l.remove(0)
print(l)
print(l.pop(2))
l.sort()
print(l)
l.reverse()
print(l)
print(l.count(5))
l2 = l.copy()
print(l2)
l.clear()
print(l)

# Indexes and slices

d = [1, 15, 45, 32, 4, 0]
print(d[0])
print(d[-1])
print(d[2:])
print(d[:])
print(d[:4])
print(d[::2])
print(d[::-1])
print(d[:-2])
print(d[1:4:-1])
del d[-3]
print(d)
print(d[-2::-1])

#Tuples
a = (1, 2, 3, 4, 5, 6, )
print(a.__sizeof__())
print(tuple("Hello "))
b = ("d",)
print(b)
print(a[3])
print(a[:-1])
print(a[2:5])

#Set mutables
# Set mutable
a = set()
print(a)
a = set("hello")
a = {"a", "b", "c", "d"}
print(a)
words = [2, 4, 20, 40]
set_words = set(words)
print(len(set_words))
print("hello" in set_words)
set_words2 = set_words.copy()