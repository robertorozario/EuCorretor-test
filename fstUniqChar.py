def firstUniqChar(str):
    splitted_str = list(str)
    for n in splitted_str:
        if splitted_str.count(n) == 1:
            print(n)
            return
    print(-1)
    return

firstUniqChar("abacabad")   # Saída: 3 ('c')
#firstUniqChar("aaabb")      # Saída: -1 (não há caracteres não repetidos)