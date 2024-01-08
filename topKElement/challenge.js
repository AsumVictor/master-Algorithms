/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const freqencyTable  = new Map()
    for(let i = 0; i < nums.length; i++){
      if(freqencyTable.has(nums[i])){
          freqencyTable.set(nums[i],  freqencyTable.get(nums[i]) + 1)
      }else {
               freqencyTable.set(nums[i],  1)     
      }
    }


    console.log([...freqencyTable].sort((a, b)=>{
        return b[1] - a[1]
    }).map(a=>a[0]).slice(0, k))
};