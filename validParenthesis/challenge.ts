function isValid(s: string): boolean {

    const parenthesis: object = {
        "(": ")",
        "{": "}",
        "[" :"]",
    }
    
    let stack: string[] = []
    
    for(let i: number = 0; i < s.length; i ++){
        if(parenthesis[s[i]]){
            stack.push(s[i])
        }else if(parenthesis[stack[stack.length -1]] === s[i])  {
            stack.pop()
        }else {
            stack.push(s[i])
        }
    }


    return stack.length === 0
    
    };