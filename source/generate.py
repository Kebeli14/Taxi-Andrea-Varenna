from pathlib import Path
from html import escape
import json
from urllib.parse import quote

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'site'
COMMONS='https://commons.wikimedia.org/wiki/Special:FilePath/'
PHOTOS={
 'hero': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Varenna_20260811.jpg/1920px-Varenna_20260811.jpg',
 'lake': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Varenna_Shore.jpg/1600px-Varenna_Shore.jpg',
 'detail': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Varenna_-_View_from_Lake_Como.jpg/1280px-Varenna_-_View_from_Lake_Como.jpg',
 'water': COMMONS+'Sunset_lake_como_varenna_Italy.jpg?width=1100',
 'wide': COMMONS+'Lake_Como_Varenna_Italy.jpg?width=1500',
 'van': 'https://static.wixstatic.com/media/40c53e_7887b3f54f5c45328dfe3556a15a6b6f~mv2.jpg',
 'van2':'https://static.wixstatic.com/media/40c53e_2dea5a7e27a0449f9e60c2363069d599~mv2.jpeg',
}

CONTENT={
 'it':{
  'lang':'it','home':'Home','services':'Servizi','vehicle':'Il mezzo','contacts':'Contatti','navcta':'Richiedi un transfer',
  'brand_sub':'VARENNA · LAGO DI COMO','eyebrow':'TAXI & TRANSFER PRIVATI · VARENNA',
  'hero1':'Il lago davanti.', 'hero2':'La strada, a noi.','hero_p':'Da Varenna agli aeroporti, tra i borghi del Lago di Como e verso le Alpi. Un servizio diretto, attento e organizzato intorno al tuo viaggio.',
  'quote':'Richiedi un preventivo','explore':'Esplora i servizi','hero_ref':'VAR. / 46°00′ N, 9°17′ E','hero_photo':'Varenna, sul Lago di Como',
  'micro1':'Partenze da Varenna','micro2':'Transfer privati su richiesta','micro3':'Assistenza anche in inglese',
  'intro_k':'IL VIAGGIO COMINCIA QUI','intro_h':'Quando arrivi sul lago, il resto dovrebbe essere semplice.','intro_p':'Una stazione, un aeroporto, un hotel, una giornata da organizzare. Taxi Andrea Varenna ti accompagna con un servizio di trasporto pensato sulle tue esigenze, senza giri inutili e con un contatto diretto.',
  'service_label':'COSA FACCIAMO','service_h':'Ogni destinazione ha il suo percorso.','service_sub':'Per una corsa breve o un itinerario di più giorni, raccontaci cosa ti serve.','allservices':'Tutti i servizi',
  's1':'Aeroporti','s1p':'Collegamenti con Malpensa, Linate e Bergamo Orio al Serio.','s1small':'01 / ARRIVI E PARTENZE',
  's2':'Stazioni ferroviarie','s2p':'Partenze e arrivi dalle stazioni di Milano, Como e Lecco.','s2small':'02 / COLLEGAMENTI',
  's3':'Lago di Como','s3p':'Trasferimenti tra Varenna, Bellagio, Menaggio e le località del lago.','s3small':'03 / TERRITORIO',
  's4':'Montagna e Svizzera','s4p':'Viaggi verso Bormio, Livigno, St. Moritz e altre destinazioni.','s4small':'04 / LUNGA PERCORRENZA',
  'photo_label':'VARENNA · LAGO DI COMO','photo_title':'Conosciamo il valore del tempo, e quello dei luoghi.','photo_link':'Scopri i trasferimenti',
  'vehicle_label':'IL NOSTRO MEZZO','vehicle_h':'Lo spazio giusto per viaggiare insieme.','vehicle_p':'Un van Hyundai a 8 posti, adatto a trasferimenti privati, famiglie e piccoli gruppi. Comunica in anticipo persone e bagagli: ti confermeremo la soluzione più adatta.',
  'vehicle_link':'Scopri il mezzo','local_label':'UN SERVIZIO LOCALE','local_h':'Qui il lago non è una cartolina. È casa.','local_p':'Un riferimento a Varenna per accompagnarti nei tuoi spostamenti, con attenzione agli orari, ai punti di incontro e a ogni dettaglio pratico.',
  'request_k':'ORGANIZZIAMO IL TUO VIAGGIO','request_h':'Da dove partiamo?','request_p':'Scrivici dove, quando e con quante persone vuoi viaggiare. Ti risponderemo per confermare disponibilità e condizioni.',
  'form_name':'Nome e cognome','form_email':'Indirizzo email','form_tel':'Telefono (facoltativo)','form_from':'Partenza','form_to':'Destinazione','form_date':'Data del viaggio','form_time':'Orario indicativo','form_people':'Passeggeri','form_luggage':'Bagagli (facoltativo)','form_notes':'Informazioni utili','placeholder_from':'Es. Aeroporto di Malpensa','placeholder_to':'Es. Varenna, hotel...','placeholder_notes':'Numero di valigie, volo, fermate, richieste particolari...',
  'mailcta':'Prepara email di richiesta','wacta':'Prepara messaggio WhatsApp','privacy_l':'Ho preso visione dell’informativa privacy','form_notice':'Il modulo prepara un messaggio sul tuo dispositivo: non effettua una prenotazione né invia dati a un server del sito.','form_validation':'Compila i campi obbligatori e accetta l’informativa privacy.',
  'address':'Via Polvani 1, Varenna (LC)','email_l':'Email','tel_l':'Telefono','find_us':'Ci trovi a Varenna','foot_title':'Il prossimo viaggio può cominciare da qui.','foot_small':'Servizio su richiesta. Preventivi e disponibilità da confermare.',
  'ser_eyebrow':'SERVIZI · TAXI ANDREA VARENNA','ser_h':'Un luogo alla volta. Nessuna fretta inutile.','ser_p':'Dagli aeroporti lombardi alle strade intorno al lago, progettiamo il trasferimento in base alla tua destinazione e ai tuoi orari.',
  'ser_block_1':'Arrivare è la parte più bella.','ser_block_1p':'Transfer da e verso gli aeroporti di Malpensa, Milano Linate e Bergamo Orio al Serio, con destinazione Varenna e le località del territorio.',
  'ser_block_2':'Dal treno direttamente a destinazione.','ser_block_2p':'Collegamenti dalle stazioni di Milano, Como e Lecco. Specifica la stazione esatta e l’orario del treno per concordare il punto d’incontro.',
  'ser_block_3':'Una giornata disegnata intorno a te.','ser_block_3p':'Tour e spostamenti su misura tra Varenna, Bellagio, Menaggio e i borghi del lago. Itinerario e soste vengono concordati in anticipo.',
  'ser_block_4':'Anche oltre il lago.','ser_block_4p':'Trasferimenti verso le località alpine e oltreconfine, tra cui Bormio, Livigno e St. Moritz. Inviaci la destinazione per un preventivo personalizzato.',
  'ser_note':'Le tratte e gli orari indicati sono esempi di servizio. Costi e disponibilità vengono comunicati dopo la richiesta.',
  'veh_eyebrow':'IL MEZZO · TAXI ANDREA VARENNA','veh_title':'Viaggiare comodi, insieme.','veh_desc':'Il nostro servizio utilizza un van Hyundai a 8 posti, pensato per chi cerca spazio e praticità durante il trasferimento.',
  'veh_fact1':'Van Hyundai','veh_fact2':'8 posti dichiarati','veh_fact3':'Trasferimenti su richiesta','veh_story_h':'Un veicolo per la strada, non per la vetrina.','veh_story_p':'Aeroporti, stazioni, piccoli gruppi e itinerari più lunghi: il veicolo è parte di un servizio costruito attorno ai tuoi spostamenti. Per gruppi numerosi o bagagli ingombranti, verifica sempre la capienza effettiva al momento della richiesta.',
  'veh_photo_note':'Fotografie del veicolo di riferimento dal sito esistente; verificare che corrispondano al mezzo attualmente in servizio prima della pubblicazione.',
  'cont_eyebrow':'CONTATTI · VARENNA','cont_h':'Dimmi dove devi andare.','cont_p':'Un breve messaggio basta per iniziare. Indicaci partenza, destinazione, data e numero di persone: ti risponderemo per concordare il trasferimento.',
  'form_heading':'Richiesta di transfer','address_heading':'Un contatto diretto, senza intermediari.','address_p':'Puoi anche chiamarci o scrivere direttamente. Per le richieste con anticipo, l’email è un modo semplice per includere tutti i dettagli.',
  'route_title':'Come funziona','step1':'Ci invii i dettagli del viaggio.','step2':'Verifichiamo disponibilità e percorso.','step3':'Concordiamo le condizioni e il punto di incontro.',
  'notconfirmed':'Una richiesta non equivale a una prenotazione confermata.',
  'credit_label':'Crediti fotografici',
 },
 'en':{
  'lang':'en','home':'Home','services':'Services','vehicle':'The vehicle','contacts':'Contact','navcta':'Request a transfer',
  'brand_sub':'VARENNA · LAKE COMO','eyebrow':'TAXI & PRIVATE TRANSFERS · VARENNA',
  'hero1':'The lake ahead.', 'hero2':'The road is ours.','hero_p':'From Varenna to the airports, across Lake Como and into the Alps. Personal transfers shaped around your journey.',
  'quote':'Request a quote','explore':'Explore our services','hero_ref':'VAR. / 46°00′ N, 9°17′ E','hero_photo':'Varenna, Lake Como',
  'micro1':'Based in Varenna','micro2':'Private transfers on request','micro3':'English-speaking service',
  'intro_k':'YOUR JOURNEY STARTS HERE','intro_h':'When you reach the lake, the rest should feel simple.','intro_p':'A railway station, an airport, a hotel, a day out. Taxi Andrea Varenna offers straightforward transport, attentive service and direct communication for your journey.',
  'service_label':'WHAT WE DO','service_h':'Every destination has its own way there.','service_sub':'A short journey or a longer route: tell us what you need.','allservices':'All services',
  's1':'Airports','s1p':'Transfers to and from Malpensa, Linate and Bergamo Orio al Serio.','s1small':'01 / ARRIVALS & DEPARTURES',
  's2':'Train stations','s2p':'Connections from railway stations in Milan, Como and Lecco.','s2small':'02 / RAIL CONNECTIONS',
  's3':'Lake Como','s3p':'Transfers around Varenna, Bellagio, Menaggio and lakeside towns.','s3small':'03 / LAKESIDE ROUTES',
  's4':'Mountains & Switzerland','s4p':'Journeys to Bormio, Livigno, St. Moritz and other destinations.','s4small':'04 / LONG DISTANCE',
  'photo_label':'VARENNA · LAKE COMO','photo_title':'We value your time, and the places you came to see.','photo_link':'Explore transfers',
  'vehicle_label':'OUR VEHICLE','vehicle_h':'Room to travel together.','vehicle_p':'An 8-seat Hyundai van for private transfers, families and small groups. Let us know passenger and luggage requirements so we can confirm the right solution.',
  'vehicle_link':'Discover the vehicle','local_label':'A LOCAL SERVICE','local_h':'Here, the lake is more than a postcard. It is home.','local_p':'A local contact in Varenna to help with practical arrangements, meeting points and travel timing.',
  'request_k':'LET’S PLAN YOUR JOURNEY','request_h':'Where shall we start?','request_p':'Tell us where and when you need to travel and how many people are coming. We will reply with availability and terms.',
  'form_name':'Full name','form_email':'Email address','form_tel':'Phone (optional)','form_from':'Pick-up location','form_to':'Destination','form_date':'Travel date','form_time':'Approximate time','form_people':'Passengers','form_luggage':'Luggage (optional)','form_notes':'Additional details','placeholder_from':'e.g. Malpensa Airport','placeholder_to':'e.g. Varenna, hotel...','placeholder_notes':'Suitcases, flight number, extra stops, special requests...',
  'mailcta':'Prepare email request','wacta':'Prepare WhatsApp message','privacy_l':'I have read the privacy notice','form_notice':'This form prepares a message on your device. It does not confirm a booking or transmit data to this website’s servers.','form_validation':'Complete all required fields and accept the privacy notice.',
  'address':'Via Polvani 1, Varenna (LC), Italy','email_l':'Email','tel_l':'Phone','find_us':'Based in Varenna','foot_title':'Your next journey starts here.','foot_small':'Service on request. Prices and availability subject to confirmation.',
  'ser_eyebrow':'SERVICES · TAXI ANDREA VARENNA','ser_h':'One destination at a time. No unnecessary rush.','ser_p':'From Lombardy airports to lakeside roads, we arrange transfers around your destination and schedule.',
  'ser_block_1':'Arriving should be the easy part.','ser_block_1p':'Travel to or from Malpensa, Milan Linate and Bergamo Orio al Serio airports, with connections to Varenna and Lake Como.',
  'ser_block_2':'From your train straight to your destination.','ser_block_2p':'Transfers from stations in Milan, Como and Lecco. Share your station and train arrival time so we can arrange the meeting point.',
  'ser_block_3':'A day shaped around you.','ser_block_3p':'Customised trips and tours through Varenna, Bellagio, Menaggio and other lakeside villages. Stops and itinerary are agreed in advance.',
  'ser_block_4':'Beyond the lake, too.','ser_block_4p':'Transfers to Alpine and cross-border destinations including Bormio, Livigno and St. Moritz. Contact us for a personalised quote.',
  'ser_note':'Routes and times listed are examples of services. Prices and availability are shared in response to your enquiry.',
  'veh_eyebrow':'THE VEHICLE · TAXI ANDREA VARENNA','veh_title':'A comfortable way to travel together.','veh_desc':'Our service uses an 8-seat Hyundai van, selected for its space and practicality during transfers.',
  'veh_fact1':'Hyundai van','veh_fact2':'8 seats stated','veh_fact3':'Transfers on request','veh_story_h':'Made for the road, not the showroom.','veh_story_p':'Airports, stations, groups and longer journeys: the vehicle supports a service adapted to the way you travel. For large groups or bulky luggage, please confirm actual passenger capacity before booking.',
  'veh_photo_note':'Reference vehicle images are sourced from the existing website; please verify that they depict the vehicle currently in service before publishing.',
  'cont_eyebrow':'CONTACT · VARENNA','cont_h':'Tell us where you need to go.','cont_p':'A short message is enough. Send your departure point, destination, date and group size so we can discuss your transfer.',
  'form_heading':'Transfer enquiry','address_heading':'Direct contact. No middlemen.','address_p':'You can call or email us directly. An email is particularly useful for sharing travel details in advance.',
  'route_title':'How it works','step1':'You share your trip details.','step2':'We check the route and availability.','step3':'We agree on the terms and meeting point.',
  'notconfirmed':'An enquiry is not a confirmed booking.',
  'credit_label':'Photo credits',
 }
}
VAT='04141980138'  # Italian VAT 11 digits; original site's footer includes an extraneous digit.
PHONE='+39 377 095 9389'
PHONE_RAW='+393770959389'
EMAIL='taxi.andrea.varenna@gmail.com'
PRIVACY='https://www.iubenda.com/privacy-policy/27574385'


def pic(name,cl='',alt='',loading='lazy'):
 return f'<img class="{cl}" src="{escape(PHOTOS[name],quote=True)}" alt="{escape(alt,quote=True)}" loading="{loading}" decoding="async" referrerpolicy="no-referrer">'

def arrow():return '<svg aria-hidden="true" viewBox="0 0 20 20" fill="none"><path d="M3 10h13m-5-5 5 5-5 5" stroke="currentColor" stroke-width="1.4"/></svg>'

def header(t,lang,page):
    links=[('home',''),('services','servizi/' if lang=='it' else 'services/'),('vehicle','mezzi/' if lang=='it' else 'vehicle/'),('contacts','contatti/' if lang=='it' else 'contact/')]
    nav=''.join(f'<a class="{"is-active" if page==k else ""}" href="/{lang}/{suffix}">{t[k]}</a>' for k,suffix in links)
    alternate='en' if lang=='it' else 'it'
    same={'home':'','services':'servizi/' if alternate=='it' else 'services/','vehicle':'mezzi/' if alternate=='it' else 'vehicle/','contacts':'contatti/' if alternate=='it' else 'contact/'}[page]
    return f'''<div class="top-note"><div class="top-note-inner"><span>{'TAXI & TRANSFER PRIVATI · LAGO DI COMO' if lang=='it' else 'TAXI & PRIVATE TRANSFERS · LAKE COMO'}</span><span>{'BASE A VARENNA · ITALIA' if lang=='it' else 'BASED IN VARENNA · ITALY'}</span></div></div><header class="site-header" id="top"><div class="header-shell">
      <a class="brand" href="/{lang}/" aria-label="Taxi Andrea Varenna — {t['home']}"><span class="brand-sign" aria-hidden="true"><svg viewBox="0 0 80 29"><path d="M2 25 24 7 37 17 48 3 78 25"/><path d="M3 28h74"/></svg></span><span class="brand-main">TAXI ANDREA<small>VARENNA</small></span></a>
      <nav class="desktop-nav" aria-label="Main navigation">{nav}</nav>
      <div class="header-actions"><a class="lang" href="/{alternate}/{same}" hreflang="{alternate}" aria-label="{'English' if alternate=='en' else 'Italiano'}">{alternate.upper()}</a><a class="header-call" href="tel:{PHONE_RAW}" aria-label="{t['tel_l']}: {PHONE}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h4l1.2 5-2.4 1.8a17 17 0 0 0 5.4 5.4l1.8-2.4 5 1.2v4c0 1.4-1 2.2-2.4 2.1A18 18 0 0 1 3.9 5.4C3.8 4 4.6 3 6 3Z"/></svg><span>{PHONE}</span></a><button class="menu-toggle" type="button" aria-label="{'Apri menu' if lang=='it' else 'Open menu'}" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span></button></div>
    </div><nav id="mobile-menu" class="mobile-nav" aria-label="Mobile navigation" hidden>{nav}<a href="tel:{PHONE_RAW}">{PHONE}</a></nav></header>'''

def footer(t,lang):
 return f'''<footer class="footer"><div class="container footer-inner"><div class="footer-lead"><span class="section-index">TAXI ANDREA VARENNA</span><h2>{t['foot_title']}</h2><a href="/{lang}/{'contatti/' if lang=='it' else 'contact/'}" class="text-arrow">{t['quote']} {arrow()}</a></div><div class="footer-bottom"><div><span class="foot-brand">TAXI ANDREA <em>VARENNA</em></span><p>{t['foot_small']}</p><p>Via Polvani 1 · 23829 Varenna (LC)</p></div><div class="footer-links"><a href="tel:{PHONE_RAW}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{PRIVACY}" target="_blank" rel="noopener">Privacy</a></div><div class="footer-legal"><p>© 2026 Taxi Andrea Varenna NCC di Marreddu Andrea</p><p class="vat-number">{'P. IVA' if lang=='it' else 'VAT No.'} {VAT}</p><a href="/credits.html">{t['credit_label']}</a></div></div></div></footer><div class="mobile-sticky"><a href="tel:{PHONE_RAW}" class="mobile-call">{'Chiama' if lang=='it' else 'Call'}</a><a href="https://wa.me/{PHONE_RAW[1:]}?text={quote('Buongiorno, vorrei richiedere un preventivo per un transfer. Grazie!' if lang=='it' else 'Hello, I would like to request a private transfer quote. Thank you!')}" target="_blank" rel="noopener noreferrer" class="mobile-quote"><span>WhatsApp</span><span aria-hidden="true">↗</span></a></div>'''

def quote_form(t,lang):
 s=lambda k:escape(t[k])
 # Form submits using user's own mail client; WhatsApp opens in new tab.
 return f'''<form class="quote-form" data-lang="{lang}" data-mailto="{EMAIL}" data-whatsapp="{PHONE_RAW[1:]}">
 <div class="form-row"><label>{s('form_name')}<input name="name" autocomplete="name" required placeholder="{'Mario Rossi' if lang=='it' else 'Jane Smith'}"></label><label>{s('form_email')}<input name="email" type="email" autocomplete="email" required placeholder="nome@email.com"></label></div>
 <div class="form-row"><label>{s('form_from')}<input name="pickup" required placeholder="{s('placeholder_from')}"></label><label>{s('form_to')}<input name="dropoff" required placeholder="{s('placeholder_to')}"></label></div>
 <div class="form-row three"><label>{s('form_date')}<input name="date" type="date" required></label><label>{s('form_time')}<input name="time" type="time" required></label><label>{s('form_people')}<select name="passengers" required><option value="" selected disabled>—</option>{''.join(f'<option value="{n}">{n}</option>' for n in range(1,9))}</select></label></div>
 <div class="form-row"><label>{s('form_tel')}<input name="phone" type="tel" autocomplete="tel"></label><label>{s('form_luggage')}<input name="luggage" placeholder="{'Es. 2 trolley, 1 valigia grande' if lang=='it' else 'e.g. 2 carry-ons, 1 suitcase'}"></label></div>
 <label>{s('form_notes')}<textarea name="notes" rows="3" placeholder="{s('placeholder_notes')}"></textarea></label>
 <label class="consent"><input type="checkbox" name="privacy" required><span>{s('privacy_l')} — <a href="{PRIVACY}" target="_blank" rel="noopener">Privacy policy ↗</a></span></label>
 <div class="form-actions"><button class="btn btn-dark" type="button" data-action="whatsapp">{'Richiedi su WhatsApp' if lang=='it' else 'Send via WhatsApp'} {arrow()}</button><button type="submit" class="btn btn-line">{s('mailcta')} {arrow()}</button></div>
 <p class="form-status" role="status" aria-live="polite"></p><p class="form-note">{s('form_notice')}</p></form>'''

def home(t,lang):
 contact=f'/{lang}/'+('contatti/' if lang=='it' else 'contact/')
 services=f'/{lang}/'+('servizi/' if lang=='it' else 'services/')
 vehicle=f'/{lang}/'+('mezzi/' if lang=='it' else 'vehicle/')
 items=''.join(f'''<a class="service-row" href="{services}#service-{i}"><span class="sr-number">0{i}</span><div class="sr-text"><span class="sr-kicker">{t[f's{i}small'].split('/ ')[-1]}</span><h3>{t[f's{i}']}</h3><p>{t[f's{i}p']}</p></div><span class="sr-arrow">{arrow()}</span></a>''' for i in range(1,5))
 return f'''<main>
 <section class="hero hero-v2" aria-labelledby="hero-title">
   <div class="hero-text"><div class="hero-content"><div class="hero-eyebrow"><span class="eyebrow">{t['eyebrow']}</span><span class="hero-edition">01 / LAGO DI COMO</span></div><h1 id="hero-title">{t['hero1']}<br><em>{t['hero2']}</em></h1><p>{t['hero_p']}</p><div class="hero-cta"><a class="btn btn-dark" href="#richiesta-rapida">{t['quote']} {arrow()}</a><a class="subtle-link" href="{services}">{t['explore']} <span>↗</span></a></div></div><div class="hero-foot"><span>46°00′ N / 09°17′ E</span><span>{'VARENNA — ITALIA' if lang=='it' else 'VARENNA — ITALY'}</span></div></div>
   <figure class="hero-image"><div class="hero-photo-main">{pic('hero','cover-img',t['hero_photo'],'eager')}</div><figcaption><span>{t['hero_photo']}</span><span>{'VARENNA / LAGO DI COMO' if lang=='it' else 'VARENNA / LAKE COMO'}</span></figcaption></figure>
  </section>
  <section class="route-desk" id="richiesta-rapida" aria-labelledby="route-desk-label"><div class="container route-desk-inner"><div class="route-desk-caption"><span class="section-index">{'RICHIESTA DIRETTA' if lang=='it' else 'DIRECT ENQUIRY'}</span><h2 id="route-desk-label">{'Dove ti accompagniamo?' if lang=='it' else 'Where can we take you?'}</h2><p>{'Due dettagli, poi ci sentiamo su WhatsApp.' if lang=='it' else 'A few details, then let’s talk on WhatsApp.'}</p></div><form class="quick-route" action="{contact}" method="get" data-lang="{lang}" data-whatsapp="{PHONE_RAW[1:]}"><label class="route-pickup"><span>{'PARTENZA' if lang=='it' else 'PICK-UP'}</span><input type="text" name="pickup" autocomplete="street-address" required maxlength="180" placeholder="{'Da dove parti?' if lang=='it' else 'Where from?'}"></label><label class="route-dropoff"><span>{'DESTINAZIONE' if lang=='it' else 'DESTINATION'}</span><input type="text" name="dropoff" required maxlength="180" placeholder="{'Dove vuoi arrivare?' if lang=='it' else 'Where to?'}"></label><label class="route-date"><span>{'DATA (FACOLTATIVA)' if lang=='it' else 'DATE (OPTIONAL)'}</span><input type="date" name="date"></label><label class="route-passengers"><span>{'PERSONE' if lang=='it' else 'PASSENGERS'}</span><select name="passengers" aria-label="{'Numero di passeggeri' if lang=='it' else 'Number of passengers'}"><option value="">—</option>{''.join(f'<option value="{n}">{n}</option>' for n in range(1,9))}<option value="8+">8+</option></select></label><button class="quick-whatsapp" type="submit"><span>{'Chiedi su WhatsApp' if lang=='it' else 'Enquire on WhatsApp'}</span><span class="wa-arrow" aria-hidden="true">↗</span></button><p class="quick-route-status" role="status" aria-live="polite"></p></form><p class="quick-note">{'Si apre WhatsApp con un messaggio pronto da inviare. Disponibilità e prezzo saranno confermati personalmente.' if lang=='it' else 'WhatsApp opens with a message ready to send. Availability and price will be confirmed personally.'}</p></div></section>
 <div class="info-strip"><div class="container info-grid"><span>{t['micro1']}</span><span>{t['micro2']}</span><span>{t['micro3']}</span></div></div>
 <section class="intro-section section-pad"><div class="container intro-grid"><div><span class="section-index">01 — {t['intro_k']}</span><span class="intro-decor" aria-hidden="true">↘</span></div><div><h2 class="display-title">{t['intro_h']}</h2><p class="large-copy">{t['intro_p']}</p></div></div></section>
 <section class="route-notebook" aria-label="{'Destinazioni frequenti' if lang=='it' else 'Common destinations'}"><div class="container route-notebook-grid"><span class="section-index">{'TRA LAGO E CITTÀ' if lang=='it' else 'BETWEEN LAKE AND CITY'}</span><div class="route-notebook-copy"><span class="route-notebook-sup">{'ALCUNI PERCORSI CHE POSSIAMO ORGANIZZARE' if lang=='it' else 'SOME JOURNEYS WE CAN ARRANGE'}</span><div class="route-notebook-items"><a href="{contact}?pickup=Malpensa&dropoff=Varenna"><span>Milano Malpensa</span><span class="route-connector">↗</span><strong>Varenna</strong></a><a href="{contact}?pickup=Varenna&dropoff=Bellagio"><span>Varenna</span><span class="route-connector">↗</span><strong>Bellagio</strong></a><a href="{contact}?pickup=Varenna&dropoff=St.%20Moritz"><span>Varenna</span><span class="route-connector">↗</span><strong>St. Moritz</strong></a></div></div><div class="route-notebook-aside">{'Sempre su richiesta, con itinerari e condizioni da concordare.' if lang=='it' else 'Always on request, with routes and details agreed in advance.'}</div></div></section>
 <section class="services-section section-pad" id="servizi"><div class="container"><div class="section-top"><div><span class="section-index">02 — {t['service_label']}</span><h2 class="display-title">{t['service_h']}</h2></div><div class="section-top-aside"><p>{t['service_sub']}</p><a href="{services}" class="text-arrow">{t['allservices']} {arrow()}</a></div></div><div class="services-list">{items}</div></div></section>
 <section class="photo-interlude"><div class="photo-interlude-main">{pic('lake','cover-img',t['photo_label'])}<div class="photo-shade"></div><div class="photo-content"><span class="eyebrow light">{t['photo_label']}</span><h2>{t['photo_title']}</h2><a class="btn btn-ivory" href="{services}">{t['photo_link']} {arrow()}</a></div></div><div class="photo-interlude-side">{pic('detail','cover-img','Lake Como')}<span>02 / 04 — LAGO DI COMO</span></div></section>
 <section class="vehicle-section section-pad"><div class="container vehicle-grid"><div class="vehicle-photo"><div class="photo-frame">{pic('van','cover-img','Hyundai van — Taxi Andrea Varenna')}</div><div class="frame-caption">HYUNDAI · PRIVATE TRANSFERS</div></div><div class="vehicle-copy"><span class="section-index">03 — {t['vehicle_label']}</span><h2 class="display-title">{t['vehicle_h']}</h2><p class="large-copy">{t['vehicle_p']}</p><a href="{vehicle}" class="text-arrow">{t['vehicle_link']} {arrow()}</a></div></div></section>
 <section class="local-section"><div class="container local-grid"><div class="local-side"><span class="section-index">04 — {t['local_label']}</span><div class="lat-long">46°00′ N<br>09°17′ E</div></div><div class="local-main"><h2>{t['local_h']}</h2><p>{t['local_p']}</p><div class="handline" aria-hidden="true"></div></div></div></section>
 <section class="contact-section section-pad" id="preventivo"><div class="container contact-grid"><div class="contact-intro"><span class="section-index">05 — {t['request_k']}</span><h2 class="display-title">{t['request_h']}</h2><p>{t['request_p']}</p><div class="contact-direct"><a href="tel:{PHONE_RAW}">{PHONE} ↗</a><a href="mailto:{EMAIL}">{EMAIL} ↗</a></div></div>{quote_form(t,lang)}</div></section>
 </main>'''

def inner_hero(t,kicker,title,subtitle,photo='hero'):
 return f'''<section class="inner-hero"><div class="container inner-hero-text"><span class="eyebrow">{kicker}</span><h1>{title}</h1><p>{subtitle}</p></div><div class="inner-hero-image">{pic(photo,'cover-img',title,'eager')}</div></section>'''

def services_page(t,lang):
 contact=f'/{lang}/'+('contatti/' if lang=='it' else 'contact/')
 blocks=[]
 for i,img in enumerate(['hero','water','detail','wide'],1):
  blocks.append(f'''<article class="service-feature {'flip' if i%2==0 else ''}" id="service-{i}"><div class="service-feature-media">{pic(img,'cover-img',t[f's{i}'])}</div><div class="service-feature-copy"><span class="section-index">0{i} / {t[f's{i}small'].split('/ ')[-1]}</span><h2>{t[f'ser_block_{i}']}</h2><p>{t[f'ser_block_{i}p']}</p><a class="text-arrow" href="{contact}">{t['quote']} {arrow()}</a></div></article>''')
 return '<main>'+inner_hero(t,t['ser_eyebrow'],t['ser_h'],t['ser_p'],'lake')+f'''<section class="service-features section-pad"><div class="container">{''.join(blocks)}<p class="service-disclaimer">{t['ser_note']}</p></div></section></main>'''

def vehicle_page(t,lang):
 contact=f'/{lang}/'+('contatti/' if lang=='it' else 'contact/')
 return '<main>'+inner_hero(t,t['veh_eyebrow'],t['veh_title'],t['veh_desc'],'wide')+f'''<section class="vehicle-details section-pad"><div class="container"><div class="vehicle-details-header"><span class="section-index">01 — HYUNDAI VAN</span><h2 class="display-title">{t['veh_story_h']}</h2></div><div class="vehicle-facts"><span>{t['veh_fact1']}</span><span>{t['veh_fact2']}</span><span>{t['veh_fact3']}</span></div><p class="vehicle-details-p">{t['veh_story_p']}</p><div class="vehicle-image-grid"><figure>{pic('van','cover-img','Taxi Andrea Varenna — reference vehicle')}<figcaption>HYUNDAI / EXTERIOR</figcaption></figure><figure>{pic('van2','cover-img','Taxi Andrea Varenna — second reference vehicle image')}<figcaption>HYUNDAI / INTERIOR OR DETAIL</figcaption></figure></div><p class="service-disclaimer">{t['veh_photo_note']}</p><div class="vehicle-cta"><h2>{t['request_h']}</h2><a class="btn btn-dark" href="{contact}">{t['quote']} {arrow()}</a></div></div></section></main>'''

def contact_page(t,lang):
 return f'''<main><section class="contact-page-top"><div class="container"><span class="eyebrow">{t['cont_eyebrow']}</span><h1>{t['cont_h']}</h1><p>{t['cont_p']}</p></div></section><section class="contact-page-section section-pad"><div class="container contact-grid"><div class="contact-info"><span class="section-index">{t['address_heading']}</span><p>{t['address_p']}</p><div class="info-lines"><div><span>{t['tel_l']}</span><a href="tel:{PHONE_RAW}">{PHONE} ↗</a></div><div><span>{t['email_l']}</span><a href="mailto:{EMAIL}">{EMAIL} ↗</a></div><div><span>{t['find_us']}</span><a href="https://www.google.com/maps/search/?api=1&query=Via+Polvani+1+Varenna" target="_blank" rel="noopener">{t['address']} ↗</a></div></div><div class="company-identity"><span class="section-index">{'DATI AZIENDALI' if lang=='it' else 'BUSINESS DETAILS'}</span><strong>Taxi Andrea Varenna NCC di Marreddu Andrea</strong><span>P. IVA {VAT}</span></div><div class="how-works"><h2>{t['route_title']}</h2><ol><li>{t['step1']}</li><li>{t['step2']}</li><li>{t['step3']}</li></ol><p>{t['notconfirmed']}</p></div></div><div><h2 class="form-title">{t['form_heading']}</h2>{quote_form(t,lang)}</div></div></section></main>'''

def render(lang,page):
 t=CONTENT[lang]
 titles={'home':('Taxi Andrea Varenna | Transfer privati sul Lago di Como' if lang=='it' else 'Taxi Andrea Varenna | Private Transfers on Lake Como'), 'services':t['services']+' | Taxi Andrea Varenna','vehicle':t['vehicle']+' | Taxi Andrea Varenna','contacts':t['contacts']+' | Taxi Andrea Varenna'}
 desc=t['hero_p'] if page=='home' else {'services':t['ser_p'],'vehicle':t['veh_desc'],'contacts':t['cont_p']}[page]
 paths={'it':{'home':'','services':'servizi/','vehicle':'mezzi/','contacts':'contatti/'},'en':{'home':'','services':'services/','vehicle':'vehicle/','contacts':'contact/'}}
 local=f'/{lang}/{paths[lang][page]}'
 alt='en' if lang=='it' else 'it'
 alt_path=f'/{alt}/{paths[alt][page]}'
 body={'home':home,'services':services_page,'vehicle':vehicle_page,'contacts':contact_page}[page](t,lang)
 structured={'@context':'https://schema.org','@type':'TaxiService','name':'Taxi Andrea Varenna NCC di Marreddu Andrea','url':'https://www.varenna-taxi.it/','telephone':PHONE_RAW,'email':EMAIL,'vatID':'IT'+VAT,'address':{'@type':'PostalAddress','streetAddress':'Via Polvani 1','addressLocality':'Varenna','postalCode':'23829','addressRegion':'LC','addressCountry':'IT'},'areaServed':['Varenna','Lake Como','Lombardy']}
 return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#17332f"><meta name="robots" content="noindex,nofollow"><title>{escape(titles[page])}</title><meta name="description" content="{escape(desc,quote=True)}"><link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml"><link rel="preconnect" href="https://commons.wikimedia.org"><link rel="preconnect" href="https://static.wixstatic.com"><link rel="stylesheet" href="/assets/css/styles.css"><link rel="alternate" hreflang="it" href="https://www.varenna-taxi.it/it/{paths['it'][page]}"><link rel="alternate" hreflang="en" href="https://www.varenna-taxi.it/en/{paths['en'][page]}"><meta property="og:title" content="{escape(titles[page],quote=True)}"><meta property="og:description" content="{escape(desc,quote=True)}"><meta property="og:type" content="website"><script type="application/ld+json">{json.dumps(structured,ensure_ascii=False)}</script><script src="/assets/js/main.js" defer></script></head><body><a class="skip-link" href="#main-content">{'Vai al contenuto' if lang=='it' else 'Skip to content'}</a>{header(t,lang,page)}<div id="main-content">{body}</div>{footer(t,lang)}</body></html>'''

for lang in ('it','en'):
 for page,path in [('home',''),('services','servizi' if lang=='it' else 'services'),('vehicle','mezzi' if lang=='it' else 'vehicle'),('contacts','contatti' if lang=='it' else 'contact')]:
  target=OUT/lang/path/'index.html'
  target.parent.mkdir(parents=True,exist_ok=True)
  target.write_text(render(lang,page),encoding='utf-8')
(OUT/'index.html').write_text('''<!doctype html><html lang="it"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=/it/"><meta name="robots" content="noindex"></head><body><a href="/it/">Vai alla versione italiana</a></body></html>''',encoding='utf-8')
(OUT/'credits.html').write_text('''<!doctype html><html lang="it"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Crediti fotografici — Taxi Andrea Varenna</title><link rel="stylesheet" href="/assets/css/styles.css"><main class="credits-page"><a href="/it/">← Torna al sito</a><h1>Crediti fotografici</h1><p>Fotografie reali di Varenna e del Lago di Como provenienti da Wikimedia Commons. La foto principale è CC0; le altre sono sotto licenza CC BY-SA 4.0. Il layout applica ritagli fotografici e lievi regolazioni colore.</p><ul><li><a href="https://commons.wikimedia.org/wiki/File:Varenna_20260811.jpg">Varenna 20260811</a> — DD991, CC0 1.0</li><li><a href="https://commons.wikimedia.org/wiki/File:Varenna_-_View_from_Lake_Como.jpg">Varenna - View from Lake Como</a> — Xavier Caré</li><li><a href="https://commons.wikimedia.org/wiki/File:Varenna_Shore.jpg">Varenna Shore</a> — P. Hughes</li><li><a href="https://commons.wikimedia.org/wiki/File:Sunset_lake_como_varenna_Italy.jpg">Sunset lake como varenna Italy</a> — Reem Al-Kashif</li><li><a href="https://commons.wikimedia.org/wiki/File:Lake_Como_Varenna_Italy.jpg">Lake Como Varenna Italy</a> — Reem Al-Kashif</li></ul><p>Licenze: <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a> e <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.</p><p>Le fotografie del veicolo provengono dal sito esistente varenna-taxi.it e sono da verificare con il titolare prima della pubblicazione. Questo prototipo non trasferisce alcun diritto sui relativi contenuti.</p></main></html>''',encoding='utf-8')
print('Generated',len(list(OUT.rglob('*.html'))),'HTML pages')
