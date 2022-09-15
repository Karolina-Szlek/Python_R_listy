import re



def compression(t):
    t = re.sub(r'[^\w\s]','',t)#
    slowa = t.split()
    tab = []
    for s in slowa:
        s = list(s)
        num = 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                num +=1
                s[i-1] = num
            else:
                num = 1

        ls = s
        for i in range(1, len(s)):
            if isinstance(s[i-1], int) and isinstance(s[i], int):#
                ls[i-1] = ''
        
        ls = ''.join([str(item) for item in ls])# 
        tab.append(ls)
    return ' '.join(tab)

def decompression(skomp_tekst):
    skomp_tekst = re.sub(r'[^\w\s]','',skomp_tekst)#
    slowa = skomp_tekst.split()
    tab = []

    for s in slowa:
        s = list(s)
        ls = []
       # zle=[]
        for i in range(0, len(s)):
            
            if (s[i] in '0123456789'):
                zle=[]
                while (s[i] in '0123456789') and ( s[i+1] in '0123456789'):
                    zle.append(s[i])
                    #zle.append(s[i])
                    i+=1
                    #print(zle)
                if (s[i] in '0123456789') and ( s[i+1] is not '0123456789'):
                    zle.append(s[i])
                a =''.join(zle)
                #print(a)
                num = (int(a)-1) * s[i+1]# t
                #num = (zle -1) * s[i]
                ls.append(num)#d
            if s[i] not in '0123456789':
                ls.append(s[i])

        ls = ''.join(ls)
        tab.append(ls)
    
    return ' '.join(tab)


print(compression("aaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccddefg"))
print(decompression("3a2b4c6262de2fg"))
print(decompression("34x"))