# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not s:
            return True
        if (s[0] != '(') and (s[0] != '[') and (s[0] != '{'):
            return False
        for s_ in s:
            if not stack:
                stack.append(s_)
                continue
            if s_ == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif s_ == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif s_ == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s_)
        
        if stack:
            return False
        else:
            return True


if __name__ == "__main__":
    solution = Solution()
    answer = solution.isValid("{[]}")
    print(answer)
