# Watermelon problem, second solution
from typing import List
w = int(input("Insert the weight: "))
print("YES") if w%2 == 0 and w > 2 else print("NO")