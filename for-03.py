# for-03.py

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)

print(result)

result = [num * 4 for num in a if num % 2 == 0]
print(result)