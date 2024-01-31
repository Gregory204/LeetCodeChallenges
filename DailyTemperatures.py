class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []  # pair: [temp, index]
        days_stack = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            print(stack)
            while stack and t > stack[-1][0]:
                Temp, index = stack.pop()
                days_stack[index] = (i - index)
                print(Temp, index, i, days_stack)
            stack.append([t, i])
        return days_stack


temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))
