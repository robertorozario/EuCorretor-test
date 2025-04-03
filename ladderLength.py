def dfs(word, endWord, wordList, visited, depth):
    if word == endWord:
        return depth

    min_length = len(wordList) + 1  

    for next_word in wordList:
        if next_word not in visited and sum(a != b for a, b in zip(word, next_word)) == 1:
            visited.append(next_word)
            min_length = min(min_length, dfs(next_word, endWord, wordList, visited, depth + 1))
            visited.pop()
    
    return min_length

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    result = dfs(beginWord, endWord, wordList, [], 1) 
    return result if result <= len(wordList) else 0

# Testes
print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
