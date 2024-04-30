from array import array
def removeSpace(s: str):
    res = ''
    puntuation = {',', '.', '?'}
    
    l = 0
    r = 0
    
    while l <= len(s) - 1:
        
        while s[l] != " ":
          if s[r] not in puntuation:
            res += s[r]
          r += 1
          l +=1

        if res != "" and res[-1] !=' ':
          res += ' '
            
        l += 1
        r = l
        
        # while s[l] == " " and l < len(s) -1:
        #     l += 1
        #     r = l
        
        
        # print(s[l])
        # res += s[r]
        # l +=  1
        # r += 1

    print(res)
          
        
    


print(removeSpace('   Hello Geeks . Welcome   to  GeeksforGeeks   .    '))
