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
