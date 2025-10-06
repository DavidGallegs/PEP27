# FORMA 1
for i in range(11):
    if i % 2 == 0:
        print(i)

# FORMA 2
for i in range(11):
    if i % 2 != 0:
        continue
    print(i)

# FORMA 3
i = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

# FORMA 4
i = 0
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1