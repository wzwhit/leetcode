class Solution:
    def simplifyPath(self, path: str) -> str:
        if path == "":
            return '/'
        stack = []
        s = path.split('/')#按/分割
        for i in range(len(s)):
            if s[i] == '.' or s[i] == '':#'.'和'//'不管
                continue
            elif s[i] == '..':#'..'删除栈顶
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(s[i])#入栈
        stack2 = [str(i) for i in stack]
        out = '/'.join(stack2)#list转string
        out = '/' + out#路径开头加入'/'
        return out
