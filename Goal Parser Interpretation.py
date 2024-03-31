class Solution:
    def interpret(self, command: str) -> str:
        i=0
        goal=''
        while i < len(command):
            if (command[i] == "(" and (i + 1 < len(command) and command[i + 1] != ")")) or command[i] == ")":
                i+=1
            elif command[i]=="(" and command[i+1]==")":
                goal+=('o')
                i+=2
            else:
                goal+=command[i]
                i+=1
        return goal
