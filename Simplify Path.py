class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        directory=path.split('/')
        for dire in directory:
            if dire=='' or dire=='.':
                continue
            elif dire=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(dire)
        return '/' + '/'.join(stack)
