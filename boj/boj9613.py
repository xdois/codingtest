import sys
import math
from itertools import combinations
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    s = 0
    l = list(map(int, input().split()))
    c = combinations(l[1:],2)
    for i in c:
        s += math.gcd(i[0], i[1])
    print(s)