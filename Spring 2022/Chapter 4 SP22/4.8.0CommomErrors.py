# The top one will yield a result
i = 1
j = 2
k = 3

if i > j:
    if i > k:
        print('A')
else:
    print('B')

# This will not yield a result
a = 1
b = 2
c = 3

if a > b:
    if a > c:
        print('Y')
    else:
        print('Z')