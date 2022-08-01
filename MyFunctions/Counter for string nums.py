def counter(s):
    li0 = ''
    li1 = ''

    for i in s:
        if s.startswith('0'):    
            if i == '0':
                li0 += i
            elif i != '0':
                li1 += i
        return str(int(s) + 1).zfill(len(s))
    
    if all(c=='0' for c in s):
        x = 1
    else:
        x = int(li1) + 1
    
    return str(x).zfill(len(s))
    

print(counter('001'))   #002
