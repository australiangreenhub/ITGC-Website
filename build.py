#!/usr/bin/env python3
"""Build script: generates the multi-page IT Green Consulting static site."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
PHONE = "0415 271 956"
PHONE_TEL = "tel:+61415271956"
EMAIL = "info@itgreenconsulting.com.au"

SERVICES = [
    ("certificate-services", "Certificate Services", "certificate-services.html",
     "STC · VEEC · ESC · PRC",
     "M10 3H4a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z M10 3v5h5 M8 14l2 2 4-4"),
    ("energy-rebates", "Energy Rebates", "energy-rebates.html",
     "Quick claims · Fast payments",
     "M3 7h18a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1z M3 11h18 M7 3v3 M17 3v3"),
    ("sales", "Sales", "sales.html",
     "Sales for installers · Quotes",
     "M3 11l18-7-7 18-2.5-8z"),
    ("energy-audits", "Energy Audits", "energy-audits.html",
     "Savings · Certificate potential",
     "M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14z M21 21l-4.35-4.35"),
    ("aggregation", "Aggregation", "aggregation.html",
     "Better prices · Less admin",
     "M4 17l6-6-6-6 M12 19h8"),
    ("it-support", "IT Support", "it-support.html",
     "Helpdesk · Devices · Systems",
     "M2 5h20a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z M8 21h8 M12 18v3 M7 10l2 2-2 2 M13 14h3"),
    ("billing-facility", "Billing Facility", "billing-facility.html",
     "Invoices · Payment tracking",
     "M6 2h12a1 1 0 0 1 1 1v19l-2.3-1.6L14.4 21l-2.4-1.6L9.6 21l-2.3-1.6L5 21V3a1 1 0 0 1 1-1z M9 7h6 M9 11h6 M9 15h4"),
]

CSS = r"""
:root{
  --navy:#0A1428; --navy-2:#0B1B33; --navy-3:#12294D;
  --blue:#1E6FD9; --blue-bright:#3A9BEE; --blue-soft:rgba(58,155,238,.12);
  --grad:linear-gradient(135deg,#1E6FD9,#3A9BEE);
  --silver:#C9D3DE; --ice:#EAF0F6; --muted:#93A5B8; --muted-onlight:#5A6B7F;
  --line:#DCE6F0; --line-dark:rgba(201,211,222,.18);
  --white:#fff; --paper:#F4F7FB;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;color:#33475E;line-height:1.65;background:var(--white)}
.container{max-width:1160px;margin:0 auto;padding:0 24px}
section{padding:88px 0}
a{color:var(--blue)}
img{max-width:100%}

/* Nav */
nav{position:sticky;top:0;z-index:50;background:rgba(10,20,40,.97);backdrop-filter:blur(8px);border-bottom:1px solid var(--line-dark)}
.nav-inner{display:flex;align-items:center;justify-content:space-between;height:80px;gap:16px}
.logo{display:flex;align-items:center;gap:12px;font-weight:800;font-size:1.18rem;color:var(--ice);text-decoration:none}
.logo img{width:52px;height:52px;border-radius:10px;display:block;background:#fff;padding:5px}
.logo .accent{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.nav-links{display:flex;gap:26px;list-style:none;align-items:center;margin:0;padding:0}
.nav-links>li{position:relative}
.nav-links a{text-decoration:none;color:var(--silver);font-weight:500;font-size:.95rem;padding:10px 2px;display:inline-block}
.nav-links a:hover,.nav-links a.active{color:#fff}
.nav-links a.active{border-bottom:2px solid var(--blue-bright)}
.drop{position:absolute;top:100%;left:-14px;min-width:250px;background:var(--navy-2);border:1px solid var(--line-dark);border-radius:14px;padding:10px;display:none;box-shadow:0 20px 50px rgba(0,0,0,.5)}
.has-drop:hover .drop,.has-drop:focus-within .drop{display:block}
.drop a{display:block;padding:10px 14px;border-radius:8px;font-size:.92rem}
.drop a:hover{background:var(--navy-3)}
.btn{display:inline-block;background:var(--grad);color:#fff;font-weight:600;text-decoration:none;padding:12px 26px;border-radius:10px;border:none;cursor:pointer;font-size:1rem;transition:.2s;box-shadow:0 8px 22px rgba(30,111,217,.35)}
.btn:hover{filter:brightness(1.1);transform:translateY(-1px)}
.btn-sm{padding:9px 18px;font-size:.9rem}
.nav-phone{color:var(--ice);text-decoration:none;font-weight:600;font-size:.95rem;white-space:nowrap}
.nav-phone:hover{color:var(--blue-bright)}
.nav-cta{display:flex;align-items:center;gap:16px}
.burger{display:none;background:none;border:none;cursor:pointer;padding:8px}
.burger span{display:block;width:26px;height:3px;background:var(--ice);border-radius:2px;margin:5px 0;transition:.25s}
@media(max-width:980px){
  .nav-links{position:fixed;top:80px;left:0;right:0;background:var(--navy);flex-direction:column;align-items:stretch;padding:12px 24px 24px;gap:0;display:none;border-bottom:1px solid var(--line-dark);max-height:calc(100vh - 80px);overflow:auto}
  body.nav-open .nav-links{display:flex}
  .nav-links a{padding:12px 4px;border-bottom:1px solid var(--line-dark);width:100%}
  .drop{position:static;display:none;border:none;background:transparent;box-shadow:none;padding:0 0 0 16px;min-width:0}
  .has-drop.sub-open .drop{display:block}
  .burger{display:block}
  .nav-phone{display:none}
}
@media(max-width:520px){.nav-cta .btn{display:none}.logo{font-size:1rem}.logo img{width:44px;height:44px}}

/* Hero */
.hero{position:relative;overflow:hidden;background:radial-gradient(1100px 520px at 85% -10%,rgba(58,155,238,.28),transparent),radial-gradient(800px 400px at 0% 110%,rgba(30,111,217,.18),transparent),linear-gradient(180deg,var(--navy),var(--navy-2));padding:100px 0 96px;color:var(--silver)}
.hero::before{content:"";position:absolute;inset:-40%;background:conic-gradient(from 0deg at 60% 40%,transparent 0deg,rgba(58,155,238,.10) 60deg,transparent 120deg,rgba(30,111,217,.08) 200deg,transparent 280deg);animation:spinGlow 26s linear infinite;pointer-events:none}
@keyframes spinGlow{to{transform:rotate(360deg)}}
.hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:56px;align-items:center;position:relative}
@media(max-width:900px){.hero-grid{grid-template-columns:1fr}}
.eyebrow{display:inline-block;background:var(--blue-soft);border:1px solid rgba(58,155,238,.4);color:var(--blue-bright);font-weight:600;font-size:.82rem;letter-spacing:.06em;text-transform:uppercase;padding:6px 14px;border-radius:999px;margin-bottom:20px}
h1{font-size:clamp(2.2rem,4.5vw,3.4rem);line-height:1.12;color:#fff;font-weight:800;margin-bottom:20px}
h1 .g{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.lede{font-size:1.15rem;color:var(--silver);margin-bottom:32px;max-width:520px}
.hero-ctas{display:flex;gap:14px;flex-wrap:wrap;align-items:center}
.btn-outline{background:transparent;color:var(--ice);border:2px solid var(--blue);box-shadow:none}
.btn-outline:hover{background:var(--blue-soft);filter:none}
.hero-art{position:relative;display:flex;align-items:center;justify-content:center;padding-bottom:46px}
.hero-logo{width:min(100%,430px);height:auto;border-radius:24px;background:#fff;padding:26px;box-shadow:0 30px 70px rgba(0,0,0,.5),0 0 0 1px rgba(58,155,238,.25);animation:floatY 7s ease-in-out infinite}
@keyframes floatY{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
.card-float{position:absolute;bottom:0;right:8px;background:rgba(11,27,51,.92);border:1px solid rgba(58,155,238,.45);border-radius:14px;padding:14px 18px;box-shadow:0 12px 32px rgba(0,0,0,.4);font-size:.85rem;color:var(--silver)}
.card-float strong{color:var(--blue-bright)}
.pulse{width:10px;height:10px;border-radius:50%;background:var(--blue-bright);display:inline-block;margin-right:8px;animation:pulse 2s infinite}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(58,155,238,.5)}70%{box-shadow:0 0 0 10px rgba(58,155,238,0)}100%{box-shadow:0 0 0 0 rgba(58,155,238,0)}}
@media(max-width:900px){.hero-art{margin-top:8px}.card-float{right:4%}}

/* Page hero */
.page-hero{position:relative;overflow:hidden;color:var(--silver);padding:110px 0 90px;background:linear-gradient(180deg,var(--navy),var(--navy-2))}
.page-hero .bg{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.28}
.page-hero .bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,20,40,.55),rgba(10,20,40,.88))}
.page-hero .inner{position:relative}
.crumbs{font-size:.85rem;color:var(--muted);margin-bottom:16px}
.crumbs a{color:var(--blue-bright);text-decoration:none}
.page-hero h1{margin-bottom:16px}

/* Marquee */
.marquee{background:var(--navy);border-top:1px solid var(--line-dark);border-bottom:1px solid var(--line-dark);overflow:hidden;padding:18px 0}
.marquee-track{display:flex;gap:56px;width:max-content;animation:scrollX 26s linear infinite;list-style:none;margin:0;padding:0}
.marquee-track span{color:var(--blue-bright);font-weight:700;letter-spacing:.14em;font-size:.9rem;white-space:nowrap}
.marquee-track .dot{color:var(--muted)}
@keyframes scrollX{to{transform:translateX(-50%)}}

/* Sections */
.sec-title{text-align:center;max-width:700px;margin:0 auto 56px}
.sec-title h2{font-size:clamp(1.7rem,3vw,2.4rem);color:var(--navy);font-weight:800;margin-bottom:14px}
.sec-title p{color:var(--muted-onlight);font-size:1.05rem}
.services{background:var(--paper)}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
@media(max-width:900px){.grid3{grid-template-columns:repeat(2,1fr)}}
@media(max-width:620px){.grid3{grid-template-columns:1fr}}
.card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:34px 28px;transition:.25s;display:flex;flex-direction:column}
.card:hover{border-color:var(--blue);box-shadow:0 18px 44px rgba(30,111,217,.14);transform:translateY(-4px)}
.icon{width:52px;height:52px;border-radius:14px;background:var(--blue-soft);display:flex;align-items:center;justify-content:center;margin-bottom:20px}
.icon svg{width:26px;height:26px;stroke:var(--blue);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.card h3{color:var(--navy);font-size:1.2rem;margin-bottom:10px;font-weight:700}
.card p{font-size:.95rem;color:var(--muted-onlight);flex:1}
.card-link{display:inline-block;margin-top:18px;font-weight:700;color:var(--blue);text-decoration:none;font-size:.95rem}
.card-link:hover{text-decoration:underline}
.tag{display:inline-block;margin-top:14px;font-size:.75rem;font-weight:600;color:var(--blue);background:var(--blue-soft);padding:4px 12px;border-radius:999px;align-self:flex-start}

/* Two-col image/text */
.split{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
@media(max-width:900px){.split{grid-template-columns:1fr}}
.split h2{color:var(--navy);font-size:clamp(1.7rem,3vw,2.3rem);font-weight:800;margin-bottom:18px}
.split p{color:var(--muted-onlight);margin-bottom:16px}
.img-frame{border-radius:22px;overflow:hidden;box-shadow:0 24px 60px rgba(10,20,40,.18);border:1px solid var(--line)}
.img-frame img{display:block;width:100%;height:auto}
.img-frame.gif-frame{max-width:480px;margin:0 auto}

/* Dark band */
.dark{background:linear-gradient(180deg,var(--navy),var(--navy-2));color:var(--silver)}
.dark h2{color:#fff}
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:10px}
@media(max-width:900px){.steps{grid-template-columns:repeat(2,1fr)}}
@media(max-width:540px){.steps{grid-template-columns:1fr}}
.step{background:var(--navy-3);border:1px solid var(--line-dark);border-radius:16px;padding:28px 24px;position:relative;transition:.25s}
.step:hover{transform:translateY(-4px);border-color:var(--blue-bright)}
.step .num{width:38px;height:38px;border-radius:50%;background:var(--grad);color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center;margin-bottom:16px;font-size:1rem}
.step h3{color:#fff;font-size:1.05rem;margin-bottom:8px;font-weight:700}
.step p{font-size:.9rem;color:var(--muted)}

/* Stats */
.stats-band{background:var(--grad);padding:0}
.stats{display:grid;grid-template-columns:repeat(4,1fr);text-align:center;padding:56px 0;gap:16px}
@media(max-width:700px){.stats{grid-template-columns:repeat(2,1fr)}}
.stat .n{font-size:2.3rem;font-weight:800;color:#fff}
.stat .l{color:#D6E8FB;font-size:.9rem;font-weight:500}

/* FAQ */
.faq{background:var(--paper)}
.faq-list{max-width:760px;margin:0 auto}
.faq-item{background:#fff;border:1px solid var(--line);border-radius:14px;margin-bottom:14px;overflow:hidden}
.faq-q{width:100%;background:none;border:none;text-align:left;padding:20px 24px;font-size:1.02rem;font-weight:600;color:var(--navy);cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;font-family:inherit}
.faq-q .chev{color:var(--blue);font-size:1.3rem;transition:.25s;flex-shrink:0}
.faq-item.open .faq-q .chev{transform:rotate(45deg)}
.faq-a{max-height:0;overflow:hidden;transition:max-height .3s ease}
.faq-a p{padding:0 24px 22px;color:var(--muted-onlight);font-size:.95rem}

/* Included list */
.included{background:var(--paper)}
.check-list{list-style:none;max-width:760px;margin:0 auto;display:grid;gap:14px}
.check-list li{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 20px 16px 56px;position:relative;color:#33475E;font-size:.98rem}
.check-list li::before{content:"✓";position:absolute;left:20px;top:15px;width:26px;height:26px;border-radius:50%;background:var(--grad);color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center;font-size:.85rem}

/* CTA band */
.cta-band{background:radial-gradient(800px 400px at 50% 0%,rgba(58,155,238,.25),transparent),linear-gradient(180deg,var(--navy),var(--navy-2));color:var(--silver);text-align:center}
.cta-band h2{color:#fff;font-size:clamp(1.7rem,3vw,2.4rem);font-weight:800;margin-bottom:14px}
.cta-band p{max-width:560px;margin:0 auto 30px;color:var(--silver)}
.cta-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}

/* Contact */
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start}
@media(max-width:860px){.contact-grid{grid-template-columns:1fr}}
.contact-info h2{font-size:clamp(1.7rem,3vw,2.2rem);color:var(--navy);font-weight:800;margin-bottom:14px}
.contact-info p{color:var(--muted-onlight);margin-bottom:24px}
.detail{display:flex;gap:14px;align-items:flex-start;margin-bottom:16px;background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:16px 18px}
.detail svg{width:22px;height:22px;stroke:var(--blue);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;flex-shrink:0;margin-top:2px}
.detail div strong{color:var(--navy);display:block;font-size:.95rem}
.detail div span{color:var(--muted-onlight);font-size:.92rem}
.detail a{color:var(--blue);font-weight:600;text-decoration:none}
.detail a:hover{text-decoration:underline}
.note{font-size:.8rem;color:var(--muted-onlight);font-style:italic;margin-top:6px}
form{background:#fff;border:1px solid var(--line);border-radius:18px;padding:34px;box-shadow:0 16px 44px rgba(10,20,40,.08)}
.field{margin-bottom:18px}
.field label{display:block;font-weight:600;color:var(--navy);font-size:.9rem;margin-bottom:6px}
.field input,.field textarea{width:100%;border:1.5px solid var(--line);border-radius:10px;padding:12px 14px;font-size:1rem;font-family:inherit;color:#33475E}
.field input:focus,.field textarea:focus{outline:none;border-color:var(--blue)}
.field textarea{resize:vertical;min-height:120px}
.form-msg{display:none;margin-top:14px;background:var(--blue-soft);border:1px solid rgba(58,155,238,.4);color:var(--blue);padding:12px 16px;border-radius:10px;font-size:.92rem}

/* Footer */
footer{background:var(--navy);color:var(--muted);padding:52px 0 28px;border-top:1px solid var(--line-dark)}
.foot-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:32px;margin-bottom:36px}
@media(max-width:700px){.foot-grid{grid-template-columns:1fr}}
.foot-grid h4{color:#fff;font-size:1rem;margin-bottom:14px;font-weight:700}
.foot-grid ul{list-style:none}
.foot-grid ul li{margin-bottom:8px}
.foot-grid a{color:var(--muted);text-decoration:none;font-size:.92rem}
.foot-grid a:hover{color:#fff}
.foot-brand p{font-size:.92rem;max-width:320px}
.foot-brand img{width:128px;height:auto;border-radius:16px;display:block;margin-bottom:14px;padding:10px;background:#fff}
.foot-logo{color:#fff;font-weight:800;font-size:1.15rem;display:block;margin-bottom:12px}
.foot-logo .accent{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.copy{border-top:1px solid var(--line-dark);padding-top:24px;text-align:center;font-size:.85rem}

/* Reveal on scroll */
.reveal{opacity:0;transform:translateY(26px);transition:opacity .7s ease,transform .7s ease}
.reveal.visible{opacity:1;transform:none}
.reveal[data-d="1"]{transition-delay:.1s}.reveal[data-d="2"]{transition-delay:.2s}
.reveal[data-d="3"]{transition-delay:.3s}.reveal[data-d="4"]{transition-delay:.4s}

.center{text-align:center;margin-top:44px}
.breadcrumb-pad{padding-bottom:0}

@media (prefers-reduced-motion: reduce){
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
  html{scroll-behavior:auto}
  .reveal{opacity:1;transform:none}
  .marquee-track{animation:none}
  .hero::before{display:none}
}
"""

JS = r"""
document.addEventListener('DOMContentLoaded',()=>{
  // Mobile nav
  const burger=document.getElementById('burger');
  if(burger){burger.addEventListener('click',()=>document.body.classList.toggle('nav-open'));}
  document.querySelectorAll('.has-drop > a.drop-toggle').forEach(a=>{
    a.addEventListener('click',e=>{
      if(window.innerWidth<=980){e.preventDefault();a.parentElement.classList.toggle('sub-open');}
    });
  });
  // Scroll reveal
  const io=new IntersectionObserver(es=>es.forEach(e=>{
    if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target);}
  }),{threshold:.12});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
  // Animated counters
  const cio=new IntersectionObserver(es=>es.forEach(e=>{
    if(!e.isIntersecting)return;cio.unobserve(e.target);
    const el=e.target,end=parseFloat(el.dataset.count),suf=el.dataset.suffix||'';
    const t0=performance.now(),dur=1400;
    const tick=t=>{const p=Math.min((t-t0)/dur,1),v=Math.round(end*(1-Math.pow(1-p,3)));
      el.textContent=v+suf;if(p<1)requestAnimationFrame(tick);};
    requestAnimationFrame(tick);
  }),{threshold:.4});
  document.querySelectorAll('[data-count]').forEach(el=>cio.observe(el));
  // FAQ accordion
  document.querySelectorAll('.faq-q').forEach(btn=>{
    btn.addEventListener('click',()=>{
      const item=btn.parentElement,ans=item.querySelector('.faq-a'),open=item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(o=>{o.classList.remove('open');o.querySelector('.faq-a').style.maxHeight=null;});
      if(!open){item.classList.add('open');ans.style.maxHeight=ans.scrollHeight+'px';}
    });
  });
  // Contact form (front-end only)
  const f=document.getElementById('contact-form');
  if(f){f.addEventListener('submit',e=>{
    e.preventDefault();
    if(!f.name.value.trim()||!f.email.value.trim()||!f.phone.value.trim()||!f.message.value.trim()){alert('Please complete all fields before sending.');return;}
    document.getElementById('form-msg').style.display='block';
    f.querySelectorAll('input,textarea').forEach(i=>i.value='');
  });}
});
"""

def head(title, desc, extra=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — IT Green Consulting</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0A1428">
<link rel="icon" type="image/x-icon" href="favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
{extra}</head>
<body>
"""

def nav(active):
    def a(href, label, key):
        cls = ' class="active"' if key == active else ''
        return f'<a href="{href}"{cls}>{label}</a>'
    drop = "".join(f'<a href="{s[2]}">{s[1]}</a>' for s in SERVICES)
    return f"""<nav>
  <div class="container nav-inner">
    <a class="logo" href="index.html" aria-label="IT Green Consulting home">
      <img src="logo-header.png" alt="IT Green Consulting logo">
      IT <span class="accent">Green</span>&nbsp;Consulting
    </a>
    <button class="burger" id="burger" aria-label="Menu"><span></span><span></span><span></span></button>
    <ul class="nav-links">
      <li>{a('index.html','Home','home')}</li>
      <li class="has-drop"><a href="certificate-services.html" class="drop-toggle{' active' if active in [s[0] for s in SERVICES] else ''}">Services</a>
        <div class="drop">{drop}</div></li>
      <li>{a('how-it-works.html','How it works','how')}</li>
      <li>{a('faq.html','FAQ','faq')}</li>
      <li>{a('contact.html','Contact','contact')}</li>
    </ul>
    <div class="nav-cta">
      <a class="nav-phone" href="{PHONE_TEL}">{PHONE}</a>
      <a class="btn btn-sm" href="contact.html">Get in touch</a>
    </div>
  </div>
</nav>
"""

def footer():
    slinks = "".join(f'<li><a href="{s[2]}">{s[1]}</a></li>' for s in SERVICES)
    return f"""<footer>
  <div class="container">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="logo-header.png" alt="IT Green Consulting logo" loading="lazy">
        <span class="foot-logo">IT <span class="accent">Green</span> Consulting</span>
        <p>Energy certificates, rebates and IT support — one partner for greener business.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{slinks}</ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="how-it-works.html">How it works</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="{PHONE_TEL}">{PHONE}</a></li>
        </ul>
      </div>
    </div>
    <div class="copy">© 2026 IT Green Consulting. All rights reserved.</div>
  </div>
</footer>
<script src="site.js"></script>
</body>
</html>
"""

def page_hero(crumbs, eyebrow, h1, lede, img=None, img_alt=""):
    bg = f'<div class="bg" style="background-image:url({img})" role="img" aria-label="{img_alt}"></div>' if img else ""
    return f"""<header class="page-hero">
  {bg}
  <div class="container inner">
    <div class="crumbs">{crumbs}</div>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
  </div>
</header>
"""

def cta_band(title, text):
    return f"""<section class="cta-band">
  <div class="container reveal">
    <h2>{title}</h2>
    <p>{text}</p>
    <div class="cta-btns">
      <a class="btn" href="contact.html">Get in touch</a>
      <a class="btn btn-outline" href="{PHONE_TEL}">Call {PHONE}</a>
    </div>
  </div>
</section>
"""

def service_cards_html():
    cards = []
    for slug, name, href, tag, icon in SERVICES:
        cards.append(f"""<div class="card reveal">
        <div class="icon"><svg viewBox="0 0 24 24"><path d="{icon}"/></svg></div>
        <h3>{name}</h3>
        <p>{CARD_BLURBS[slug]}</p>
        <a class="card-link" href="{href}">Learn more →</a>
        <span class="tag">{tag}</span>
      </div>""")
    return "\n".join(cards)

CARD_BLURBS = {
 "certificate-services": "We create and monetise energy certificates across federal and state schemes — STCs, VEECs, ESCs and PRCs. Our team manages eligibility, compliance and creation from start to finish, then surrenders or sells the certificates in the way that best suits your financial and environmental goals.",
 "energy-rebates": "Rebate processing built for installers. Lodge claims straight from your phone, get real-time compliance checks as you go, and receive fast payment once approved. If you're claiming for the first time, we walk you through every step — so every eligible installation becomes extra income instead of paperwork.",
 "sales": "We provide sales for the installers. Our team sells on your behalf — bundling certificates and rebates into sharper quotes and handling the customer conversations — so you can stay on the tools while the jobs keep coming in.",
 "energy-audits": "Our audits pinpoint where your site is wasting energy and money — then map out the upgrades and certificate opportunities that fix it. Choose the audit that suits you: a live on-site audit, a phone audit, or a desktop audit. You get a clear, prioritised report with real numbers, not jargon.",
 "aggregation": "Pooling certificates across multiple projects and installers means stronger market returns and far simpler administration. We bundle your volumes, manage the trading, and pass the benefits back to you.",
 "it-support": "Managed IT support tailored for trade and energy businesses — devices, email, systems and a responsive helpdesk, including support for the Data Force, Bridgeselect and Alitsy platforms. We keep your technology reliable so you can focus on selling and installing, not troubleshooting.",
 "billing-facility": "Billing handled for you. We generate invoices for completed installs and certificate and rebate income, track payments as they land, and manage the billing admin — so your cash flow stays clear and your books stay tidy.",
}

def build_page(filename, title, desc, active, body):
    html = head(title, desc) + nav(active) + body + footer()
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(html)
    print("wrote", filename, len(html)//1024, "KB")

# ---------------- Service page content (all copy in our own words) ----------------
SERVICE_PAGES = {
 "certificate-services": dict(
  title="Certificate Services", hero_img="img/solar-sunset.webp",
  hero_alt="Solar panel array under a bright blue sky",
  eyebrow="Certificate Services",
  h1="Turn energy upgrades into <span class=\"g\">tradeable value.</span>",
  lede="We create, manage and monetise energy certificates across every major Australian scheme — so your projects earn everything they're entitled to.",
  paras=[
   "Every Australian energy scheme turns eligible activity into tradeable certificates — but the rules, paperwork and timing differ from state to state. IT Green Consulting exists to make that complexity disappear. We work with installers, builders and businesses to identify which certificates a project can generate, then handle the entire creation journey.",
   "Our team starts with a thorough eligibility assessment. We look at your installations, equipment and timelines, and map them against the federal STC scheme, plus state programs including VEECs in Victoria and ESCs and PRCs in New South Wales. If a certificate can legitimately be created, we find it.",
   "From there we manage compliance end to end — documentation, evidence, registration and creation — so nothing gets rejected on a technicality. And once certificates exist, we put them to work: selling them at competitive market rates for maximum financial return, or surrendering them against your sustainability commitments where that matters more.",
   "Whether you're an installer wanting certificate value built into every job, or a business sitting on an upgrade portfolio, we shape the certificate strategy around your goals and keep you informed with clear reporting at every stage.",
  ],
  included=[
   "Scheme eligibility assessments across STC, VEEC, ESC and PRC",
   "End-to-end compliance, documentation and evidence management",
   "Certificate creation, registration and tracking",
   "Monetisation at competitive market rates with prompt settlement",
   "Certificate surrender management for sustainability targets",
   "Clear, regular reporting on every certificate and dollar",
  ],
  steps=[
   ("Assess", "We review your projects and map every certificate opportunity across the schemes that apply."),
   ("Document & verify", "Our compliance team gathers and checks the evidence so creation goes through first time."),
   ("Create", "Certificates are created and registered in your name, ready to sell or surrender."),
   ("Monetise & report", "We trade at strong market rates and report back on every certificate and payment."),
  ],
 ),
 "energy-rebates": dict(
  title="Energy Rebates", hero_img="img/electrician.webp",
  hero_alt="Electrician installing an electrical switchboard",
  eyebrow="Energy Rebates",
  h1="Every eligible install becomes <span class=\"g\">extra income.</span>",
  lede="Installer-friendly rebate processing: lodge claims from your phone, pass compliance checks in real time, and get paid fast.",
  paras=[
   "Rebates only pay out when claims are lodged correctly — and for busy installers, paperwork is the last thing on the list. Our rebate service is built around the way installers actually work: fast, mobile and no-nonsense.",
   "You lodge each claim straight from your phone in minutes. As you submit, real-time compliance checks flag any missing or inconsistent detail before it becomes a rejection, so claims go through cleanly the first time.",
   "Once approved, payments are processed quickly — because rebate money sitting in a queue isn't helping your cash flow. You'll always know where each claim stands with straightforward status updates.",
   "Never claimed before? That's fine. We walk first-timers through the whole process — eligibility, documentation, lodgement — so your very first claim feels as easy as your fiftieth. Every eligible installation turns into extra income instead of admin.",
  ],
  included=[
   "Mobile-friendly claim lodgement in minutes",
   "Real-time compliance checks before submission",
   "Fast payment processing once approved",
   "Step-by-step guidance for first-time claimants",
   "Live claim tracking and status updates",
   "Documentation support for every claim type",
  ],
  steps=[
   ("Sign up", "Register once and we'll set up your installer profile across the relevant schemes."),
   ("Lodge your claim", "Submit from your phone in minutes — photos, details and evidence attached as you go."),
   ("Compliance check", "Real-time checks catch issues instantly so your claim isn't bounced back."),
   ("Get paid", "Approved claims are paid out fast, with a clear record of every dollar."),
  ],
  gif=True,
 ),
 "sales": dict(
  title="Sales", hero_img="img/team.webp",
  hero_alt="Business team collaborating around a table with laptops",
  eyebrow="Sales",
  h1="Sell the <span class=\"g\">incentive</span>, not just the install.",
  lede="We provide sales for the installers — our team sells on your behalf, packaging certificates and rebates into sharp quotes that win work.",
  paras=[
   "Selling takes time — time most installers would rather spend on the tools. That's why our team handles sales on behalf of the installers we partner with, turning your installations and incentive value into signed jobs. And in Australia, every job carries extra value: thousands of dollars in certificates and rebates that most quotes barely mention. That's a missed sale, every time.",
   "We turn that incentive value into a genuine sales advantage for you. Certificates and rebates get structured into your quotes so the customer's out-of-pocket cost is clear, compelling and honest — the kind of number that closes deals.",
   "Beyond the numbers, we bring the words: plain-English explainers, one-page leave-behinds and answers to the curly questions customers ask about rebates and certificates. Whoever is talking to your customer, they do it with confidence, not guesswork.",
   "And because we're handling the compliance behind the scenes, every promise made on your behalf is one you can keep. Incentives become a growth engine for your business instead of a risk.",
  ],
  included=[
   "Rebate-inclusive quote structuring that wins on price",
   "Plain-English customer explainers for incentives",
   "Sales collateral and one-page leave-behinds",
   "Team training on certificates and rebate talking points",
   "Ongoing support as schemes and values change",
  ],
  steps=[
   ("Understand your offer", "We learn your products, pricing and typical customers."),
   ("Package the incentives", "Certificates and rebates are built into sharp, honest quotes."),
   ("Sell on your behalf", "Our team presents the quote, answers customer questions and follows up until it's signed."),
   ("Win more jobs", "Track the uplift as incentive-led quotes convert at a higher rate."),
  ],
 ),
 "energy-audits": dict(
  title="Energy Audits", hero_img="img/engineer.webp",
  hero_alt="Consultant reviewing data on a computer monitor",
  eyebrow="Energy Audits",
  h1="Find the waste. <span class=\"g\">Fix it with numbers.</span>",
  lede="Professional energy audits that pinpoint where your site loses money — and which upgrades pay back fastest.",
  paras=[
   "You can't fix what you haven't measured. Our energy audits give you a clear, evidence-based picture of exactly where your site is wasting energy — and what each fix is worth in dollars, payback time and certificate value.",
   "We review the big-ticket areas: lighting, heating and cooling, hot water, refrigeration and process equipment, plus how and when your site actually uses power. The analysis goes beyond the obvious to find the savings hiding in operating patterns.",
   "The result is a prioritised report written in plain English: which upgrades to do first, what they'll cost, how fast they pay back, and which certificates or rebates each one unlocks. No jargon, no padding — just decisions you can act on.",
   "For many clients, the audit pays for itself many times over through the first round of identified savings. And because we can also create the certificates and process the rebates, the path from report to realised savings is a short one.",
  ],
  included=[
   "Your choice of live audit, phone audit or desktop audit",
   "On-site or remote energy review of your facility",
   "Lighting, HVAC, hot water, refrigeration and equipment analysis",
   "Usage-pattern review to find hidden waste",
   "Upgrades prioritised by cost, payback and savings",
   "Certificate and rebate opportunities mapped to each upgrade",
   "Plain-English report with real numbers",
  ],
  steps=[
   ("Discover", "We gather your bills, walk the site and understand how you use energy."),
   ("Analyse", "Our team models consumption and pinpoints the highest-value fixes."),
   ("Report", "You get a prioritised, plain-English report with costs and paybacks."),
   ("Act", "We help you implement — and create the certificates the upgrades earn."),
  ],
  audit_types=True,
 ),
 "aggregation": dict(
  title="Aggregation", hero_img="img/solar-aerial.webp",
  hero_alt="Aerial view of solar panels in a field",
  eyebrow="Aggregation",
  h1="Small parcels. <span class=\"g\">Big-market prices.</span>",
  lede="We pool certificates across projects and installers to unlock stronger prices — with one point of contact.",
  paras=[
   "Small parcels of certificates trade at a discount. It's simple market mechanics: buyers pay more for volume, and individual installers rarely have enough to command it. Aggregation flips that equation in your favour.",
   "We pool certificate volumes across many projects and installers, then trade the combined parcels professionally. The result is typically stronger pricing than you'd achieve alone — and the benefit flows back to you.",
   "Administration shrinks too. Instead of tracking markets, counterparties and settlement yourself, you deal with a single point of contact. We handle the trading, the paperwork and the timing; you see clear reporting and prompt settlement.",
   "Aggregation suits installers with steady certificate flow, businesses with multi-site upgrades, and partners who'd rather focus on their core work than the certificate market. Bring the volume — we'll bring the market access.",
  ],
  included=[
   "Certificate volume pooling across projects and installers",
   "Professional trading for stronger market prices",
   "A single point of contact for everything",
   "Transparent reporting on volumes, prices and settlements",
   "Prompt settlement once trades complete",
   "Far less administration for your team",
  ],
  steps=[
   ("Pool", "Your certificates join a larger aggregated volume."),
   ("Trade", "We trade professionally for the best achievable market price."),
   ("Settle", "Funds are settled promptly with a full breakdown."),
   ("Report", "Clear reporting on every parcel, price and payment."),
  ],
 ),
 "it-support": dict(
  title="IT Support", hero_img="img/it-team.webp",
  hero_alt="Overhead view of laptops and devices on an office desk",
  eyebrow="IT Support",
  h1="Technology that <span class=\"g\">keeps up</span> with your team.",
  lede="Managed IT support built for trade and energy businesses — devices, email, systems and a helpdesk that answers.",
  paras=[
   "Your tools should never slow down a job. But for most trade and energy businesses, IT is a patchwork — a laptop here, a personal email there, and nobody to call when something breaks at 7am before a big install day.",
   "We provide managed IT support shaped around the way your business actually operates: in the office, on the road and on site. Devices set up properly, email and collaboration tools that just work, and systems kept secure and backed up.",
   "When something does go wrong, you get a responsive helpdesk — real help from people who understand your business, not a ticket queue that goes quiet. Most issues are resolved fast, and we keep you in the loop the whole way.",
   "As you grow, your IT grows with you: onboarding new staff, adding devices, tightening security. One partner for the whole journey, so technology becomes something you never have to think about.",
  ],
  included=[
   "Responsive helpdesk with fast resolution times",
   "Device setup, management and troubleshooting",
   "Business email and collaboration tools",
   "Security, backups and system maintenance",
   "New-staff onboarding and device provisioning",
   "Support for the Data Force, Bridgeselect and Alitsy platforms",
   "Straightforward plans that scale with your team",
  ],
  steps=[
   ("Assess your setup", "We review your devices, email, systems and pain points."),
   ("Stabilise", "Quick wins first: fix what's broken and secure what's exposed."),
   ("Manage", "Ongoing maintenance, monitoring and updates handled for you."),
   ("Support", "A helpdesk that's there when you need it — on site or remote."),
  ],
  platforms=True,
 ),
 "billing-facility": dict(
  title="Billing Facility", hero_img="img/team.webp",
  hero_alt="Business team collaborating around a table with laptops",
  eyebrow="Billing Facility",
  h1="Invoices out. Payments tracked. <span class=\"g\">Admin handled.</span>",
  lede="A billing facility for installers and partners — we raise the invoices, track the payments and manage the billing admin, so you don't have to.",
  paras=[
   "Billing is essential — and for busy installers, it's also the first thing that slips. Invoices go out late, payments aren't chased, and certificate and rebate income gets muddled in with everything else. Our billing facility takes that whole load off your desk.",
   "We generate invoices for your completed installs, and for the certificate and rebate income your jobs earn, so every dollar you're owed is documented and sent promptly. Professional, error-free invoices go out on time, every time.",
   "Then we track what's been paid and what hasn't. You get a clear view of outstanding amounts and incoming payments, without having to reconcile spreadsheets or chase paperwork yourself.",
   "The result is cleaner cash flow and tidier books — and hours of admin handed back to your week. Pair it with our certificate, rebate and aggregation services and your entire back office runs through one partner.",
  ],
  included=[
   "Invoice generation for completed installs",
   "Billing for certificate and rebate income",
   "Payment tracking — know what's paid and what's outstanding",
   "Billing administration handled end to end",
   "Clear billing reports for your records",
   "One partner across billing, certificates and rebates",
  ],
  steps=[
   ("Send us the job", "Pass us the completed install and billing details — we take it from there."),
   ("We invoice", "Professional invoices are generated and sent promptly."),
   ("Payments tracked", "We track payments as they land and flag anything outstanding."),
   ("You stay informed", "Clear reports show exactly what's been billed and what's been paid."),
  ],
 ),
}

FAQS = [
 ("Which certificate schemes do you work with?",
  "We work across the major federal and state schemes, including STCs at the federal level, plus VEECs in Victoria and ESCs and PRCs in New South Wales. If you're unsure which schemes apply to your project, we'll assess it for you at no cost."),
 ("I'm an installer claiming for the first time. Can you help?",
  "Absolutely — that's exactly who our rebate service is built for. We guide first-timers through every step, from eligibility to documentation to claim lodgement, so you avoid the common mistakes that delay payment."),
 ("How fast are payments processed?",
  "We prioritise fast turnaround: correctly lodged claims move through quickly, and certificates are monetised at competitive market rates with clear, prompt payment once settled. We'll give you a realistic timeline for your specific claim when we start."),
 ("What does an energy audit involve?",
  "We review your site's energy use — lighting, HVAC, hot water, equipment and more — and identify where you're overspending. The report prioritises upgrades by payback, and flags any certificate or rebate opportunities each upgrade unlocks."),
 ("How does aggregation benefit me?",
  "By pooling certificates across many projects and installers, we trade larger volumes that typically achieve stronger prices than small individual parcels — and you deal with one point of contact instead of complex market admin."),
 ("What IT support do you offer?",
  "We support trade and energy businesses with everyday IT: setting up and managing devices and email, keeping systems secure and running, and a helpdesk for when something breaks. Plans can be shaped around the size of your team."),
 ("Do you work with clients outside Victoria and New South Wales?",
  "Yes. The federal STC scheme applies Australia-wide, and we also cover state programs in Victoria and New South Wales. Wherever you're based, we'll map exactly which schemes your projects qualify for."),
 ("How do we get started?",
  "Call us on 0415 271 956 or send a message through the contact form. We'll start with a free initial conversation to understand your business or project, then lay out the schemes, services and next steps that apply to you."),
]

def faq_items_html(items, reveal=False):
    out = []
    for i, (q, a_) in enumerate(items):
        out.append(f"""<div class="faq-item{' reveal' if reveal else ''}"{' data-d="'+str(i%4)+'"' if reveal else ''}>
        <button class="faq-q">{q}<span class="chev">+</span></button>
        <div class="faq-a"><p>{a_}</p></div>
      </div>""")
    return "\n".join(out)

def steps_html(steps, reveal=False):
    out = []
    for i, (t, p) in enumerate(steps):
        out.append(f"""<div class="step{' reveal' if reveal else ''}"{' data-d="'+str(i)+'">' if reveal else '>'}
        <div class="num">{i+1}</div>
        <h3>{t}</h3>
        <p>{p}</p>
      </div>""")
    return "\n".join(out)

def service_page(slug):
    d = SERVICE_PAGES[slug]
    crumbs = f'<a href="index.html">Home</a> · <a href="index.html#services">Services</a> · {d["title"]}'
    body = page_hero(crumbs, d["eyebrow"], d["h1"], d["lede"], d["hero_img"], d["hero_alt"])
    paras = "".join(f"<p>{p}</p>" for p in d["paras"])
    body += f"""<section>
  <div class="container split">
    <div class="reveal">
      <h2>What this service does for you</h2>
      {paras}
    </div>
    <div class="img-frame reveal" data-d="1">
      <img src="{d['hero_img']}" alt="{d['hero_alt']}" loading="lazy">
    </div>
  </div>
</section>
"""
    if d.get("gif"):
        body += """<section class="services">
  <div class="container split">
    <div class="img-frame gif-frame reveal">
      <img src="img/battery.gif" alt="Animated diagram showing renewable energy flowing into battery storage" loading="lazy">
    </div>
    <div class="reveal" data-d="1">
      <h2>See the flow: energy in, income out</h2>
      <p>Every rebate starts with eligible activity — a battery installed, a hot water system upgraded, a building made more efficient. Our job is to make sure the value locked inside that activity flows back to you as fast as possible.</p>
      <p>Lodge the claim, pass the checks, get paid. That's the whole journey, and we manage every step of it with you.</p>
      <a class="btn" href="contact.html">Start your first claim</a>
    </div>
  </div>
</section>
"""
    if d.get("audit_types"):
        body += """<section>
  <div class="container">
    <div class="sec-title reveal">
      <h2>Three ways to get audited</h2>
      <p>Pick the audit format that fits your site, your schedule and your budget.</p>
    </div>
    <div class="grid3">
      <div class="card reveal">
        <h3>Live Audit</h3>
        <p>Our auditor attends your site in person, inspects equipment and usage first-hand, and captures the detail only an on-site visit can. The most thorough option for larger or more complex sites.</p>
        <span class="tag">On-site · In person</span>
      </div>
      <div class="card reveal" data-d="1">
        <h3>Phone Audit</h3>
        <p>A guided audit conducted over the phone. We walk you through your site, equipment and bills step by step — a fast, convenient option when a site visit isn't practical.</p>
        <span class="tag">Remote · Guided</span>
      </div>
      <div class="card reveal" data-d="2">
        <h3>Desktop Audit</h3>
        <p>A document and data-based audit with no site visit at all. We analyse your energy bills, usage data and equipment records to identify savings and certificate opportunities.</p>
        <span class="tag">Documents · No site visit</span>
      </div>
    </div>
  </div>
</section>
"""
    if d.get("platforms"):
        body += """<section>
  <div class="container">
    <div class="sec-title reveal">
      <h2>Platforms we support</h2>
      <p>Alongside everyday IT support, we also provide support for these platforms used across the energy industry.</p>
    </div>
    <div class="grid3">
      <div class="card reveal">
        <h3>Data Force</h3>
        <p>Day-to-day support for Data Force users — account access, troubleshooting and keeping your team productive on the platform.</p>
        <span class="tag">Supported platform</span>
      </div>
      <div class="card reveal" data-d="1">
        <h3>Bridgeselect</h3>
        <p>Setup help, issue resolution and ongoing user support for Bridgeselect, so your team can get on with the job.</p>
        <span class="tag">Supported platform</span>
      </div>
      <div class="card reveal" data-d="2">
        <h3>Alitsy</h3>
        <p>Onboarding assistance, troubleshooting and general support for Alitsy users across your business.</p>
        <span class="tag">Supported platform</span>
      </div>
    </div>
  </div>
</section>
"""
    inc = "".join(f"<li>{i}</li>" for i in d["included"])
    body += f"""<section class="included">
  <div class="container">
    <div class="sec-title reveal">
      <h2>What's included</h2>
      <p>Everything handled — nothing left for you to chase.</p>
    </div>
    <ul class="check-list">{inc}</ul>
  </div>
</section>
<section class="dark">
  <div class="container">
    <div class="sec-title reveal">
      <h2 style="color:#fff">How it works</h2>
      <p style="color:#93A5B8">A simple path from enquiry to outcome.</p>
    </div>
    <div class="steps">{steps_html(d['steps'], True)}</div>
    <p class="center reveal" style="color:#93A5B8;max-width:640px;margin-left:auto;margin-right:auto">Partner perk: depending on the volume of jobs you run, you'll also have a <strong style="color:#fff">dedicated representative</strong> who knows your business and keeps everything moving.</p>
    <div class="center reveal"><a class="btn" href="contact.html">Talk to us about {d['title'].lower()}</a></div>
  </div>
</section>
"""
    body += cta_band("Ready when you are.",
                     f"Tell us about your project and we'll show you exactly what {d['title'].lower()} can deliver for your business.")
    return body

# ---------------- Home ----------------
HOME_STEPS = [
 ("Get in touch", "Tell us about your business or project — installer, business owner or partner. We'll map out which schemes and services apply to you."),
 ("We handle the detail", "Eligibility checks, audits, documentation and compliance — our team manages the whole process so nothing slips through."),
 ("Certificates & claims created", "We create your certificates and lodge rebate claims correctly the first time, with real-time checks along the way."),
 ("You get paid", "Certificates are monetised at strong market rates and payments are processed fast — with clear reporting on every dollar."),
]

def home():
    marquee_items = ["STC", "VEEC", "ESC", "PRC"]
    spans = "".join(f'<span>{c}</span><span class="dot">•</span>' for c in marquee_items)
    marquee = f'<ul class="marquee-track"><li style="display:flex;gap:56px">{spans}</li><li style="display:flex;gap:56px" aria-hidden="true">{spans}</li></ul>'
    body = f"""<header class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow">Energy certificates · Rebates · IT support</span>
      <h1>Energy certificates, rebates and IT support — <span class="g">one partner</span> for greener business.</h1>
      <p class="lede">IT Green Consulting helps Australian businesses and installers turn clean-energy upgrades into real income. We handle the paperwork, compliance and certificates end to end — plus the IT that keeps your business running.</p>
      <div class="hero-ctas">
        <a class="btn" href="index.html#services">Explore services</a>
        <a class="btn btn-outline" href="{PHONE_TEL}">Call {PHONE}</a>
      </div>
    </div>
    <div class="hero-art">
      <img class="hero-logo" src="logo.png" alt="IT Green Consulting — ITGC logo">
      <div class="card-float"><span class="pulse"></span>Claim approved · <strong>Fast payment</strong></div>
    </div>
  </div>
</header>
<div class="marquee" aria-hidden="true">{marquee}</div>

<section class="services" id="services">
  <div class="container">
    <div class="sec-title reveal">
      <h2 id="services-h">What we do</h2>
      <p>Seven connected services that take an energy project from idea to income — with the technology support to keep your business humming.</p>
    </div>
    <div class="grid3">
      {service_cards_html()}
    </div>
  </div>
</section>

<section>
  <div class="container split">
    <div class="img-frame reveal">
      <img src="img/solar-field.webp" alt="Rows of solar panels in a green field under a blue sky" loading="lazy">
    </div>
    <div class="reveal" data-d="1">
      <h2>Built for Australia's energy schemes</h2>
      <p>From rooftop solar and batteries to lighting, hot water and commercial upgrades, eligible activity is happening on job sites every day — value that's often left on the table because the paperwork feels too hard.</p>
      <p>We make it simple. One partner handles certificates, rebates, audits and aggregation, backed by the IT support that keeps your business running smoothly.</p>
      <a class="btn" href="how-it-works.html">See how it works</a>
    </div>
  </div>
</section>

<section class="services">
  <div class="container">
    <div class="sec-title reveal">
      <h2>Why partner with us</h2>
      <p>More than a processor — a partner set up around how your business actually runs.</p>
    </div>
    <div class="grid3">
      <div class="card reveal">
        <h3>A dedicated representative</h3>
        <p>Depending on the volume of jobs you run, you'll have a dedicated representative who knows your business, your projects and your priorities — one person to call, not a call centre.</p>
        <span class="tag">Matched to your job volume</span>
      </div>
      <div class="card reveal" data-d="1">
        <h3>Everything under one roof</h3>
        <p>Certificates, rebates, sales, audits, aggregation, IT support and billing — handled by one team that talks to each other, so nothing falls between providers.</p>
        <span class="tag">One partner · Seven services</span>
      </div>
      <div class="card reveal" data-d="2">
        <h3>Fast, transparent payments</h3>
        <p>Claims checked in real time, certificates traded at strong market rates, and clear reporting on every dollar — so you always know what's coming and when.</p>
        <span class="tag">Clear reporting</span>
      </div>
    </div>
  </div>
</section>

<div class="stats-band">
  <div class="container stats">
    <div class="stat"><div class="n" data-count="4">0</div><div class="l">Certificate types covered</div></div>
    <div class="stat"><div class="n" data-count="7">0</div><div class="l">Integrated services</div></div>
    <div class="stat"><div class="n" data-count="1">0</div><div class="l">Partner for the whole journey</div></div>
    <div class="stat"><div class="n" data-count="100" data-suffix="%">0</div><div class="l">Compliance handled for you</div></div>
  </div>
</div>

<section class="dark">
  <div class="container">
    <div class="sec-title reveal">
      <h2 style="color:#fff">How it works</h2>
      <p style="color:#93A5B8">From your first enquiry to money in your account — a simple, transparent path.</p>
    </div>
    <div class="steps">{steps_html(HOME_STEPS, True)}</div>
    <div class="center reveal"><a class="btn" href="how-it-works.html">Read the full process</a></div>
  </div>
</section>

<section class="faq">
  <div class="container">
    <div class="sec-title reveal">
      <h2>Frequently asked questions</h2>
      <p>Quick answers to the things people ask us most.</p>
    </div>
    <div class="faq-list">{faq_items_html(FAQS[:3], True)}</div>
    <div class="center reveal"><a class="btn" href="faq.html">See all FAQs</a></div>
  </div>
</section>
"""
    body += cta_band("Let's talk about your next project",
                     "Whether it's a single installation or a portfolio of projects, we'll show you the path to the best return.")
    build_page("index.html", "Energy Certificates, Rebates & IT Support",
               "IT Green Consulting helps Australian businesses turn energy upgrades into income — certificate creation, rebate processing, audits, aggregation, sales, billing and managed IT support.",
               "home", body)

def how_page():
    crumbs = '<a href="index.html">Home</a> · How it works'
    body = page_hero(crumbs, "How it works", "Four simple steps from enquiry to <span class=\"g\">income.</span>",
                     "No jargon, no chasing paperwork. Here's exactly what happens when you work with us.",
                     "img/ev-charging.webp", "Electric vehicle charging plug connected to a car")
    details = [
     ("Get in touch", "It starts with a conversation. Tell us about your business or project — whether you're an installer doing dozens of jobs a week, a business planning upgrades, or a partner looking to grow. We'll map out which schemes, services and incentives apply to you, and give you a clear picture of the value on the table."),
     ("We handle the detail", "From here, the process is off your plate. We run eligibility checks, conduct audits where needed, gather and verify documentation, and manage compliance across every relevant scheme. This is where claims usually fall over — and where our team earns its keep."),
     ("Certificates & claims created", "With documentation verified, we create your certificates and lodge rebate claims correctly the first time. Real-time compliance checks run throughout, so issues surface instantly rather than weeks later as rejections."),
     ("You get paid", "Certificates are monetised at strong market rates and rebate payments processed fast. You receive clear reporting on every certificate, every claim and every dollar — so you always know exactly what came back and why."),
    ]
    steps = "".join(f"""<div class="step reveal" data-d="{i}">
        <div class="num">{i+1}</div>
        <h3>{t}</h3>
        <p>{p}</p>
      </div>""" for i, (t, p) in enumerate(details))
    body += f"""<section class="dark">
  <div class="container">
    <div class="steps">{steps}</div>
  </div>
</section>
<section>
  <div class="container split">
    <div class="reveal">
      <h2>What you don't have to do</h2>
      <p>You don't need to study scheme rules, chase missing documents, argue with assessors or watch certificate markets. That's our job — and we've built the process so you can focus on yours.</p>
      <p>All you need is a project and a phone. Call us on {PHONE} and we'll take it from there.</p>
      <a class="btn" href="contact.html">Start step one</a>
    </div>
    <div class="img-frame reveal" data-d="1">
      <img src="img/solar-field.webp" alt="Rows of solar panels in a green field under a blue sky" loading="lazy">
    </div>
  </div>
</section>
"""
    body += cta_band("Ready to start?", "The first conversation is free — and we'll tell you honestly what your project is worth.")
    build_page("how-it-works.html", "How It Works",
               "The four-step process IT Green Consulting uses to turn energy upgrades into certificates, rebates and income.",
               "how", body)

def faq_page():
    crumbs = '<a href="index.html">Home</a> · FAQ'
    body = page_hero(crumbs, "FAQ", "Questions? <span class=\"g\">Answered.</span>",
                     "Everything people usually ask before working with us. Still curious? Call us on " + PHONE + ".")
    body += f"""<section class="faq">
  <div class="container">
    <div class="faq-list">{faq_items_html(FAQS, True)}</div>
  </div>
</section>
"""
    body += cta_band("Still have a question?", "Call us or send a message — we're happy to talk through your specific project.")
    build_page("faq.html", "FAQ",
               "Frequently asked questions about energy certificates, rebates, audits, aggregation and IT support from IT Green Consulting.",
               "faq", body)

def contact_page():
    crumbs = '<a href="index.html">Home</a> · Contact'
    body = page_hero(crumbs, "Contact", "Let's talk about <span class=\"g\">your next project.</span>",
                     "Whether it's a single installation or a portfolio of projects, tell us what you're working on and we'll show you the path to the best return.")
    body += f"""<section>
  <div class="container contact-grid">
    <div class="contact-info reveal">
      <h2>Get in touch</h2>
      <p>Call us, or send a message and we'll get back to you promptly.</p>
      <div class="detail">
        <svg viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.13.96.36 1.9.7 2.8a2 2 0 0 1-.45 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.45c.9.34 1.84.57 2.8.7A2 2 0 0 1 22 16.9z"/></svg>
        <div><strong>Phone</strong><a href="{PHONE_TEL}">{PHONE}</a></div>
      </div>
      <div class="detail">
        <svg viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 7l-10 6L2 7"/></svg>
        <div><strong>Email</strong><span>{EMAIL}</span></div>
      </div>
      <div class="detail">
        <svg viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        <div><strong>Dedicated representative</strong><span>Partners who run regular job volume get a dedicated representative — your own point of contact, matched to the volume of jobs you run.</span></div>
      </div>
      <p class="note">Email above is a placeholder — real email coming soon.</p>
    </div>
    <form id="contact-form" class="reveal" data-d="1" novalidate>
      <div class="field">
        <label for="name">Name</label>
        <input id="name" name="name" type="text" placeholder="Your full name" required>
      </div>
      <div class="field">
        <label for="email">Email</label>
        <input id="email" name="email" type="email" placeholder="you@example.com" required>
      </div>
      <div class="field">
        <label for="phone">Phone</label>
        <input id="phone" name="phone" type="tel" placeholder="04XX XXX XXX" required>
      </div>
      <div class="field">
        <label for="message">Message</label>
        <textarea id="message" name="message" placeholder="Tell us about your project or enquiry…" required></textarea>
      </div>
      <button class="btn" type="submit" style="width:100%">Send message</button>
      <div class="form-msg" id="form-msg">Thanks — your message has been noted. (Form backend coming soon; we'll confirm the real email shortly.)</div>
    </form>
  </div>
</section>
"""
    build_page("contact.html", "Contact",
               "Contact IT Green Consulting about certificates, rebates, audits, aggregation or IT support. Call " + PHONE + ".",
               "contact", body)

def main():
    with open(os.path.join(OUT, "styles.css"), "w") as f:
        f.write(CSS.strip() + "\n")
    with open(os.path.join(OUT, "site.js"), "w") as f:
        f.write(JS.strip() + "\n")
    print("wrote styles.css, site.js")
    home()
    for slug, *_ in SERVICES:
        d = SERVICE_PAGES[slug]
        build_page(slug + ".html", d["title"],
                   d["lede"], slug, service_page(slug))
    how_page()
    faq_page()
    contact_page()

if __name__ == "__main__":
    main()
