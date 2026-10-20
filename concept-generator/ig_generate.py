"""Generate Instagram-seller concept sites from ig-template.html.
Usage: python3 concept-generator/ig_generate.py   (writes concepts/<slug>/index.html)
"""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'concepts')
T = open(os.path.join(HERE, 'ig-template.html')).read()

def vars_(d):
    return ';'.join(f'--{k}:{v}' for k, v in d.items())

NG_DELIVERY = [["Lagos Mainland (24–48 hrs)", 3500], ["Lagos Island & Lekki (24–48 hrs)", 5000], ["Nationwide (2–5 days)", 9000], ["International (DHL, 5–7 days)", 45000]]
NG_PAY = ["Card, bank transfer or USSD (Paystack)", "Pay with Flutterwave", "Pay on delivery (Lagos only)"]
UK_PAY = ["Card, Apple Pay or Google Pay", "Pay in 3 with Klarna", "PayPal"]

SITES = {}

SITES['tranons'] = dict(
  handle='tranonsluxury', name='Tranons by Tracy', logo='TRANONS<small>by Tracy</small>', cur='NGN', mode='shop', og=3,
  title='Tranons by Tracy | Tailored lifestyle & luxury, Lekki Lagos',
  desc='Award-winning tailored menswear and womenswear from Lekki Phase 1, Lagos. Shop ready-to-wear, book a bespoke fitting, global shipping.',
  fonts='family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Manrope:wght@400;500;600;700',
  vars=dict(bg='#F7F3EC', ink='#111', muted='#6B655C', line='#E2DACB', soft='#EFE8DC', card='#FFFDF8', accent='#C29A4B', accent2='#E7CF95', **{'on-accent':'#111'},
            display="'Cormorant Garamond',Georgia,serif", body="'Manrope',system-ui,sans-serif", **{'hero-bg':'#0D0D0D','hero-ink':'#F7F3EC'}, ir='4px', r='2px', dw='500'),
  nav=[['Shop','shop'],['Bespoke','story'],['Visit','visit']],
  hero=dict(eyebrow='Award-winning · Lekki Phase 1', title='Tailored to the *last* stitch.', lede='Tailored lifestyle and luxury for men and women, cut in our Lagos atelier and shipped around the world.',
            cta=['Shop the collection','shop'], cta2=['Book a fitting','visit'], badges=['<b>223K</b> on Instagram','Global shipping','Bespoke & ready-to-wear'], pics=[3,6,5,7], stamp=['№1','Tailored lifestyle']),
  ticker=['Bespoke tailoring','Ready to wear','Global shipping','29 Fola Osibo, Lekki Phase 1','Tue–Sat, 9am–6pm'],
  shopTitle='The <em>new</em> season', products=[
    dict(name='The Onyx Kaftan Set', cat='Men', img=3, price=185000, tag='New', desc='Relaxed black kaftan and trouser set in a soft, structured weave. Cut to order in our atelier.'),
    dict(name='Emerald Senator', cat='Men', img=5, price=210000, tag='Bestseller', hot=True, desc='A modern senator in deep emerald with a clean placket and tapered trouser.'),
    dict(name='Noir Pleated Shirt', cat='Men', img=7, price=95000, desc='Fine vertical pleats, long sleeves, a quiet statement for evenings.'),
    dict(name='Merlot Halter Gown', cat='Women', img=6, price=240000, tag='Limited', desc='A sculpted halter neckline in rich merlot, made to your measurements.'),
  ],
  defaultOpts=[['Size',['S','M','L','XL','Made to measure'],[0,0,0,0,35000]]],
  quickNote='Every piece is finished by hand. Made-to-measure orders take 7–10 working days.',
  story=dict(pics=[4,0], eyebrow='The atelier', title='Made by hand, *worn* for life.'.replace('*',''), body=['Tranons by Tracy is an award-winning tailoring house led by Uju Tracy Benson, dressing men and women for the moments that matter.','Book a fitting at our Lekki studio, or order made-to-measure from anywhere in the world.'],
             facts=[['223K','Instagram followers'],['Global','shipping'],['Tue–Sat','9am–6pm']]),
  infoTitle='Visit the atelier', info=[['📍','29 Fola Osibo, Lekki Phase 1','Open Tuesday to Saturday, 9am to 6pm.'],['✂️','Bespoke fittings','Book a 45-minute fitting online and we\'ll have your measurements ready for every future order.'],['✈️','Global shipping','Tracked delivery across Nigeria and worldwide, with duties shown at checkout.'],['💳','Pay your way','Card, transfer or USSD with Paystack, all in naira.']],
  insta=[3,5,6,7,4,0], followers='223K', instaTitle='Seen on the gram',
  cta=['Your next look', 'Dressed for every room you walk into.', 'Shop now', 'shop'],
  sections=['hero','shop','story','info','insta','bigcta'],
  delivery=NG_DELIVERY, pay=NG_PAY, payNote='Secure payment by Paystack. You\'ll get a receipt by SMS and email.', orderPrefix='TRN',
  doneNote='We\'ll send updates on WhatsApp as your order is finished and shipped.', wa='https://wa.me/message/GJNIOCTWWCBBP1',
  footer='29 Fola Osibo, Lekki Phase 1, Lagos · Tue–Sat 9am–6pm',
)

SITES['white-buttons'] = dict(
  handle='whitebuttons.ng', name='White Buttons', logo='white buttons<small>RTW</small>', cur='NGN', mode='shop', og=1,
  title='White Buttons | Modest, elegant women\'s ready-to-wear, sizes 6–24',
  desc='Modest, elegant, effortlessly put together. Women\'s ready-to-wear made in Nigeria in sizes 6 to 24, shipped worldwide.',
  fonts='family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=DM+Sans:wght@400;500;600;700',
  vars=dict(bg='#FBF6EF', ink='#2A1F1A', muted='#7A6A5E', line='#EADFD2', soft='#F3E8DB', card='#FFFCF8', accent='#C0532F', accent2='#E6A93A', **{'on-accent':'#fff'},
            display="'Fraunces',Georgia,serif", body="'DM Sans',system-ui,sans-serif", ir='22px', dw='400'),
  nav=[['New in','shop'],['Size guide','story'],['Delivery','visit']],
  hero=dict(eyebrow='Made in Nigeria · Sizes 6–24', title='Modest. Elegant. *Effortless.*', lede='Ready-to-wear for women who like to look put together without trying too hard. Every style, every size from 6 to 24.',
            cta=['Shop new in','shop'], cta2=['Find your size','story'], badges=['<b>139K</b> women follow us','Ships worldwide','Sizes 6 to 24'], pics=[1,0,4,6], stamp=['6–24','every style, every size']),
  ticker=['New drops every week','Sizes 6 to 24','Made in Nigeria','Ships worldwide','Modest · Elegant · Effortless'],
  shopTitle='Pieces you\'ll *live* in'.replace('*',''), products=[
    dict(name='Ivory Lace Boubou', cat='Kaftans', img=1, price=85000, tag='Bestseller', hot=True, desc='Flowing ivory lace with a soft lining. Throw it on for a wedding, a dinner or Sunday service.'),
    dict(name='Rosa Print Kaftan Set', cat='Sets', img=0, price=68000, tag='New', desc='Bold rose print on black, cape-sleeve top and matching trousers.'),
    dict(name='Midnight Wide-Leg Jumpsuit', cat='Jumpsuits', img=2, price=59000, desc='Navy wide-leg jumpsuit with a cinched waist. Office to dinner in one piece.'),
    dict(name='Monochrome Robe Set', cat='Sets', img=3, price=72000, desc='Graphic black-and-white print in an easy robe and trouser pairing.'),
    dict(name='Sunburst Ankara Dress', cat='Dresses', img=4, price=64000, tag='New', desc='A golden ankara maxi with a relaxed fit and deep pockets.'),
    dict(name='Heritage Print Kaftan', cat='Kaftans', img=6, price=70000, desc='Earthy prints in a breezy kaftan cut that flatters every shape.'),
  ],
  defaultOpts=[['Size',['6','8','10','12','14','16','18','20','22','24']],['Length',['Regular','Tall (+2")']]],
  quickNote='Not sure of your size? Message us your measurements and we\'ll pick it for you.',
  story=dict(pics=[4,2], eyebrow='Size guide', title='Made for every body, 6 to 24', body=['Every White Buttons style is cut in ten sizes, from 6 to 24, so nobody has to settle for "the closest fit".','Pick your usual UK size. If you\'re between sizes, go up for kaftans and down for jumpsuits.'],
             facts=[['10','sizes per style'],['139K','women on Instagram'],['🇳🇬','made in Nigeria']]),
  infoTitle='Delivery & returns', info=[['🚚','Lagos in 24–48 hours','Island, mainland and Lekki, tracked to your door.'],['🌍','Worldwide shipping','UK, US, Canada and beyond, with tracking all the way.'],['📏','Free size swap','Wrong size? Swap it within 3 days of delivery.'],['💳','Pay in naira','Card, transfer or USSD with Paystack.']],
  insta=[0,1,2,3,4,6], followers='139K', instaTitle='Styled by you',
  cta=['New drops every week','Your wardrobe, sorted.','Shop new in','shop'],
  sections=['hero','shop','story','info','insta','bigcta'],
  delivery=NG_DELIVERY, pay=NG_PAY, payNote='Secure payment by Paystack.', orderPrefix='WB',
  doneNote='Your order is being packed. We\'ll WhatsApp you the tracking link.', wa='https://wa.me/+2349016811123',
  footer='Women\'s ready-to-wear · Made in Nigeria · Ships worldwide',
)

SITES['eyanga-lagos'] = dict(
  handle='eyangalagos', name='Eyanga Lagos', logo='EYANGA<small>Lagos</small>', cur='NGN', mode='shop', og=5,
  title='Eyanga Lagos | Fashion luxury store',
  desc='Eyanga Lagos fashion luxury store. Shop statement pieces online with nationwide delivery and free exchange within 48 hours.',
  fonts='family=Bodoni+Moda:ital,opsz,wght@0,6..96,500;1,6..96,500&family=Jost:wght@400;500;600',
  vars=dict(bg='#F4F2ED', ink='#0F0F0F', muted='#6A6862', line='#DEDAD1', soft='#E9E5DC', card='#FBFAF7', accent='#5FA83A', accent2='#C7E3A8', **{'on-accent':'#0F0F0F'},
            display="'Bodoni Moda',Georgia,serif", body="'Jost',system-ui,sans-serif", **{'hero-bg':'#0F0F0F','hero-ink':'#F4F2ED'}, ir='0px', r='0px', dw='500', lls='.18em'),
  nav=[['Shop','shop'],['The edit','story'],['Store','visit']],
  hero=dict(eyebrow='Fashion luxury store · Lagos', title='Quiet luxury, *loud* entrance.', lede='Statement pieces chosen for women who arrive and own the room. Shop online and get it delivered anywhere in Nigeria.',
            cta=['Shop the edit','shop'], cta2=['Visit the store','visit'], badges=['<b>10K</b> on Instagram','Nationwide delivery','Free exchange in 48 hrs'], pics=[5,1,0,2], stamp=None),
  ticker=['New arrivals weekly','Nationwide delivery','Free exchange within 48 hours','Open Monday to Saturday','Customer care +234 805 842 4788'],
  shopTitle='The <em>edit</em>', products=[
    dict(name='Noir Cinch Jumpsuit', cat='Jumpsuits', img=0, price=145000, tag='New', desc='Black utility jumpsuit with a sculpted waist and dramatic sleeves.'),
    dict(name='Alabaster Batwing Shirt', cat='Tops', img=1, price=78000, tag='Bestseller', hot=True, desc='Crisp white poplin with a batwing sleeve and cinched hem.'),
    dict(name='The Boardroom Set', cat='Sets', img=3, price=165000, desc='Structured white shirt with a black pleated midi. Meetings, then dinner.'),
    dict(name='Taffeta Midi Skirt', cat='Skirts', img=4, price=120000, desc='Full black taffeta that moves when you do.'),
    dict(name='Midnight Halter Gown', cat='Dresses', img=2, price=210000, tag='Limited', desc='Halter neck, full skirt, made for the red carpet and every party after.'),
  ],
  defaultOpts=[['Size',['XS','S','M','L','XL']]],
  quickNote='No refunds, but free exchange within 48 hours of delivery.',
  story=dict(pics=[5,3], eyebrow='The edit', title='Bold focus. Timeless you.', body=['Eyanga Lagos curates luxury fashion for women who dress with intention: sharp tailoring, sculpted silhouettes and pieces that photograph beautifully.','Every arrival is hand-picked, so when it\'s gone, it\'s gone.'],
             facts=[['10K','followers'],['48 hrs','free exchange'],['Mon–Sat','in store']]),
  infoTitle='Visit or order online', info=[['🕘','Opening hours','Monday to Friday 9am to 7pm, Saturday 9am to 5pm.'],['📞','Customer care','+234 805 842 4788, on call and WhatsApp.'],['🚚','Nationwide delivery','Lagos in 24–48 hours, the rest of Nigeria in 2 to 5 days.'],['🔁','Free exchange','Exchange within 48 hours. No refunds.']],
  insta=[5,0,1,2,3,4], followers='10K', instaTitle='As worn on @eyangalagos',
  cta=['Just landed','Your next statement piece is here.','Shop the edit','shop'],
  sections=['hero','shop','story','info','insta','bigcta'],
  delivery=NG_DELIVERY, pay=NG_PAY, payNote='Secure payment by Paystack.', orderPrefix='EYG',
  doneNote='Customer care will confirm delivery on WhatsApp within the hour.', wa='https://wa.me/2348058424788',
  footer='Fashion luxury store, Lagos · Mon–Fri 9am–7pm, Sat 9am–5pm · +234 805 842 4788',
)

SITES['zarakhan-boutique'] = dict(
  handle='zarakhan_boutique', name='Zarakhan Boutique', logo='Zarakhan<small>Boutique</small>', cur='GBP', mode='shop', og=3,
  title='Zarakhan Boutique Birmingham | Asian bridal, party & festive wear',
  desc='Asian bridal, party and festive wear from Zarakhan Boutique, Birmingham. Shop online, click and collect, or visit the store.',
  fonts='family=Playfair+Display:ital,wght@0,500;0,700;1,500&family=Poppins:wght@400;500;600',
  vars=dict(bg='#FFF5F7', ink='#2B1420', muted='#7E5F6C', line='#F0D9E0', soft='#FBE8EE', card='#FFFFFF', accent='#B0306A', accent2='#E2B25A', **{'on-accent':'#fff'},
            display="'Playfair Display',Georgia,serif", body="'Poppins',system-ui,sans-serif", ir='20px', dw='500'),
  nav=[['Shop','shop'],['Weekend sale','sale'],['Visit','visit']],
  hero=dict(eyebrow='Birmingham · Worldwide shipping', title='Dressed for the moments *everyone* remembers.', lede='Bridal, party and festive wear, hand-embellished and ready to shop. Order online, collect in store, or have it shipped anywhere.',
            cta=['Shop the collection','shop'], cta2=['See the weekend sale','sale'], badges=['<b>125K</b> on Instagram','Click & collect','Worldwide shipping'], pics=[3,1,0,2], stamp=['125K','followers, and now a website']),
  ticker=['Bridal','Party wear','Eid & festive','Menswear','Click & collect in Birmingham','Worldwide shipping'],
  shopTitle='Hand-<em>embellished</em> & ready to wear', products=[
    dict(name='Noor Embroidered Anarkali', cat='Party wear', img=1, price=165, tag='New', desc='Black net anarkali with dense gold embroidery and a matching dupatta.'),
    dict(name='Mauve Mirrorwork Suit', cat='Bridal', img=3, price=245, tag='Bestseller', hot=True, desc='Rose-mauve with mirrorwork and sequins, for the mehndi or the walima.'),
    dict(name='Ivory Sherwani & Lehenga', cat='Menswear', img=0, price=320, desc='A coordinated pairing for couples: ivory sherwani with a sage lehenga.'),
    dict(name='Festive Kurta Pairing', cat='Menswear', img=2, price=95, desc='Rich colour, clean lines and a matching shawl.'),
    dict(name='Lilac Party Suits', cat='Party wear', img=9, price=45, was=85, tag='Sale', hot=True, desc='Our weekend sale favourite. Three-piece lilac suits in mixed embellishments.'),
  ],
  defaultOpts=[['Size',['XS','S','M','L','XL','Custom']]],
  quickNote='Need alterations? Our team can adjust fit in store in Birmingham.',
  banner=[7,'This weekend only','Weekend sale. Selected suits now from £45.','shop','Shop the sale'],
  story=dict(pics=[0,3], eyebrow='Our store', title='Come and see it in person', body=['Zarakhan Boutique brings bridal, party and festive wear to Birmingham, with new pieces arriving every week.','Try on in store, or shop online and choose click & collect.'],
             facts=[['125K','Instagram followers'],['🇬🇧','UK & worldwide'],['Weekly','new arrivals']]),
  infoTitle='Visit, collect or ship', info=[['🏬','Visit the shop','Call the store on 0121 328 7080.'],['📦','Click & collect','Order online and pick up in Birmingham, usually the next day.'],['🌍','Worldwide shipping','Tracked UK delivery in 2–3 days and international shipping.'],['💬','Orders & enquiries','WhatsApp +44 7399 143394.']],
  insta=[1,3,0,2,7,9], followers='125K', instaTitle='New in on Instagram',
  cta=['Eid, weddings, parties','Find the outfit before the invite lands.','Shop now','shop'],
  sections=['hero','shop','banner','story','info','insta','bigcta'],
  delivery=[['Click & collect in Birmingham',0],['UK tracked (2–3 days)',4.99],['UK next day',8.99],['International tracked',19.99]], pay=UK_PAY,
  payNote='Secure checkout by Stripe.', orderPrefix='ZK', doneNote='We\'ll email you when your order is ready to collect or on its way.', wa='https://wa.me/447399143394',
  footer='Zarakhan Boutique, Birmingham · Shop 0121 328 7080 · WhatsApp +44 7399 143394',
)

SITES['tinus-place'] = dict(
  handle='tinusplace', name='Tinu\'s Place', logo='TINUSPLACE<small>Luxury hair</small>', cur='NGN', mode='shop', og=5,
  title='Tinusplace | Luxury hair vendor, Lagos',
  desc='Luxury wigs, frontals and bundles from Tinusplace. Choose your length and lace, pay online and get it delivered.',
  fonts='family=Syne:wght@600;700;800&family=Inter:wght@400;500;600;700',
  vars=dict(bg='#FFF6FA', ink='#160A10', muted='#7B5D6A', line='#F4D7E4', soft='#FDE7F1', card='#FFFFFF', accent='#E6007E', accent2='#FFB800', **{'on-accent':'#fff'},
            display="'Syne',system-ui,sans-serif", body="'Inter',system-ui,sans-serif", **{'hero-bg':'#160A10','hero-ink':'#FFF6FA'}, ir='24px', dw='800', dls='-.03em'),
  nav=[['Shop hair','shop'],['Our studio','story'],['Delivery','visit']],
  hero=dict(eyebrow='#1 trusted luxury hair vendor', title='Hair that walks in *before* you do.', lede='Luxury wigs and frontals, customised to your length and lace. Pick, pay and have it delivered, with no back-and-forth in the DMs.',
            cta=['Shop hair','shop'], cta2=['Visit the studio','story'], badges=['<b>79K</b> on Instagram','Exhibitor, Beauty in the Motherland 2026','Ships worldwide'], pics=[9,5,8,11], stamp=['79K','queens and counting']),
  ticker=['Luxury wigs','Frontals & closures','Custom colour','Wig installs','Exhibiting at Beauty in the Motherland 2026'],
  shopTitle='Pick your <em>hair</em>', quickLabel='Customise', products=[
    dict(name='Honey Balayage Body Wave', cat='Coloured', img=5, price=380000, tag='Bestseller', hot=True, desc='Rich espresso roots melting into honey highlights with a full, bouncy body wave.'),
    dict(name='Chestnut Layered Frontal', cat='Frontals', img=6, price=320000, desc='Soft face-framing layers in warm chestnut on a melted HD lace.'),
    dict(name='Espresso Blunt Bob', cat='Bobs', img=7, price=180000, tag='New', desc='Sleek, blunt and low-maintenance. Pre-plucked and ready to wear.'),
    dict(name='Onyx Body Wave', cat='Frontals', img=8, price=350000, desc='Jet-black body wave with natural movement and a pre-plucked hairline.'),
    dict(name='Toffee Highlight Layers', cat='Coloured', img=9, price=360000, desc='Dark base with toffee highlights and voluminous layers.'),
    dict(name='Midnight Deep Wave', cat='Frontals', img=11, price=340000, desc='Glossy midnight waves with plenty of volume.'),
  ],
  defaultOpts=[['Length',['14"','18"','22"','26"'],[0,45000,95000,150000]],['Lace',['5x5 closure','13x4 frontal','13x6 HD frontal'],[0,40000,85000]],['Density',['180%','250%'],[0,60000]]],
  quickNote='Free bleached knots and pre-plucking on every unit. Installs available in our Lagos studio.',
  story=dict(pics=[4,10], eyebrow='The studio', title='Walk in, try on, walk out glowing', body=['Tinusplace is a luxury hair brand from Lagos, trusted by thousands of women who want hair that looks expensive and lasts.','Visit our studio to try units on, book an install, or shop online and have it delivered anywhere.'],
             facts=[['79K','followers'],['2026','Beauty in the Motherland exhibitor'],['🌍','worldwide delivery']]),
  infoTitle='Delivery & care', info=[['🚚','Lagos in 24 hours','Fast dispatch across Lagos, 2 to 5 days nationwide.'],['🌍','Worldwide','Tracked shipping to the UK, US and Canada.'],['💇🏾‍♀️','Installs & revamps','Book an install or a revamp in our studio.'],['💳','Pay your way','Card, transfer or USSD with Paystack.']],
  insta=[9,5,11,8,4,0], followers='79K', instaTitle='Real queens, real hair',
  cta=['Your next unit','Less time in the DMs. More compliments.','Shop hair','shop'],
  sections=['hero','shop','story','info','insta','bigcta'],
  delivery=NG_DELIVERY, pay=NG_PAY, payNote='Secure payment by Paystack.', orderPrefix='TP',
  doneNote='Your unit is being customised. We\'ll WhatsApp you before it ships.', wa='https://wa.me/message/DJD6BMJBRSOGB1',
  footer='Tinusplace luxury hair · Lagos, Nigeria',
)

SITES['charm-nails-spa'] = dict(
  handle='charmnailsspa_kingstanding', name='Charm Nails Spa', logo='Charm<small>Nails Spa</small>', cur='GBP', mode='book', og=4,
  title='Charm Nails Spa Kingstanding | Award-winning nails, book online',
  desc='Award-winning nail salon in Kingstanding, Birmingham. Acrylics, gel, BIAB and mani-pedis. Book online in seconds.',
  fonts='family=Marcellus&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700',
  vars=dict(bg='#FFF8F4', ink='#2A1A1F', muted='#7D6468', line='#F1DDD8', soft='#FCEBE6', card='#FFFFFF', accent='#C9466E', accent2='#E9B949', **{'on-accent':'#fff'},
            display="'Marcellus',Georgia,serif", body="'Nunito Sans',system-ui,sans-serif", ir='22px', dw='400'),
  nav=[['Treatments','book'],['Awards','awards'],['Our work','gallery']], headerCta=['Book now','book'],
  hero=dict(eyebrow='Kingstanding · Birmingham', title='Award-winning nails, *booked* in seconds.', lede='Acrylics, gel, BIAB and mani-pedis by a friendly, award-winning team. Choose your treatment and time, and you\'re in.',
            cta=['Book a treatment','book'], cta2=['See our work','gallery'], badges=['<b>18K</b> on Instagram','International award winners','High-quality products only'], pics=[4,5,0,6], stamp=['🏆','Award-winning team']),
  ticker=['Acrylic','Gel','BIAB','Manicure & pedicure','Nail art','Award-winning team'],
  bookTitle='Treat yourself', services=[
    dict(name='Acrylic full set', desc='Any length and shape, finished with gel colour.', mins=75, price=35),
    dict(name='BIAB overlay', desc='Builder gel on natural nails for strength and shine.', mins=60, price=32),
    dict(name='Gel polish, hands', desc='File, shape, cuticle care and long-wear gel colour.', mins=45, price=25),
    dict(name='Spa mani-pedi', desc='Soak, scrub, massage and polish for hands and feet.', mins=90, price=45),
    dict(name='Infills', desc='Keep your acrylic or BIAB set looking fresh.', mins=60, price=28),
    dict(name='Nail art add-on', desc='Chrome, French, 3D flowers or charms.', mins=15, price=8),
  ],
  closedDays=[], hours=[9,19], deposit=5, depositNote='A £5 deposit secures your slot and comes off your bill. Free changes up to 24 hours before.',
  awards=['Recognised internationally','Our trophy wall', [0,1,2]],
  gallery=['Fresh from the studio','Our work', [[4,'Gold chrome'],[5,'Floral art'],[6,'Autumn set']]],
  infoTitle='Good to know', info=[['📍','Kingstanding, Birmingham','Easy to reach, with friendly staff and walk-ins when there\'s space.'],['🏆','Award-winning','Our team has won international awards, and we always use high-quality products.'],['🗓️','Book online 24/7','No more waiting for a DM reply. Pick a time and it\'s confirmed.'],['💳','Pay how you like','Card, Apple Pay or cash in the salon.']],
  insta=[4,5,6,0,1,2], followers='18K', instaTitle='Fresh sets daily',
  cta=['Your next set','Nails this good deserve a proper booking page.','Book now','book'],
  sections=['hero','booking','awards','gallery','info','insta','bigcta'], footer='Charm Nails Spa, Kingstanding, Birmingham',
)

CAKE_FLAV_LUX = [['Vanilla bean','#FBF4E8','#F3E3C6'],['Red velvet','#FFF5F3','#C8303E'],['Chocolate fudge','#F2E6DA','#5A3221'],['Lemon & elderflower','#FFFBE6','#F2D75C'],['Pistachio & rose','#F4F8EC','#E8A9B6']]
SITES['luxxe-cakes'] = dict(
  handle='luxxecakes', name='Luxxe Cakes', logo='Luxxe<small>Cakes</small>', cur='GBP', mode='cake', og=0,
  title='Luxxe Cakes London | Luxury wedding cakes, eggless & egg',
  desc='Luxury wedding and celebration cakes in London, eggless or with egg. Design your cake online and request a quote.',
  fonts='family=Cormorant:ital,wght@0,500;0,600;1,500&family=Jost:wght@400;500;600',
  vars=dict(bg='#FBF8F3', ink='#1D1B24', muted='#77707A', line='#EAE3D9', soft='#F4EEE5', card='#FFFFFF', accent='#B08655', accent2='#E9C2C5', **{'on-accent':'#fff'},
            display="'Cormorant',Georgia,serif", body="'Jost',system-ui,sans-serif", **{'hero-bg':'#151826','hero-ink':'#FBF8F3'}, ir='6px', dw='500'),
  nav=[['Design a cake','design'],['Gallery','gallery'],['Enquire','visit']], headerCta=['Design your cake','design'],
  hero=dict(eyebrow='London · Eggless & egg', title='Cakes they\'ll talk about after the *last* dance.', lede='Statement wedding and celebration cakes designed around your day, made eggless or with egg.',
            cta=['Design your cake','design'], cta2=['See the gallery','gallery'], badges=['<b>6.4K</b> on Instagram','Eggless or with egg','London-wide delivery & set-up'], pics=[0,2,4,5], stamp=['Eggless','or with egg, always luxe']),
  ticker=['Wedding cakes','Engagements','Birthdays','Eggless & egg','Delivery and set-up across London'],
  cakeTitle='Build it, *love* it', occasions=[['Wedding','💍'],['Engagement','💐'],['Birthday','🎂'],['Celebration','🥂']], flavours=CAKE_FLAV_LUX, maxTiers=6, minDays=21,
  cakeNote='Final price depends on design, sugar flowers and delivery. We\'ll confirm within 24 hours.', cakeDone='We\'ll send a personalised quote and design sketch within 24 hours.',
  serves_js='t=>[0,20,50,90,140,200,270][t]', price_js='(t,o)=>[0,180,340,520,720,940,1180][t]+(o===0?120:0)',
  gallery=['Recent work','Made for the big day', [[0,'Cascading florals'],[1,'Six-tier white'],[2,'Under the lights'],[3,'Roses & gold'],[5,'Ballroom moment'],[4,'Just married']]],
  infoTitle='How it works', info=[['✏️','1. Design online','Choose tiers, flavours and eggless or egg, and get an instant estimate.'],['📞','2. Consultation','We\'ll call to perfect the design, colours and finishing touches.'],['🚐','3. Delivered & set up','We deliver and set up across London, so you don\'t have to worry.'],['🥚','Eggless specialists','Every flavour is available eggless, with no compromise on taste.']],
  insta=[0,1,2,3,4,5], followers='6.4K', instaTitle='Fresh from the studio',
  cta=['Booking now for next season','Let\'s make the cake of the night.','Design your cake','design'],
  sections=['hero','cake','gallery','info','insta','bigcta'], footer='Luxxe Cakes, London · Eggless and egg wedding cakes',
)

CAKE_FLAV_CB = [['Vanilla','#FFF7EC','#F7C8D8'],['Chocolate','#F1E2D6','#6B3A26'],['Red velvet','#FFF3F3','#D0334B'],['Butterscotch','#FFF4DF','#E0A13A'],['Rasmalai','#FFF9EC','#E5C46A'],['Mango','#FFF6DE','#F5B21B']]
SITES['cakes-and-bakes-barkingside'] = dict(
  handle='cakes_and_bakes.barkingside', name='Cakes & Bakes', logo='Cakes &amp; Bakes<small>Barkingside</small>', cur='GBP', mode='cake', og=8,
  title='Cakes & Bakes Barkingside | Eggless celebration cakes since 2010',
  desc='Eggless celebration cakes in Barkingside, Ilford since 2010. Birthday, wedding and corporate cakes, 5-star food hygiene. Design and order online.',
  fonts='family=Fredoka:wght@500;600;700&family=Nunito:wght@400;600;700',
  vars=dict(bg='#FFF9F2', ink='#2B2030', muted='#7B6C7E', line='#F2E2D6', soft='#FFEFE6', card='#FFFFFF', accent='#E2457A', accent2='#35B5C9', **{'on-accent':'#fff'},
            display="'Fredoka',system-ui,sans-serif", body="'Nunito',system-ui,sans-serif", ir='26px', dw='600', dls='-.01em'),
  nav=[['Design a cake','design'],['Gallery','gallery'],['Find us','visit']], headerCta=['Order a cake','design'],
  hero=dict(eyebrow='Barkingside, Ilford · Since 2010', title='A little chocolate, a *lot* of happiness.', lede='Eggless celebration cakes for birthdays, weddings and every party in between. Design yours online and we\'ll bake it fresh.',
            cta=['Design your cake','design'], cta2=['See our cakes','gallery'], badges=['<b>100%</b> eggless','5★ food hygiene','Since 2010'], pics=[8,9,5,10], stamp=['5★','food hygiene rating']),
  ticker=['Birthdays','Weddings','Corporate events','100% eggless','5★ food hygiene','59 High Street, Barkingside'],
  cakeTitle='Design it in 30 seconds', occasions=[['Birthday','🎈'],['Wedding','💍'],['Corporate','🏢'],['Halloween','🎃']], flavours=CAKE_FLAV_CB, maxTiers=4, minDays=3,
  cakeNote='Most celebration cakes need 3 days\' notice. Wedding cakes need 4 weeks.', cakeDone='We\'ll WhatsApp you within a few hours to confirm the design and price.',
  serves_js='t=>[0,12,30,60,100][t]', price_js='(t,o)=>[0,45,95,180,290][t]+(o===1?80:0)',
  banner=[3,'This month','Halloween theme cakes are here. Order by 31 October.','design','Design a spooky cake'],
  gallery=['Fresh from the oven','Cakes we\'ve loved making', [[8,'Chocolate drip'],[9,'Under the sea'],[5,'Scales of justice'],[6,'Ocean ombré'],[10,'Pink crown'],[3,'Halloween']]],
  infoTitle='Come and see us', info=[['📍','59 High Street, Barkingside','Ilford, Essex IG6 2AD. Pop in to see what\'s fresh.'],['🥚','Eggless since 2010','Every cake is eggless, so everyone can have a slice.'],['⭐','5★ food hygiene','Rated 5 for food hygiene, and proud of it.'],['🚗','Collection or delivery','Collect in store or ask about local delivery.']],
  insta=[8,9,5,6,10,3], followers='4.1K', instaTitle='Baked with love',
  cta=['Party coming up?','Let\'s make it a sweet one.','Order a cake','design'],
  sections=['hero','cake','banner','gallery','info','insta','bigcta'], footer='Cakes &amp; Bakes, 59 High Street, Barkingside, Ilford IG6 2AD',
)

for slug, s in SITES.items():
    D = {k: v for k, v in s.items() if k not in ('vars','fonts','title','desc','og','serves_js','price_js')}
    D.setdefault('shopEyebrow', 'Shop online')
    if s['mode'] != 'shop':
        D.setdefault('products', [])
    D.setdefault('closedDays', []); D.setdefault('hours', [9, 18]); D.setdefault('minDays', 1)
    D.setdefault('headerCta', ['Shop', 'shop'])
    data = json.dumps(D, ensure_ascii=False)
    if 'serves_js' in s:
        data = data[:-1] + ',"serves":' + s['serves_js'] + ',"priceFn":' + s['price_js'] + '}'
    else:
        data = data[:-1] + ',"serves":t=>0,"priceFn":()=>0}'
    jsonld = {"@context": "https://schema.org", "@type": "Store" if s['mode'] == 'shop' else ("NailSalon" if s['mode'] == 'book' else "Bakery"),
              "name": s['name'], "description": s['desc'], "sameAs": [f"https://www.instagram.com/{s['handle']}/"], "image": f"img/{s['og']}.jpg"}
    html = (T.replace('__TITLE__', s['title'].replace('&', '&amp;')).replace('__DESC__', s['desc'])
             .replace('__OG__', str(s['og'])).replace('__FONTS__', s['fonts']).replace('__VARS__', vars_(s['vars']))
             .replace('__EXTRA_CSS__', s.get('css', '')).replace('__HANDLE__', s['handle']).replace('__LOGO__', s['logo'])
             .replace('__JSONLD__', json.dumps(jsonld, ensure_ascii=False)).replace('__DATA__', data))
    os.makedirs(os.path.join(OUT, slug), exist_ok=True)
    open(os.path.join(OUT, slug, 'index.html'), 'w').write(html)
    print('wrote', slug)
