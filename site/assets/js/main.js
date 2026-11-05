/* Taxi Andrea Varenna — accessible, dependency-free interactions. */
(() => {
  'use strict';
  const isEnglish = document.documentElement.lang === 'en';
  const menuButton = document.querySelector('.menu-toggle');
  const mobileMenu = document.getElementById('mobile-menu');
  if (menuButton && mobileMenu) {
    const closeMenu = () => {
      menuButton.setAttribute('aria-expanded', 'false');
      mobileMenu.hidden = true;
      document.body.classList.remove('menu-open');
    };
    menuButton.addEventListener('click', () => {
      const opening = menuButton.getAttribute('aria-expanded') !== 'true';
      menuButton.setAttribute('aria-expanded', String(opening));
      mobileMenu.hidden = !opening;
      document.body.classList.toggle('menu-open', opening);
    });
    mobileMenu.addEventListener('click', event => {
      if (event.target.closest('a')) closeMenu();
    });
    window.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
    window.addEventListener('resize', () => { if (window.innerWidth > 880) closeMenu(); });
  }

  const today = new Date();
  const isoToday = [today.getFullYear(), String(today.getMonth()+1).padStart(2, '0'), String(today.getDate()).padStart(2, '0')].join('-');
  document.querySelectorAll('input[type="date"]').forEach(input => { input.min = isoToday; });

  const clean = value => String(value || '').trim().replace(/[\u0000-\u001F]+/g, ' ').slice(0, 250);
  const formatDate = value => {
    if (!value) return '';
    const parts = value.split('-');
    if (parts.length !== 3) return value;
    return isEnglish ? [parts[2], parts[1], parts[0]].join('/') : [parts[2], parts[1], parts[0]].join('/');
  };
  const openWhatsapp = (number, message) => {
    const href = 'https://wa.me/' + encodeURIComponent(number) + '?text=' + encodeURIComponent(message);
    // Triggered exclusively by a user action; visitor still reviews/sends in WhatsApp.
    const link = document.createElement('a');
    link.href = href;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    document.body.append(link);
    link.click();
    link.remove();
  };

  // Quick request: no personal data is stored or submitted to this website.
  document.querySelectorAll('.quick-route').forEach(form => {
    form.addEventListener('submit', event => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const data = new FormData(form);
      const pickup = clean(data.get('pickup'));
      const dropoff = clean(data.get('dropoff'));
      const date = formatDate(clean(data.get('date')));
      const passengers = clean(data.get('passengers'));
      const status = form.querySelector('.quick-route-status');
      if (!pickup || !dropoff) {
        if (status) status.textContent = isEnglish ? 'Please enter pick-up and destination.' : 'Inserisci partenza e destinazione.';
        return;
      }
      const lines = isEnglish ? [
        'Hello Andrea, I would like a quote for a private transfer.', '',
        'Pick-up: ' + pickup,
        'Destination: ' + dropoff,
        ...(date ? ['Travel date: ' + date] : []),
        ...(passengers ? ['Passengers: ' + passengers] : []),
        '', 'Could you please confirm availability and price? Thank you.'
      ] : [
        'Buongiorno Andrea, vorrei richiedere un preventivo per un transfer.', '',
        'Partenza: ' + pickup,
        'Destinazione: ' + dropoff,
        ...(date ? ['Data del viaggio: ' + date] : []),
        ...(passengers ? ['Passeggeri: ' + passengers] : []),
        '', 'Potresti confermarmi disponibilità e prezzo? Grazie.'
      ];
      if (status) status.textContent = isEnglish ? 'Opening WhatsApp with your request…' : 'Apertura di WhatsApp con la richiesta…';
      openWhatsapp(form.dataset.whatsapp, lines.join('\n'));
    });
  });

  // Optional pre-fill for itinerary links. No storage or server request.
  const params = new URLSearchParams(window.location.search);
  const contactForm = document.querySelector('.contact-page-section .quote-form');
  if (contactForm && (params.has('pickup') || params.has('dropoff'))) {
    for (const key of ['pickup', 'dropoff']) {
      const field = contactForm.elements.namedItem(key);
      if (field && params.has(key)) field.value = clean(params.get(key));
    }
    const title = document.querySelector('.form-title');
    if (title) {
      const tip = document.createElement('span');
      tip.className = 'prefill-tip';
      tip.textContent = isEnglish ? ' · Route added' : ' · Percorso inserito';
      title.append(tip);
    }
  }

  document.querySelectorAll('.quote-form').forEach(form => {
    const english = form.dataset.lang === 'en';
    const status = form.querySelector('.form-status');
    function compose() {
      if (!form.reportValidity()) {
        if (status) status.textContent = english ? 'Please complete the required fields.' : 'Completa i campi obbligatori.';
        return null;
      }
      const data = Object.fromEntries([...new FormData(form)].map(([key, val]) => [key, clean(val)]));
      if (!data.privacy) {
        if (status) status.textContent = english ? 'Please accept the privacy notice.' : 'Leggi e accetta l’informativa privacy.';
        return null;
      }
      const rows = english ? [
        'Hello Andrea, I would like a private transfer quote.', '',
        'Name: ' + data.name, 'Email: ' + data.email, 'Phone: ' + (data.phone || '—'),
        'Pick-up: ' + data.pickup, 'Destination: ' + data.dropoff,
        'Travel date: ' + formatDate(data.date), 'Time: ' + data.time,
        'Passengers: ' + data.passengers, 'Luggage: ' + (data.luggage || '—'),
        'Notes: ' + (data.notes || '—'), '',
        'Please confirm availability and price. Thank you!'
      ] : [
        'Buongiorno Andrea, vorrei un preventivo per un transfer.', '',
        'Nome: ' + data.name, 'Email: ' + data.email, 'Telefono: ' + (data.phone || '—'),
        'Partenza: ' + data.pickup, 'Destinazione: ' + data.dropoff,
        'Data del viaggio: ' + formatDate(data.date), 'Orario: ' + data.time,
        'Passeggeri: ' + data.passengers, 'Bagagli: ' + (data.luggage || '—'),
        'Note: ' + (data.notes || '—'), '',
        'Potresti confermare disponibilità e prezzo? Grazie!'
      ];
      return rows.join('\n');
    }
    form.addEventListener('submit', event => {
      event.preventDefault();
      const message = compose();
      if (!message) return;
      const subject = english ? 'Private transfer quote - Taxi Andrea Varenna' : 'Richiesta preventivo transfer - Taxi Andrea Varenna';
      if (status) status.textContent = english ? 'Your email app will open to complete sending.' : 'Si aprirà l’app email per completare l’invio.';
      window.location.href = 'mailto:' + form.dataset.mailto + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(message);
    });
    const whatsappButton = form.querySelector('[data-action="whatsapp"]');
    if (whatsappButton) whatsappButton.addEventListener('click', () => {
      const message = compose();
      if (!message) return;
      if (status) status.textContent = english ? 'Opening WhatsApp with your request…' : 'Apertura di WhatsApp con la richiesta…';
      openWhatsapp(form.dataset.whatsapp, message);
    });
  });
})();
