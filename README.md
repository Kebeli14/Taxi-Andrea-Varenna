# Taxi Andrea Varenna — Quiet Confidence / V3

Restyling **multipagina, bilingue IT/EN, responsive** di Taxi Andrea Varenna. HTML semantico, CSS su misura e JavaScript vanilla, senza dipendenze da installare né kit grafici preconfezionati.

## Apri l'anteprima in locale

**Windows**: estrai lo ZIP, entra nella cartella `Taxi_Andrea_Varenna_V3` e fai doppio clic su `AVVIA_ANTEPRIMA_WINDOWS.bat`. È necessario **Node.js** installato.

In alternativa, apri il terminale nella cartella principale e digita:

```bash
npm run dev
```

Vai su **http://localhost:4173/it/**. Non devi eseguire `npm install`.

Se la porta 4173 fosse già occupata: `set PORT=4188 && npm run dev` (Prompt dei comandi su Windows) oppure `$env:PORT=4188; npm run dev` (PowerShell), poi apri `http://localhost:4188/it/`.

### Pagine

- `/it/` e `/en/`: homepage
- `/it/servizi/` e `/en/services/`: servizi
- `/it/mezzi/` e `/en/vehicle/`: mezzo
- `/it/contatti/` e `/en/contact/`: contatti e richiesta preventivo
- `/credits.html`: crediti delle fotografie

## Novità della V3

- **Richiesta rapida via WhatsApp**: sulla homepage, partenza e destinazione sono obbligatorie, data e passeggeri sono facoltativi. Il pulsante apre `wa.me` con un testo già preparato in **italiano o inglese**, in base alla lingua della pagina. Il visitatore può rivederlo e inviarlo; non parte nessun messaggio automaticamente.
- **Modulo dettagliato**: nella pagina Contatti e in fondo alla homepage, WhatsApp è l’azione principale, email quella secondaria. Entrambe includono i dati inseriti.
- **Mobile**: barra fissa Chiama / WhatsApp; form con campo data e passeggeri affiancati, tap target ampi, contrasto migliorato e navigazione dedicata.
- **Nuova direzione grafica**: palette più neutra (avorio quasi bianco, verde petrolio scuro, bronzo dosato), fotografia protagonista senza badge turistici o sovrapposizioni fittizie, impaginazione più pulita.
- **Partita IVA**: **04141980138** nel footer, contatti e schema SEO. Da confermare con il titolare prima della pubblicazione.
- **Nessun backend necessario** per generare l’anteprima delle richieste: invio e conferma restano manuali su WhatsApp o email.

### Test del flusso WhatsApp

1. Apri `http://localhost:4173/it/`, inserisci **Varenna** e **Malpensa** nella richiesta rapida e clicca **Chiedi su WhatsApp**.
2. Verifica che si apra `wa.me/393770959389` e che il testo contenga partenza, destinazione ed eventuali data e passeggeri.
3. Ripeti da `http://localhost:4173/en/` per controllare il testo inglese.

**Importante:** la numerazione del contatto è quella pubblicata dal servizio. Prima della pubblicazione confermare con Andrea che sia il suo account WhatsApp effettivamente operativo.

## Dati aziendali utilizzati

- Nome commerciale: Taxi Andrea Varenna
- Ragione sociale: Taxi Andrea Varenna NCC di Marreddu Andrea
- P. IVA: **04141980138** (dato da confermare con il titolare prima della pubblicazione)
- Telefono: +39 377 095 9389
- E-mail: taxi.andrea.varenna@gmail.com
- Indirizzo operativo pubblicato sul sito: Via Polvani 1, Varenna (LC)

Fonti consultate:
- Sito pubblico: https://www.varenna-taxi.it/it
- Scheda aziendale P. IVA: https://reportazienda.it/aziende/LC/taxi-andrea-varenna-ncc-di-marreddu-andrea-423553

## Modifica contenuti, design e interazioni

- `source/generate.py`: testi, traduzioni, URL immagini, navigazione, markup HTML. Dopo modifica: `python source/generate.py`.
- `site/assets/css/styles.css`: responsive e grafica su misura.
- `site/assets/js/main.js`: navigazione, precompilazione campi, composizione richieste email / WhatsApp.
- `site/`: sito statico generato, pronto da portare su un hosting statico dopo le verifiche di produzione.

## Prima di pubblicare

- **Non è un motore di prenotazione**. I pulsanti del modulo compongono un'email o un messaggio WhatsApp nel dispositivo del visitatore; l'invio deve essere completato dal visitatore. Per notifiche affidabili e gestione delle richieste online serve backend con provider email, antispam e gestione privacy.
- **WhatsApp**: il numero pubblico potrebbe non essere abilitato a WhatsApp. Confermarlo con il titolare.
- **Foto del mezzo**: vengono richiamate dal sito originale e servono autorizzazione e conferma che mostrino il mezzo utilizzato attualmente. «8 posti» riprende quanto scritto dal sito, ma bisogna verificare il numero di passeggeri escluso il conducente.
- **Foto del lago**: vengono caricate da Wikimedia Commons a runtime, non sono distribuite nello ZIP; connettività richiesta. I crediti e le licenze sono nella pagina dedicata. Per un risultato stabile e veloce, in produzione è preferibile usare foto proprie e immagini ottimizzate localmente con diritti accertati.
- **Privacy**: l'informativa attualmente collegata è quella presente sul sito originale; riesaminare contenuto e adempimenti rispetto alle modalità effettive di raccolta e al nuovo hosting.
- **SEO**: tutte le pagine di questa anteprima includono `noindex,nofollow` per evitare indicizzazione accidentale. Prima di andare online rimuovere questa direttiva, verificare canonical/hreflang, sitemap, robots e redirect delle vecchie pagine.
- **Dominio e pubblicazione**: non è stata apportata alcuna modifica al sito Wix attivo. Nessuna credenziale o accesso è necessario per provare questa V3 localmente.

È un **prototipo navigabile avanzato** da valutare visivamente e funzionalmente, non una prenotazione automatizzata già pronta alla produzione.
