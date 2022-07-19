# Problem # 2
import math
k = eval(input("Enter a value: "))
sum = 0
for i in range(1, k + 1):
    formula = math.sqrt(i) * 2 ** (i - 5)
    sum = formula + sum

print(format(sum, ".2f"))