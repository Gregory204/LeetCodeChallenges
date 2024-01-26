# Koko loves to eat bananas. There are n piles of bananas,
# the ith pile has piles[i] bananas. The guards have gone and
# will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k.
# Each hour, she chooses some pile of bananas and eats k bananas
# from that pile. If the pile has less than k bananas, she eats
# all of them instead and will not eat any more bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the
# bananas before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas
# within h hours.

import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            hours = 0

            for b in piles:
                hours += math.ceil(b / m)

            if hours <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res

piles = [3,6,7,11]
h = 8
print(Solution().minEatingSpeed(piles, h))
# Output = 4

'''
class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)

        stored = float('inf')
        while l < r:
            m = ((l + r) // 2)
            cur = 0
            for b in piles:
                res = b/m
                if res == int(res):
                    cur += int(res)
                else:
                    rounded = (res + 1) // 1
                    cur += int(rounded)

            if cur >= h:
                stored = l
                if l < stored:
                    stored = l
                l = m + 1
            if cur <= h:
                stored = r
                if r < stored:
                    stored = r
                r = m - 1
        return stored


piles = [3,6,7,11]
h = 8
print(Solution().minEatingSpeed(piles, h))
# Output = 4

piles = [3, 6, 7, 11]
l = 0
r = max(piles)
m = ((l + r) // 2) + 1
cur = 0
for pile in piles:
    b = pile / m
    if b == int(b):
        cur += b
    else:
        b_rounded = (pile / m + 1) // 1
        cur += b_rounded

print(int(cur))

'''
