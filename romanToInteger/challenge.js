/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const synbolVal = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    let sum = 0
    for(let i = 0; i < s.length; i++){
         if(synbolVal[s[i]] < synbolVal[s[i + 1]]){
          sum -= synbolVal[s[i]]
         }else {
             sum += synbolVal[s[i]]
         }
      }
    
    console.log(sum)

};