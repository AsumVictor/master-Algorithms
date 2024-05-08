def solution(s: str, k:int):
   map = {}
   l = 0
   r = 0
   maximum_value = 0
   max_len = 0

   while l < len(s):
       
    while ((r - l + 1) - maximum_value )<= k and r <= len(s) - 1:
        map[s[r]] = map.get(s[r], 0) + 1
        maximum_value = max(maximum_value, map.get(s[r]))
        max_len = max(max_len, (r - l + 1))
        r += 1

    map[s[l]] = map.get(s[l], 0) - 1
    l += 1
      
   return max_len



print(solution('ABABAAB',2))
print('-------------------')
print(solution('AABABBA',1))
print('-------------------')
print(solution('ABCBBXBBABCCABABAAB',2))
