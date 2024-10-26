





def word_search(board,word):
    rows,cols=len(board),len(board[0])
    visited=set()
    def dfs(r,c,i):
        if i == len(word):
            return True
        if (r< 0 or r >=rows or c < 0 or c >=cols or board[r][c] !=word[i] or (r,c) in visited):
            return False
        visited.add((r,c))
        found=(  
            dfs(r+1,c,i+1) or #down
            dfs(r-1,c,i+1)or  #up
            dfs(r,c-1,i+1) or #left
            dfs(r,c + 1,i+1) #right
                )
        visited.remove((r,c))
        return found


    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,0): return True
    return False




board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

def main():
    result=word_search(board,word)
    print(result)

if __name__=="__main__":
    main()
