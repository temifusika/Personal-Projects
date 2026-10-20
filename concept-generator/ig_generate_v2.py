"""Editorial / 'agency-grade' concept sites for Instagram sellers.
Reuses product, booking and cake data from ig_generate.py, adds a distinct art direction per brand.
Usage: python3 concept-generator/ig_generate_v2.py
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'concepts')
ns = {'__file__': os.path.join(HERE, 'ig_generate.py')}
exec(open(os.path.join(HERE, 'ig_generate.py')).read().split('\nfor slug, s in SITES.items():')[0], ns)
V1 = ns['SITES']
T = open(os.path.join(HERE, 'ig-template-v2.html')).read()

def theme(bg, ink, muted, line, soft, accent, on, dark, light, disp, serif, sans, dw='700', dls='-.03em', htt='uppercase', ir='0px', extra=None):
    v = dict(bg=bg, ink=ink, muted=muted, line=line, soft=soft, accent=accent, **{'on-accent': on}, dark=dark, light=light,
             disp=disp, serif=serif, sans=sans, dw=dw, dls=dls, htt=htt, ir=ir)
    v.update(extra or {})
    return v

A = {}

A['tranons'] = dict(
  fonts='family=Anton&family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@400;500;600',
  vars=theme('#0D0C0A', '#EDE6D8', '#8E8677', '#2A2721', '#191714', '#C9A45C', '#0D0C0A', '#000000', '#EDE6D8',
             "'Anton',Impact,sans-serif", "'Instrument Serif',Georgia,serif", "'Inter Tight',system-ui,sans-serif", dw='400', dls='.005em',
             extra={'hsize': 'clamp(90px,21vw,360px)', 'mw': '400'}),
  pre='TRANONS', word='TRANONS', city='Lagos', tz='Africa/Lagos', logo='TRANONS<sup>®</sup>',
  hero=dict(title=['TRANONS'], pics=[3, 5, 7, 6], pos='center 20%', tl=['Tailored lifestyle & luxury', 'Lekki Phase 1 — Lagos'],
            lede='Award-winning tailoring for men and women, cut by hand in our Lagos atelier and shipped around the world.'),
  mani=dict(lab=['01 — The house', 'Est. Lekki Phase 1'], text='Every *stitch* is a decision. We cut, fit and finish by hand, for men and women who want their clothes to say *everything* before they speak.',
            side='Led by Uju Tracy Benson, Tranons dresses 223,000 followers and counting for weddings, boardrooms and every red carpet in between.'),
  primary=['Shop the season', 'shop'],
  col=dict(ghost='THE SEASON', lab='02 — The season'),
  idx=dict(title='MADE *for* YOU', note='Hover to preview, tap to shop. Every piece can be made to your measurements.',
           rows=[dict(name='Kaftans', r='Men · from ₦185,000', img=3, p=0), dict(name='Senators', r='Men · from ₦210,000', img=5, p=1),
                 dict(name='Shirts', r='Men · from ₦95,000', img=7, p=2), dict(name='Gowns', r='Women · from ₦240,000', img=6, p=3),
                 dict(name='_Bespoke_', r='Book a fitting', img=4, go='visit', cur='BOOK')]),
  dots=dict(word='TBT', stats=[['223K', 'Instagram family'], ['Global', 'Shipping'], ['№1', 'Tailored lifestyle']], hint='04 — Made in Lagos, worn worldwide'),
  mq=['Bespoke', 'Tailored', 'Lekki', 'Luxury', 'Made to measure', 'Worldwide'],
  story=dict(lab='05 — The atelier', title='HAND *made,* HEART MADE', pics=[4, 0], body=['Our team cuts and finishes every piece in Lekki. Come in for a fitting and we\'ll keep your measurements for every future order.', 'Open Tuesday to Saturday, 9am to 6pm, at 29 Fola Osibo, Lekki Phase 1.']),
  infoLab=['06 — Good to know', 'Tue–Sat · 9am–6pm'],
  info=[['29 Fola Osibo', 'Lekki Phase 1, Lagos. Walk in or book a fitting.'], ['Made to measure', 'Ready in 7–10 working days, finished by hand.'], ['Global shipping', 'Tracked to your door anywhere in the world.'], ['Pay in naira', 'Card, transfer or USSD with Paystack.']],
  cta=['Your next look', 'Got an occasion coming up?', 'SHOP NOW', 'shop', 'Tranons by Tracy'],
  nav=[['Season', 'shop'], ['House', 'story'], ['Visit', 'visit']],
  sections=['hero', 'mani', 'collection', 'index', 'dots', 'marquee', 'story', 'info', 'cta'],
)

A['white-buttons'] = dict(
  fonts='family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Fraunces:ital,opsz,wght@1,9..144,400&family=DM+Sans:wght@400;500;600',
  vars=theme('#F3ECE2', '#231710', '#7C6A5C', '#DDD0C1', '#EADFD0', '#C2552F', '#FFF8F0', '#2A1A12', '#F6EFE6',
             "'Bricolage Grotesque',system-ui,sans-serif", "'Fraunces',Georgia,serif", "'DM Sans',system-ui,sans-serif", dw='800', dls='-.045em', htt='none', ir='18px',
             extra={'hsize': 'clamp(72px,14.5vw,250px)'}),
  pre='white buttons', word='white buttons', city='Lagos', tz='Africa/Lagos', logo='white buttons',
  hero=dict(title=['white', 'buttons'], pics=[1, 0, 4, 6], pos='center 18%', tl=['Modest · Elegant · Effortless', 'Sizes 6 — 24'],
            lede='Women\'s ready-to-wear made in Nigeria, in every size from 6 to 24, and shipped worldwide.'),
  mani=dict(lab=['01 — Why we exist', '139K women and counting'], text='We make clothes for *every* body, in every room you walk into. Modest, elegant and *effortlessly* put together, from size 6 to 24.',
            side='No "closest fit". Every White Buttons style is cut in ten sizes, so the dress you love is made for you.'),
  primary=['Shop new in', 'shop'],
  col=dict(ghost='new in', lab='02 — New in this week'),
  idx=dict(title='shop *by* mood', note='Hover to preview. Every piece comes in sizes 6 to 24.',
           rows=[dict(name='Kaftans', r='Flowy · from ₦70,000', img=1, p=0), dict(name='Sets', r='Matching · from ₦68,000', img=0, p=1),
                 dict(name='Jumpsuits', r='One and done · ₦59,000', img=2, p=2), dict(name='Dresses', r='Sunday best · ₦64,000', img=4, p=4),
                 dict(name='_Size guide_', r='Find your fit', img=3, go='about', cur='FIT')]),
  dots=dict(word='6–24', stats=[['10', 'Sizes per style'], ['139K', 'Women on Instagram'], ['🌍', 'Ships worldwide']], hint='03 — Made in Nigeria'),
  mq=['Modest', 'Elegant', 'Effortless', 'Sizes 6–24', 'Made in Nigeria'],
  story=dict(lab='04 — Size guide', title='made for *every* body', pics=[4, 2], body=['Pick your usual UK size. Between sizes? Go up for kaftans and down for jumpsuits.', 'Still unsure? Message us your measurements and we\'ll choose for you. Free size swaps within 3 days.']),
  infoLab=['05 — Delivery & returns', 'Lagos · Nigeria · Worldwide'],
  info=[['Lagos in 24–48 hrs', 'Island, mainland and Lekki, tracked to your door.'], ['Worldwide', 'UK, US, Canada and beyond.'], ['Free size swap', 'Wrong size? Swap within 3 days.'], ['Pay in naira', 'Card, transfer or USSD with Paystack.']],
  cta=['New drops every week', 'Your wardrobe, sorted.', 'shop now', 'shop', 'White Buttons RTW'],
  nav=[['New in', 'shop'], ['Our story', 'story'], ['Delivery', 'visit']],
  sections=['hero', 'mani', 'collection', 'index', 'marquee', 'story', 'dots', 'info', 'cta'],
)

A['eyanga-lagos'] = dict(
  fonts='family=Playfair+Display:ital,wght@0,800;0,900;1,400&family=Archivo:wght@400;500;600',
  vars=theme('#EEECE6', '#0B0B0B', '#6B6963', '#D4D1C8', '#E2DFD6', '#A6E35E', '#0B0B0B', '#0B0B0B', '#EEECE6',
             "'Playfair Display',Didot,serif", "'Playfair Display',Didot,serif", "'Archivo',system-ui,sans-serif", dw='900', dls='-.04em',
             extra={'hsize': 'clamp(80px,19vw,330px)'}),
  pre='EYANGA', word='EYANGA', city='Lagos', tz='Africa/Lagos', logo='EYANGA',
  hero=dict(title=['EYANGA'], pics=[5, 1, 0, 2], pos='center 22%', tl=['Fashion luxury store', 'Lagos — Mon to Sat'],
            lede='Quiet luxury, loud entrance. Statement pieces hand-picked for women who arrive and own the room.'),
  mani=dict(lab=['01 — The edit', 'Bold focus. Timeless you.'], text='We don\'t do *ordinary.* Every piece in the Eyanga edit is chosen to make an entrance, and when it\'s gone, it\'s *gone.*',
            side='New arrivals land every week. Order online, get it anywhere in Nigeria, and exchange free within 48 hours.'),
  primary=['Shop the edit', 'shop'],
  col=dict(ghost='THE EDIT', lab='02 — Just landed'),
  idx=dict(title='THE *wardrobe*', note='Hover to preview. Tap to shop.',
           rows=[dict(name='Jumpsuits', r='₦145,000', img=0, p=0), dict(name='Shirts', r='₦78,000', img=1, p=1), dict(name='Sets', r='₦165,000', img=3, p=2),
                 dict(name='Skirts', r='₦120,000', img=4, p=3), dict(name='Gowns', r='₦210,000', img=2, p=4)]),
  dots=dict(word='EYANGA', stats=[['10K', 'Followers'], ['48 hrs', 'Free exchange'], ['Mon–Sat', 'In store']], hint='03 — Lagos'),
  mq=['Quiet luxury', 'Loud entrance', 'Lagos', 'The edit', 'New in weekly'],
  story=dict(lab='04 — The store', title='BOLD *focus,* TIMELESS YOU', pics=[3, 5], body=['Visit the store Monday to Friday 9am–7pm and Saturday 9am–5pm, or shop online for nationwide delivery.', 'Customer care: +234 805 842 4788 on call and WhatsApp.']),
  infoLab=['05 — Good to know', 'Customer care +234 805 842 4788'],
  info=[['Opening hours', 'Mon–Fri 9am–7pm, Sat 9am–5pm.'], ['Nationwide', 'Lagos in 24–48 hours, Nigeria in 2–5 days.'], ['Free exchange', 'Within 48 hours. No refunds.'], ['Paystack', 'Card, transfer or USSD, all in naira.']],
  cta=['Just landed', 'Your next statement piece is here.', 'SHOP', 'shop', 'Eyanga Lagos'],
  nav=[['Edit', 'shop'], ['Store', 'about'], ['Info', 'visit']],
  sections=['hero', 'mani', 'collection', 'index', 'marquee', 'story', 'dots', 'info', 'cta'],
)

A['zarakhan-boutique'] = dict(
  fonts='family=Syne:wght@600;800&family=Playfair+Display:ital,wght@1,400;1,500&family=Manrope:wght@400;500;600',
  vars=theme('#140A10', '#F5E7DC', '#A8918A', '#33212C', '#21131B', '#E0AE62', '#140A10', '#0B0509', '#F5E7DC',
             "'Syne',system-ui,sans-serif", "'Playfair Display',Georgia,serif", "'Manrope',system-ui,sans-serif", dw='800', dls='-.04em',
             extra={'hsize': 'clamp(60px,13.2vw,230px)'}),
  pre='ZARAKHAN', word='ZARAKHAN', city='Birmingham', tz='Europe/London', logo='ZARAKHAN',
  hero=dict(title=['ZARAKHAN'], pics=[3, 1, 0, 2], pos='center 30%', tl=['Bridal · Party · Festive', 'Birmingham, UK'],
            lede='Hand-embellished bridal, party and festive wear. Your website was "coming soon". Here\'s how it could look.'),
  mani=dict(lab=['01 — For the moments', '125K followers'], text='Mehndi, nikkah, walima, Eid. We dress you for the moments *everyone* remembers, in pieces embroidered, mirrored and *made* to be photographed.',
            side='Shop online with UK delivery, choose click and collect in Birmingham, or ship anywhere in the world.'),
  primary=['Shop the collection', 'shop'],
  col=dict(ghost='COLLECTION', lab='02 — The collection'),
  idx=dict(title='SHOP *by* OCCASION', note='Hover to preview, tap to shop. Alterations available in store.',
           rows=[dict(name='Bridal', r='from £245', img=3, p=1), dict(name='Party wear', r='from £165', img=1, p=0), dict(name='Menswear', r='from £95', img=0, p=2),
                 dict(name='_Weekend sale_', r='now from £45', img=9, p=4, cur='SALE')]),
  dots=dict(word='Z', stats=[['125K', 'Followers'], ['UK', '& worldwide'], ['Weekly', 'New arrivals']], hint='03 — Birmingham'),
  mq=['Bridal', 'Mehndi', 'Nikkah', 'Walima', 'Eid', 'Party wear'],
  story=dict(lab='04 — The boutique', title='COME *see* IT IN PERSON', pics=[0, 7], body=['Try on in our Birmingham boutique, with alterations by our team. Call the shop on 0121 328 7080.', 'Orders and enquiries on WhatsApp: +44 7399 143394.']),
  infoLab=['05 — Visit, collect or ship', 'Shop 0121 328 7080'],
  info=[['Click & collect', 'Order online, collect in Birmingham, usually next day.'], ['UK delivery', 'Tracked in 2–3 days, or next day.'], ['Worldwide', 'International tracked shipping.'], ['Pay your way', 'Card, Apple Pay, Klarna or PayPal.']],
  cta=['Eid, weddings, parties', 'Find the outfit before the invite lands.', 'SHOP NOW', 'shop', 'Zarakhan Boutique'],
  nav=[['Shop', 'shop'], ['Occasions', 'index'], ['Visit', 'visit']],
  sections=['hero', 'mani', 'collection', 'index', 'marquee', 'story', 'dots', 'info', 'cta'],
)

A['tinus-place'] = dict(
  fonts='family=Archivo+Black&family=DM+Serif+Display:ital@1&family=Inter:wght@400;500;600',
  vars=theme('#0E0A0C', '#FBE9F1', '#A88F9A', '#2E2228', '#1A1216', '#FF2E93', '#0E0A0C', '#000000', '#FBE9F1',
             "'Archivo Black',system-ui,sans-serif", "'DM Serif Display',Georgia,serif", "'Inter',system-ui,sans-serif", dw='400', dls='-.045em',
             extra={'hsize': 'clamp(70px,16.5vw,290px)'}),
  pre='TINUS', word='TINUSPLACE', city='Lagos', tz='Africa/Lagos', logo='TINUSPLACE',
  hero=dict(title=['TINUS', 'PLACE'], pics=[9, 5, 11, 8], pos='center 28%', tl=['#1 Trusted luxury hair vendor', 'Lagos — Worldwide'],
            lede='Hair that walks in before you do. Customise your unit, pay online and skip the back-and-forth in the DMs.'),
  mani=dict(lab=['01 — Hair, but make it luxury', '79K queens'], text='Your hair is the *first* thing they notice. So every Tinusplace unit is chosen, customised and plucked to look like it *grew* there.',
            side='Pick your length, lace and density and watch the price update. Delivered in Lagos in 24 hours, and worldwide.'),
  primary=['Shop hair', 'shop'],
  col=dict(ghost='PICK YOUR HAIR', lab='02 — Customise your unit'),
  idx=dict(title='FIND *your* HAIR', note='Hover to preview. Every unit is customisable.',
           rows=[dict(name='Body wave', r='from ₦350,000', img=8, p=3), dict(name='Balayage', r='from ₦380,000', img=5, p=0), dict(name='Layers', r='from ₦320,000', img=6, p=1),
                 dict(name='Bobs', r='from ₦180,000', img=7, p=2), dict(name='Deep wave', r='from ₦340,000', img=11, p=5)]),
  dots=dict(word='TINU', stats=[['79K', 'Queens on Instagram'], ['2026', 'Beauty in the Motherland'], ['24 hrs', 'Lagos delivery']], hint='03 — As seen at Beauty in the Motherland'),
  mq=['Frontals', 'Closures', 'Balayage', 'Bobs', 'Installs', 'Revamps'],
  story=dict(lab='04 — The studio', title='WALK IN, *glow* OUT', pics=[4, 10], body=['Try units on at our Lagos studio, book an install or a revamp, or shop online and have it delivered.', 'Exhibitor at Beauty in the Motherland 2026, Eko Hotel, Lagos.']),
  infoLab=['05 — Delivery & care', 'Lagos · Worldwide'],
  info=[['Lagos in 24 hrs', '2–5 days nationwide.'], ['Worldwide', 'Tracked to the UK, US and Canada.'], ['Installs', 'Book an install or revamp in studio.'], ['Paystack', 'Card, transfer or USSD in naira.']],
  cta=['Your next unit', 'Less time in the DMs. More compliments.', 'SHOP HAIR', 'shop', 'Tinusplace luxury hair'],
  nav=[['Hair', 'shop'], ['Studio', 'about'], ['Delivery', 'visit']],
  sections=['hero', 'mani', 'collection', 'index', 'dots', 'marquee', 'story', 'info', 'cta'],
)

A['charm-nails-spa'] = dict(
  fonts='family=Space+Grotesk:wght@500;700&family=Cormorant+Garamond:ital,wght@1,500&family=Manrope:wght@400;500;600',
  vars=theme('#F6E9E4', '#2A1418', '#86676B', '#E3CFCA', '#EEDAD4', '#B8325A', '#FFF5F2', '#2A1418', '#F6E9E4',
             "'Space Grotesk',system-ui,sans-serif", "'Cormorant Garamond',Georgia,serif", "'Manrope',system-ui,sans-serif", dw='700', dls='-.055em', ir='22px',
             extra={'hsize': 'clamp(72px,16vw,280px)'}),
  pre='CHARM', word='CHARM NAILS', city='Birmingham', tz='Europe/London', logo='CHARM',
  hero=dict(title=['CHARM'], pics=[4, 5, 6], pos='center 50%', tl=['Award-winning nail spa', 'Kingstanding, Birmingham'],
            lede='Acrylics, gel, BIAB and mani-pedis by an internationally award-winning team. Now bookable in seconds.'),
  mani=dict(lab=['01 — Charm, by name', '18K followers'], text='Award-winning *nails* shouldn\'t need a DM to book. Pick your treatment, pick your time, and you\'re *in.*',
            side='Our team has won international awards and only uses high-quality products. A £5 deposit holds your slot.'),
  primary=['Book a treatment', 'book'], headerCta=['Book', 'book'],
  idx=dict(title='OUR *work*', note='Hover to preview the sets our clients love.',
           rows=[dict(name='Gold chrome', r='Acrylic + chrome', img=4, go='book', cur='BOOK'), dict(name='Floral art', r='Gel + 3D flowers', img=5, go='book', cur='BOOK'),
                 dict(name='Autumn set', r='Acrylic + art', img=6, go='book', cur='BOOK'), dict(name='_Trophy wall_', r='International awards', img=0, go='about', cur='WOW')]),
  dots=dict(word='CHARM', stats=[['18K', 'Followers'], ['🏆', 'Award winners'], ['24/7', 'Online booking']], hint='03 — Kingstanding, Birmingham'),
  mq=['Acrylic', 'Gel', 'BIAB', 'Mani-pedi', 'Nail art', 'Award-winning'],
  story=dict(lab='04 — Recognised internationally', title='OUR *trophy* WALL', pics=[0, 1], body=['The Charm team has picked up international awards for nail artistry, and every set is done with high-quality products.', 'Friendly, professional staff in Kingstanding, Birmingham.']),
  infoLab=['05 — Good to know', 'Kingstanding, Birmingham'],
  info=[['Book 24/7', 'No waiting on a DM reply.'], ['£5 deposit', 'Comes off your bill. Free changes up to 24 hours before.'], ['Award-winning', 'International awards for nail art.'], ['Pay your way', 'Card, Apple Pay or cash in salon.']],
  cta=['Your next set', 'Nails this good deserve a proper booking page.', 'BOOK NOW', 'book', 'Charm Nails Spa'],
  nav=[['Book', 'book'], ['Work', 'index'], ['Awards', 'about']],
  sections=['hero', 'mani', 'booking', 'index', 'marquee', 'story', 'dots', 'info', 'cta'],
)
A['charm-nails-spa']['services_img'] = [4, 5, 6, 4, 5, 6]

A['luxxe-cakes'] = dict(
  fonts='family=Cormorant+Garamond:ital,wght@0,500;0,600;1,400&family=Jost:wght@400;500;600',
  vars=theme('#F5F0E8', '#121428', '#6F6C78', '#DED6CA', '#ECE4D7', '#B88A55', '#FFFFFF', '#0F1124', '#F5F0E8',
             "'Cormorant Garamond',Georgia,serif", "'Cormorant Garamond',Georgia,serif", "'Jost',system-ui,sans-serif", dw='600', dls='-.03em',
             extra={'hsize': 'clamp(80px,18vw,320px)', 'mw': '400'}),
  pre='LUXXE', word='LUXXE CAKES', city='London', tz='Europe/London', logo='LUXXE',
  hero=dict(title=['LUXXE'], pics=[2, 0, 5, 1], pos='center 40%', tl=['Luxury wedding cakes', 'London — Eggless & egg'],
            lede='Statement wedding and celebration cakes, designed around your day. Every flavour available eggless.'),
  mani=dict(lab=['01 — The last dance', '6.4K followers'], text='The cake is the *last* thing they see before the dance floor. We make sure it\'s the one they *talk* about.',
            side='Design your cake online in a minute, see it build in front of you, and get a personal quote within 24 hours.'),
  primary=['Design your cake', 'design'], headerCta=['Design', 'design'],
  idx=dict(title='MADE *for* THE DAY', note='Hover to preview recent cakes.',
           rows=[dict(name='Cascade', r='Sugar florals', img=0, go='design', cur='DESIGN'), dict(name='Six tiers', r='All white', img=1, go='design', cur='DESIGN'),
                 dict(name='Ballroom', r='Under the lights', img=2, go='design', cur='DESIGN'), dict(name='Roses & gold', r='Classic', img=3, go='design', cur='DESIGN')]),
  dots=dict(word='LUXXE', stats=[['Eggless', 'or with egg'], ['6', 'tiers and up'], ['London', 'delivery & set-up']], hint='03 — London'),
  mq=['Weddings', 'Engagements', 'Eggless', 'Sugar florals', 'Set-up included'],
  infoLab=['04 — How it works', 'London-wide'],
  info=[['Design online', 'Tiers, flavours, eggless or egg, and an instant estimate.'], ['Consultation', 'We call to perfect colours and finishing touches.'], ['Delivered & set up', 'Across London, so you don\'t have to worry.'], ['Eggless specialists', 'No compromise on taste.']],
  gallery=dict(ghost='RECENT WORK', lab='05 — Recent work', items=[[0, 'Cascading florals'], [1, 'Six-tier white'], [2, 'Under the lights'], [3, 'Roses & gold'], [5, 'Ballroom moment'], [4, 'Just married']]),
  cta=['Booking now for next season', 'Let\'s make the cake of the night.', 'DESIGN', 'design', 'Luxxe Cakes London'],
  nav=[['Design', 'design'], ['Work', 'gallery'], ['How', 'visit']],
  sections=['hero', 'mani', 'cake', 'gallery', 'index', 'dots', 'marquee', 'info', 'cta'],
)

A['cakes-and-bakes-barkingside'] = dict(
  fonts='family=Bowlby+One&family=Instrument+Serif:ital@1&family=Nunito:wght@400;600;700',
  vars=theme('#FFF3E8', '#2A1530', '#7C687F', '#F0DCCB', '#FFE6D6', '#FF4F8B', '#FFFFFF', '#2A1530', '#FFF3E8',
             "'Bowlby One',system-ui,sans-serif", "'Instrument Serif',Georgia,serif", "'Nunito',system-ui,sans-serif", dw='400', dls='-.02em', ir='26px',
             extra={'hsize': 'clamp(60px,12.5vw,220px)'}),
  pre='YUM', word='CAKES & BAKES', city='Barkingside', tz='Europe/London', logo='CAKES&amp;BAKES',
  hero=dict(title=['CAKES &', 'BAKES'], pics=[8, 9, 10, 5], pos='center 40%', tl=['Eggless celebration cakes', 'Barkingside — Since 2010'],
            lede='A little chocolate, a lot of happiness. 100% eggless cakes for birthdays, weddings and every party in between.'),
  mani=dict(lab=['01 — Since 2010', '5★ food hygiene'], text='Every cake we bake is *eggless,* so everyone at the party gets a slice. Since 2010, we\'ve made Barkingside\'s celebrations a little *sweeter.*',
            side='Design your cake in 30 seconds, choose your date and we\'ll WhatsApp you to confirm.'),
  primary=['Design your cake', 'design'], headerCta=['Order', 'design'],
  idx=dict(title='CAKES *we* LOVED', note='Hover to preview. Tap to design your own.',
           rows=[dict(name='Chocolate drip', r='Birthday', img=8, go='design', cur='YUM'), dict(name='Under the sea', r='Kids party', img=9, go='design', cur='YUM'),
                 dict(name='Pink crown', r='Princess', img=10, go='design', cur='YUM'), dict(name='Scales', r='Graduation', img=5, go='design', cur='YUM'),
                 dict(name='_Halloween_', r='Order by 31 Oct', img=3, go='design', cur='BOO')]),
  dots=dict(word='C&B', stats=[['100%', 'Eggless'], ['5★', 'Food hygiene'], ['2010', 'Baking since']], hint='03 — 59 High Street, Barkingside'),
  mq=['Birthdays', 'Weddings', 'Eggless', 'Halloween', 'Corporate', 'Since 2010'],
  infoLab=['04 — Come and see us', '59 High Street, IG6 2AD'],
  info=[['59 High Street', 'Barkingside, Ilford IG6 2AD.'], ['Eggless since 2010', 'So everyone gets a slice.'], ['5★ hygiene', 'Rated 5 and proud of it.'], ['Collect or deliver', 'Collect in store or ask about delivery.']],
  gallery=dict(ghost='FRESH FROM THE OVEN', lab='05 — Fresh from the oven', items=[[8, 'Chocolate drip'], [9, 'Under the sea'], [5, 'Scales of justice'], [6, 'Ocean ombré'], [10, 'Pink crown'], [3, 'Halloween']]),
  cta=['Party coming up?', 'Let\'s make it a sweet one.', 'ORDER', 'design', 'Cakes and Bakes Barkingside'],
  nav=[['Design', 'design'], ['Cakes', 'gallery'], ['Find us', 'visit']],
  sections=['hero', 'mani', 'cake', 'gallery', 'index', 'marquee', 'dots', 'info', 'cta'],
)

for slug, a in A.items():
    s = V1[slug]
    D = {k: s[k] for k in s if k not in ('vars', 'fonts', 'title', 'desc', 'og', 'serves_js', 'price_js', 'hero', 'story', 'info', 'cta', 'nav', 'sections', 'gallery', 'logo', 'insta', 'ticker', 'banner')}
    D.update({k: v for k, v in a.items() if k not in ('vars', 'fonts', 'logo', 'services_img')})
    if s['mode'] == 'book':
        for i, sv in enumerate(D['services']):
            sv['img'] = a['services_img'][i]
    D.setdefault('products', []); D.setdefault('closedDays', []); D.setdefault('hours', [9, 18]); D.setdefault('minDays', 1)
    D.setdefault('headerCta', ['Shop', 'shop']); D.setdefault('wa', '')
    D['footer'] = s['footer']
    data = json.dumps(D, ensure_ascii=False)
    tail = (',"serves":' + s['serves_js'] + ',"priceFn":' + s['price_js'] + '}') if 'serves_js' in s else ',"serves":t=>0,"priceFn":()=>0}'
    data = data[:-1] + tail
    jsonld = {"@context": "https://schema.org", "@type": {"shop": "ClothingStore", "book": "NailSalon", "cake": "Bakery"}[s['mode']],
              "name": s['name'], "description": s['desc'], "sameAs": [f"https://www.instagram.com/{s['handle']}/"], "image": f"img/{s['og']}.jpg"}
    if slug == 'tinus-place':
        jsonld['@type'] = 'HealthAndBeautyBusiness'
    wl = max(len(a['word']), 4)
    a['vars']['wsize'] = f'{min(19, round(100 / (wl * 0.62), 1))}vw'
    vars_ = ';'.join(f'--{k}:{v}' for k, v in a['vars'].items())
    html = (T.replace('__TITLE__', s['title'].replace('&', '&amp;')).replace('__DESC__', s['desc']).replace('__OG__', str(s['og']))
             .replace('__FONTS__', a['fonts']).replace('__VARS__', vars_).replace('__EXTRA_CSS__', a.get('css', ''))
             .replace('__HANDLE__', s['handle']).replace('__LOGO__', a['logo']).replace('__NAME__', s['name'].replace('&', '&amp;'))
             .replace('__JSONLD__', json.dumps(jsonld, ensure_ascii=False)).replace('__DATA__', data))
    open(os.path.join(OUT, slug, 'index.html'), 'w').write(html)
    print('wrote', slug)
