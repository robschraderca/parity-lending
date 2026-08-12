// parity-inquiry — Check My Numbers inquiry form → GoHighLevel
// POST { name, email, phone, address, scenario, page }
// 1) upserts the contact with Loan Details custom fields + tags
// 2) adds a note with the full scenario
// 3) emails the lead a confirmation (via GHL conversations API)
// 4) emails internal alerts to ALERT_EMAILS

const GHL = 'https://services.msgsndr.com';
const ALLOWED_ORIGINS = [
  'https://paritylending.com',
  'https://www.paritylending.com',
  'https://parity-lending.robschraderca.workers.dev',
  'https://robschraderca.github.io',
];

let FIELD_CACHE = null; // name -> id

function cors(origin) {
  const ok = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    'Access-Control-Allow-Origin': ok,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Vary': 'Origin',
  };
}

function json(body, status, origin) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', ...cors(origin) },
  });
}

async function ghl(env, method, path, body) {
  const res = await fetch(GHL + path, {
    method,
    headers: {
      Authorization: 'Bearer ' + env.GHL_TOKEN,
      Version: '2021-07-28',
      'Content-Type': 'application/json',
      Accept: 'application/json',
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const text = await res.text();
  let data = null;
  try { data = JSON.parse(text); } catch (e) { /* keep text */ }
  if (!res.ok) throw new Error(`GHL ${method} ${path} -> ${res.status}: ${text.slice(0, 400)}`);
  return data;
}

async function getFieldIds(env) {
  if (FIELD_CACHE) return FIELD_CACHE;
  const data = await ghl(env, 'GET', `/locations/${env.LOCATION_ID}/customFields`);
  const map = {};
  for (const f of data.customFields || []) map[f.name] = f.id;
  FIELD_CACHE = map;
  return map;
}

const money = (n) => '$' + Math.round(+n || 0).toLocaleString('en-US');

function mapPropertyType(pt) {
  // GHL dropdown: Condo, Townhouse, Single-Family, 2 Units, 3 Units, 4 Units
  if (pt === 'Single-family rental') return 'Single-Family';
  if (pt === 'Condo / townhome') return 'Condo';
  return null; // "2-4 unit" ambiguous, "Short-term rental" not in list -> note only
}

function buildCustomFields(fieldIds, p, s) {
  const rows = [];
  const add = (name, value) => {
    if (value === null || value === undefined || value === '' || !fieldIds[name]) return;
    rows.push({ id: fieldIds[name], field_value: value });
  };
  if (s) {
    add('Loan Purpose', s.goal === 'Purchase' ? 'Purchase' : (s.goal ? 'Refinance' : null));
    add('Property Value / Purchase Price', Math.round(s.price || 0) || null);
    add('Loan Amount', Math.round(s.loan || 0) || null);
    add('LTV', s.ltv || null);
    add('Property Type', mapPropertyType(s.ptype));
    add('Gross Monthly Rent', Math.round(s.rent || 0) || null);
    if (s.hoa > 0) add('HOA Dues (Annual)', Math.round(s.hoa * 12));
    if (s.ficoN >= 300) add('Credit Score (Stated)', s.ficoN);
  }
  add('Property Address', p.address);
  return rows;
}

function scenarioNote(p, s) {
  const L = [];
  L.push('WEBSITE INQUIRY — Check My Numbers calculator');
  L.push(`Submitted: ${new Date().toISOString()}`);
  L.push('');
  L.push(`Name: ${p.name}`);
  L.push(`Email: ${p.email}`);
  L.push(`Phone: ${p.phone}`);
  L.push(`Property address: ${p.address}`);
  if (s) {
    L.push('');
    L.push(`Goal: ${s.goal || 'n/a'}`);
    L.push(`Property type: ${s.ptype || 'n/a'}${s.isSTR ? ' (short-term rental, 20% expense factor applied)' : ''}`);
    L.push(`Price / value: ${money(s.price)}`);
    L.push(`Gross monthly rent: ${money(s.rent)}`);
    L.push(`Down payment / equity: ${s.downPct}% (LTV ${s.ltv}%)`);
    L.push(`Monthly HOA: ${money(s.hoa)}`);
    L.push(`Credit band (stated): ${s.fico || 'n/a'}`);
    L.push(`Timeline: ${s.time || 'n/a'}`);
    L.push(`Vesting: ${s.vest || 'n/a'}`);
    L.push('');
    L.push('--- CALCULATOR ESTIMATE (illustrative, taxes 1.1%/yr, insurance 0.55%/yr assumed) ---');
    L.push(`Loan amount: ${money(s.loan)}`);
    L.push(`Estimated DSCR: ${s.dscr}`);
    L.push(`Illustrative rate: ${s.rate}%`);
    L.push(`Estimated PITIA: ${money(s.pitia)}/mo`);
    L.push(`Estimated cash flow: ${s.cashFlow < 0 ? '-' : ''}${money(Math.abs(s.cashFlow))}/mo`);
    L.push(`Cash to close (down payment): ${money(s.downPayment)}`);
    L.push(`Reserves required (est.): ${s.resMonths} months`);
  }
  if (p.page) { L.push(''); L.push(`Page: ${p.page}`); }
  return L.join('\n');
}

function leadEmailHtml(p, s) {
  const row = (k, v) => `<tr><td style="padding:6px 14px 6px 0;color:#5A6484;white-space:nowrap">${k}</td><td style="padding:6px 0;font-weight:600;color:#0E1B3D">${v}</td></tr>`;
  let table = '';
  if (s) {
    table = `<table style="border-collapse:collapse;font-size:14px;margin:18px 0">${
      row('Goal', s.goal || '—')}${
      row('Property', s.ptype || '—')}${
      row('Price / value', money(s.price))}${
      row('Gross monthly rent', money(s.rent))}${
      row('Down payment / equity', `${s.downPct}% (LTV ${s.ltv}%)`)}${
      row('Estimated DSCR', s.dscr)}</table>`;
  }
  return `<div style="font-family:Arial,Helvetica,sans-serif;color:#0E1B3D;font-size:15px;line-height:1.6;max-width:560px">
  <p>Hi ${p.name.split(' ')[0]},</p>
  <p>We received your inquiry from the Check My Numbers calculator at paritylending.com — thank you.
  A licensed loan officer will review your scenario and get back to you shortly.</p>
  ${table}
  <p>If anything above changes, or you want to add detail (like the property address or a purchase contract),
  just reply to this email.</p>
  <p style="margin-bottom:2px">— Parity Lending</p>
  <p style="color:#5A6484;font-size:13px;margin-top:0">info@paritylending.com</p>
  <p style="color:#8A91A6;font-size:11px;margin-top:22px">Business-purpose loans for non-owner-occupied investment
  property only. The numbers above are estimates from your own inputs, not an offer, quote, rate lock, or commitment
  to lend. RSS Financial Holdings LLC dba Parity Lending.</p>
</div>`;
}

function alertEmailHtml(p, s, contactId, locationId) {
  const link = `https://app.gohighlevel.com/v2/location/${locationId}/contacts/detail/${contactId}`;
  return `<div style="font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:1.6;color:#0E1B3D">
  <h2 style="font-size:16px">New DSCR inquiry — Check My Numbers</h2>
  <pre style="background:#F2F3F6;padding:14px;border-radius:8px;font-size:13px;white-space:pre-wrap">${
    scenarioNote(p, s).replace(/</g, '&lt;')}</pre>
  <p><a href="${link}">Open contact in HighLevel</a></p>
</div>`;
}

async function sendEmail(env, contactId, subject, html) {
  return ghl(env, 'POST', '/conversations/messages', {
    type: 'Email',
    contactId,
    subject,
    html,
    emailReplyTo: env.REPLY_TO || 'info@paritylending.com',
  });
}

async function upsertContact(env, fields, p, tags, source) {
  const parts = p.name.trim().split(/\s+/);
  const firstName = parts.shift() || '';
  const lastName = parts.join(' ');
  const body = {
    locationId: env.LOCATION_ID,
    firstName,
    lastName,
    name: p.name.trim(),
    email: p.email,
    phone: p.phone || undefined,
    address1: p.address || undefined,
    source,
    tags,
    customFields: fields,
  };
  const data = await ghl(env, 'POST', '/contacts/upsert', body);
  return data.contact?.id || data.contact?._id || data.id;
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors(origin) });
    if (request.method !== 'POST') return json({ error: 'POST only' }, 405, origin);

    let p;
    try { p = await request.json(); } catch (e) { return json({ error: 'bad json' }, 400, origin); }

    const bad = [];
    if (!p.name || p.name.trim().length < 2) bad.push('name');
    if (!p.email || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(p.email)) bad.push('email');
    if (!p.phone || String(p.phone).replace(/\D/g, '').length < 10) bad.push('phone');
    if (!p.address || p.address.trim().length < 5) bad.push('address');
    if (bad.length) return json({ error: 'invalid fields', fields: bad }, 400, origin);

    const s = p.scenario || null;
    const result = { ok: true, emails: {} };

    try {
      // 1) lead contact with Loan Details fields
      const fieldIds = await getFieldIds(env);
      const cf = buildCustomFields(fieldIds, p, s);
      const contactId = await upsertContact(env, cf, p,
        ['website-inquiry', 'check-my-numbers'], 'Check My Numbers calculator');
      result.contactId = contactId;

      // 2) scenario note
      try {
        await ghl(env, 'POST', `/contacts/${contactId}/notes`, { body: scenarioNote(p, s) });
      } catch (e) { result.note = String(e.message).slice(0, 300); }

      // 3) confirmation email to the lead
      try {
        await sendEmail(env, contactId, 'We received your inquiry — Parity Lending', leadEmailHtml(p, s));
        result.emails.lead = 'sent';
      } catch (e) { result.emails.lead = String(e.message).slice(0, 300); }

      // 4) internal alerts
      const alerts = (env.ALERT_EMAILS || '').split(',').map(x => x.trim()).filter(Boolean);
      result.emails.alerts = [];
      for (const addr of alerts) {
        try {
          const aid = await upsertContact(env, [],
            { name: addr === 'michael@tunited.net' ? 'Michael McDermott' : 'Rob Schrader',
              email: addr, phone: '', address: '' },
            ['internal-alerts'], 'internal');
          await sendEmail(env, aid,
            `New DSCR inquiry: ${s?.goal || 'inquiry'}, ${money(s?.price || 0)} — ${p.name}`,
            alertEmailHtml(p, s, contactId, env.LOCATION_ID));
          result.emails.alerts.push(addr + ': sent');
        } catch (e) { result.emails.alerts.push(addr + ': ' + String(e.message).slice(0, 200)); }
      }

      return json(result, 200, origin);
    } catch (e) {
      return json({ error: String(e.message).slice(0, 500) }, 502, origin);
    }
  },
};
