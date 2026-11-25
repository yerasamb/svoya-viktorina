import json,sys,collections
cats=[];cur=None
for f in ['data/1.txt','data/2.txt','data/3.txt']:
    for ln in open(f,encoding='utf-8'):
        ln=ln.rstrip('\n')
        if not ln.strip(): continue
        if ln.startswith('## '):
            i,n=ln[3:].split('|');cur={'id':i,'name':n,'q':[]};cats.append(cur);continue
        p=ln.split('|')
        assert len(p)==3,ln
        cur['q'].append([int(p[0]),p[1].strip(),p[2].strip()])
tot=0
for c in cats:
    cnt=collections.Counter(q[0] for q in c['q'])
    print(c['id'],c['name'],len(c['q']),dict(cnt))
    tot+=len(c['q'])
    qs=[q[1] for q in c['q']];d=[x for x,n in collections.Counter(qs).items() if n>1]
    if d: print(' DUP',d)
print('total',tot)
json.dump({'cats':cats},open('questions.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
