class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                sum_ele = stack[-1] + stack[-2]
                stack.append(sum_ele)
            elif op == "C":
                stack.pop()
            elif op == "D":
                d_ele = (stack[-1])*2
                stack.append(d_ele)
            else:
                stack.append(int(op))
        return sum(stack)   