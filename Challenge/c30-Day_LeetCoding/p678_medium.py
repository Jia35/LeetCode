# 678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/


class Solution:
    def checkValidString(self, s: str) -> bool:
        # lo = hi = 0
        # for c in s:
        #     lo += 1 if c == '(' else -1
        #     hi += 1 if c != ')' else -1
        #     if hi < 0: break
        #     lo = max(lo, 0)

        # return lo == 0

        stack = []
        for c in s:
            if c == ')':
                if stack:
                    if '(' in stack:
                        for i in range(len(stack)-1, -1, -1):
                            if stack[i] == '(':
                                stack.pop(i)
                                break
                    elif '*' in stack:
                        for i in range(len(stack)-1, -1, -1):
                            if stack[i] == '*':
                                stack.pop(i)
                                break
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(c)

        if '(' in stack:
            while '(' in stack:
                if stack[0] == '(':
                    if '*' in stack:
                        stack.remove('(')
                        stack.remove('*')
                    else:
                        return False
                else:
                    stack.remove('*')
        
        elif ')' in stack:
            while ')' in stack:
                if stack[-1] == ')':
                    if '*' in stack:
                        stack.remove(')')
                        stack.remove('*')
                    else:
                        return False
                else:
                    stack.remove('*')
        return True


if __name__ == "__main__":
    solution = Solution()
    answer = solution.checkValidString("(((((()))))**")
    print(answer)
