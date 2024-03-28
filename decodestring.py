class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        currStr=''
        currNum=0
        for p in s:
            if p.isdigit():
                currNum=currNum*10+int(p)
            else:
                if p=='[':
                    stack.append([currStr,currNum])
                    currStr=''
                    currNum=0
                elif p==']':
                    prevStr,num=stack.pop()
                    currStr=prevStr+num*currStr
                else:
                    currStr+=p
        return currStr                    
