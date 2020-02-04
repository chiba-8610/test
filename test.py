with open('input.txt') as f:
    l=f.readlines()
    
m=int(l[-1].replace('\n',''))
pair=[]
for s in l[:-1]:
    s=s.replace('\n','').split(':')
    pair.append([int(s[0]),s[1]])
pair=sorted(pair,key=lambda x:x[0])
out=''
for tmp in pair:
    if m%tmp[0]==0:
        out+=tmp[1]

if out=='':
    print(m)
else:
    print(out)

    
