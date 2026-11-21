class Solution:
    def calculate(self, s: str) -> int:
        curr_num = 0
        curr_op = "+"
        res = 0
        i = 0
        n = len(s)
        stack = []
        while i < n:
            if s[i].isdigit():
                while i < n and s[i].isdigit():
                    curr_num = curr_num * 10 + int(s[i])
                    i += 1
                i -= 1
                
                if curr_op == "+":
                    stack.append(curr_num)
                    curr_num = 0


                elif curr_op == "-":
                    stack.append(-curr_num)
                    curr_num = 0

                elif curr_op == "*":
                    stack.append(curr_num * stack.pop())
                    curr_num = 0
                else:
                    stack.append(int(float(stack.pop()) / curr_num))
                    curr_num = 0

            elif s[i] != " ":
                curr_op = s[i]

            i += 1
        return sum(stack)



               

        