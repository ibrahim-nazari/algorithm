

def find_largest_rectangle(buldings):
    stack=[]
    largest=0
    for index,bulding in enumerate(buldings):
        while stack and stack[-1][0] > bulding:
            h,i=stack.pop()
            largest=max(largest,h * (index-i))
        stack.append((bulding,index))
    length=len(buldings)
    while stack:
        h,i=stack.pop()
        largest=max(largest, h * (length -i))
    return largest




def main():
    t=int(input())
    for _ in range(t):
        buldings=list(map(int,input().split(",")))
        result=find_largest_rectangle(buldings)
        print(result)

if __name__ == "__main__":
    main()