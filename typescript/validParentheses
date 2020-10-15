function isValid(s: string): boolean {
    const split : string[] = s.split('')
    const map : {[index: string]:string }  = {
        '{' : '}',
        '[' : ']',
        '(' : ')'
    }
    
    const stack: string[] = [];
    
    for(const sp of split) {
        if(sp in map) {
            stack.push(sp)
        } else {
            const latest : string | undefined = stack.pop()
            if(latest !== undefined) {
                if(map[latest] !== sp) {
                    return false;
                } 
            } else {
                return false
            }
        }
    }
    
    return  stack.length === 0 
};
