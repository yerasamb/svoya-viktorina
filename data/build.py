import json,collections,glob
cats=[];cur=None
for f in ['data/1.txt','data/2.txt','data/3.txt']:
    for ln in open(f,encoding='utf-8'):
        ln=ln.rstrip('\n')
        if not ln.strip(): continue
        if ln.startswith('## '):
            i,n=ln[3:].split('|');cur={'id':i,'name':n,'q':[]};cats.append(cur);continue
        p=ln.split('|')
        assert len(p) in (3,4),ln
        q=[int(p[0]),p[1].strip(),p[2].strip()]
        if len(p)==4: q.append(p[3].strip())
        cur['q'].append(q)
# anime: data/anime/*.txt, "### Title" headers; question = [level, q, a, img(""), title]
anime={'id':'anime','name':'Аниме','q':[]};sub=None
for f in sorted(glob.glob('data/anime/*.txt')):
    for ln in open(f,encoding='utf-8'):
        ln=ln.rstrip('\n')
        if not ln.strip(): continue
        if ln.startswith('### '): sub=ln[4:].strip();continue
        p=ln.split('|');assert len(p)==3 and sub,ln
        anime['q'].append([int(p[0]),p[1].strip(),p[2].strip(),"",sub])
cats.append(anime)
tot=0
for c in cats:
    cnt=collections.Counter(q[0] for q in c['q'])
    print(c['id'],c['name'],len(c['q']),dict(sorted(cnt.items())))
    tot+=len(c['q'])
print('total',tot)
json.dump({'cats':cats},open('questions.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
