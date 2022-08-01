def counter(s):
    nl1 = ''
    nl2 = ''

    for i in s:
        if s.startswith('0'):    
            if i == '0':
                nl1 += i
            elif i != '0':
                nl2 += i
    else:
        return str(int(s) + 1).zfill(len(s))
    
    if all(c=='0' for c in s):
        x = 1
    else:
        x = int(nl2) + 1
    
    return str(x).zfill(len(s))
    

print(counter('001'))   #002
