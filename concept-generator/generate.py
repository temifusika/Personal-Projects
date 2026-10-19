"""Generate personalised concept pages from a JSON list of businesses.
Usage: python3 concept-generator/generate.py concept-generator/businesses.json concepts   (writes ../<slug>/index.html, prints slug map)"""
import json,re,sys,os
HERE=os.path.dirname(os.path.abspath(__file__))
SERV={
 'Barber':[['Skin fade',18,'Clipper fade, finished with scissors'],['Haircut',15,'Scissor or clipper cut'],['Haircut & beard',25,'Cut plus beard shape-up'],['Beard trim',10,'Line-up and shape'],['Hot towel shave',15,'Traditional cut-throat shave'],['Kids cut',12,'Under 12s']],
 'Hair salon':[['Cut & blow-dry',45,'Consultation, wash, cut and finish'],['Blow-dry',25,'Wash and style'],['Full colour',70,'Root to tip'],['Half-head highlights',85,'Foils, toner included'],['Treatment',20,'Conditioning treatment']],
 'Nail salon':[['Gel manicure',25,'Shape, cuticle care and gel colour'],['BIAB overlay',35,'Builder gel on natural nails'],['Acrylic full set',35,'Any length and shape'],['Infills',25,'Within 3 weeks'],['Gel pedicure',30,'Soak, scrub and gel colour'],['Nail art',5,'Per nail, from']],
 'Beauty salon':[['Lash extensions',45,'Classic full set'],['Brow lamination',35,'Includes tint'],['Facial',40,'45-minute treatment'],['Waxing',10,'From'],['Lash lift',35,'Includes tint']],
}
LEDE={'Barber':'Fresh cuts, sharp fades and beard work in {city}. Book your slot online in under a minute, or call ahead.',
 'Hair salon':'Cuts, colour and styling in {city}. See prices and book your appointment online, any time.',
 'Nail salon':'Gel, BIAB, acrylics and nail art in {city}. Check prices and book your appointment online.',
 'Beauty salon':'Lashes, brows and treatments in {city}. Check prices and book online.'}
SUB={'Barber':'Straightforward prices, no surprises.','Hair salon':'Clear prices for every service.','Nail salon':'Clear prices for every treatment.','Beauty salon':'Clear prices for every treatment.'}
LABEL={'Barber':'Barbers','Hair salon':'Hair salon','Nail salon':'Nail salon','Beauty salon':'Beauty salon'}
CAR=[['Wash & vac',12,'Exterior hand wash and interior vacuum',1,False],['Snow foam wash',10,'Exterior only, hand dried',1,False],
     ['Mini valet',25,'Wash, vac, dash and windows',2,True],['Full valet',70,'Inside and out, seats shampooed',5,True],
     ['Interior deep clean',50,'Seats, carpets and mats',4,True],['Engine bay clean',15,'Degrease and dress',0,True]]
NEG=re.compile(r"\b(rude|worst|never|terrible|awful|waste|wasted|disappoint|avoid|unprofessional|bad|poor|scratch|damage|refund|not happy|wouldn't|won't)\b",re.I)
POS=re.compile(r"\b(great|best|amazing|excellent|recommend|friendly|brilliant|fantastic|lovely|professional|perfect|love|loved|top|happy|spotless)\b",re.I)
def clean(t): return re.sub(r'[   ]',' ',t).replace(' – ','–').replace('–',' – ')
def quotes(texts,n=3):
    out=[]
    for t in texts:
        t=' '.join(t.split())
        if NEG.search(t) or not POS.search(t): continue
        if len(t)>170:
            cut=t[:170]; m=max(cut.rfind('. '),cut.rfind('! '))
            t=cut[:m+1] if m>60 else cut[:cut.rfind(' ')]+'…'
        out.append(t)
        if len(out)==n: break
    return out
def phone(p):
    if not p: return ''
    return p.replace('+44 ','0')
def slug(n,used):
    s=re.sub(r'[^a-z0-9]+','-',n.lower()).strip('-')[:40].strip('-')
    b=s;i=2
    while s in used: s=f'{b}-{i}';i+=1
    used.add(s); return s
def main(src,outdir):
    B=json.load(open(src)); used=set(); m={}
    for b in B:
        cat=b['category']; car=cat.startswith('Car wash')
        hours=[]
        for h in b.get('hours',[]):
            d,_,v=clean(h).partition(': '); hours.append([d,v])
        name=re.sub(r'\s*\|.*$','',b['name']).strip()
        data=dict(name=name,city=b['city'],address=re.sub(r',\s*UK$','',b['address']),rating=float(b['rating']),reviews=int(b['reviews']),phone=phone(b.get('phone')),
                  hours=hours,quotes=quotes(b.get('review_texts',[])))
        if car:
            data.update(services=CAR,lede=f'Hand car wash and valeting in {b["city"]}. See prices for your car, then drive in or book a valet online.')
            tpl='carwash.html'
        else:
            data.update(theme='barber' if cat=='Barber' else 'salon',label=LABEL[cat],services=SERV[cat],lede=LEDE[cat].format(city=b['city']),svcsub=SUB[cat])
            tpl='salon.html'
        html=open(os.path.join(HERE,tpl)).read()
        html=html.replace('{{NAME}}',name.replace('&','&amp;').replace('<','&lt;')).replace('{{DATA}}',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
        s=slug(name,used); os.makedirs(os.path.join(outdir,s),exist_ok=True)
        open(os.path.join(outdir,s,'index.html'),'w').write(html)
        m[b['place_id']]=dict(slug=s,quotes=len(data['quotes']))
    json.dump(m,open(os.path.join(HERE,'slugs.json'),'w'),indent=1)
    print(len(m),'pages')
if __name__=='__main__': main(sys.argv[1],sys.argv[2])
