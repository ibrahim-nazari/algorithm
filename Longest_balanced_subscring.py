
def find_longest_substring(s):
    n=len(s)
    longest=0
    current_count=0
    stack=[]
    for i in range(n):
        if s[i]=="(":
            current_count=0
            stack.append("(")
        else:
           if stack:
              stack.pop()
              current_count +=2
              longest=max(longest,current_count)
    return longest




def main():
    t=int(input())
    for _ in range(t):
        s=input()
        longest=find_longest_substring(s)
        print(longest)

if __name__ =="__main__":
    main()