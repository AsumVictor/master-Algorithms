const FindSome = (array, target) => {
    const table = new Map()
    for (let i = 0; i < array.length; i++) {
        if(table.has(array[i])){
            return [i, table.get(array[i])]
        }
      let complement = target - array[i]
        table.set(complement, i)
    }
};

module.exports  = FindSome
