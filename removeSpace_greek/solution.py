def solution(s: str):
    res = ''
    puntuation = {',', '.', '?'}
    
    l = 0
    r = 0
    
    while l <= len(s) - 1:
        word = ''
        while s[l] != " ":
          word += s[r]
          r += 1
          l +=1
          
        if word != '':
            if word in puntuation: 
              res += word
            else:
                if res == "":
                  res += word
                else: 
                    res += ' '
                    res += word


        l += 1
        r = l

    return(res)
