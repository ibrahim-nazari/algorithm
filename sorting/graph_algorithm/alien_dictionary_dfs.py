def alien_order(words):
    graph={c:set() for word in words for c in word}
    for i in range(len(words) -1):
        word1,word2=words[i],words[i+1]
        minLen=min(len(word1),len(word2))
        if word1[:minLen] == word2[:minLen] and len(word2) > len(word1):
            return ""
        for char1,char2 in zip(word1,word2):
            if char1 !=char2:
                graph[char1].add(char2)
                break
    visited={}
    result=[]
    def dfs(c):
        if c in visited:
            return visited[c]
        visited[c]=False
        for nei in graph[c]:
            if not dfs(nei):
                return False
        visited[c]=True
        result.append(c)
        return True

    if not all(dfs(c) for c in graph):
        return ""
    return "".join(result[::-1])
                
        
        
        

# Test the example
words = ["wrt", "wrf", "er", "ett", "rftt"]
print(alien_order(words))  # Expected output: "wertf"
