import './style.css';
const HEROES=['Janeway','Tuvok'];
const heroCards={
Janeway:['captains_prerogative','command_training','counterpoint','determination','fire_phasers_ii','fire_phasers_iii','reprimanded','resolve','set_to_kill','shields_up_ii','shields_up_iii','shore_leave_ii','tactical_exercises_ii','theres_coffee_in_that_nebula'],
Tuvok:['calculated_opening','kal_toh','kolinahr_discipline','kolinar_ii','my_mind_to_your_mind','my_thoughts_to_your_thoughts','nerve_pinch_ii','nerve_pinch_iii','return_fire_ii','return_fire_iii','security_protocols','tactical_precision_ii','tactical_recalibration','vulcan_composure']};
const shared=['better_d','buh_bye','double_up','get_that_outta_here','getting_paid','helping_hand','not_this_time','one_more_time','samesies','six-it','so_wild','tip_it','transference','triple_up','try_try_again','twice_as_wild','vegas_baby','what_status_effects'];
const upgrades={Janeway:{fire_phasers_ii:'Fire Phasers',fire_phasers_iii:'Fire Phasers',shields_up_ii:'Shields Up',shields_up_iii:'Shields Up',shore_leave_ii:'Shore Leave',tactical_exercises_ii:'Tactical Exercises'},Tuvok:{kolinar_ii:'Kolinar',nerve_pinch_ii:'Nerve Pinch',nerve_pinch_iii:'Nerve Pinch',return_fire_ii:'Return Fire',return_fire_iii:'Return Fire',tactical_precision_ii:'Tactical Precision'}};
const tokens={Janeway:{Coffee:0,'Command Codes':0,Reprimand:0},Tuvok:{Logic:0,'Mind Meld':0,Targeted:0,Protect:0}};
const root=import.meta.env.BASE_URL+'assets/';
const boardSlots={Janeway:['fire-phasers','shore-leave','tactical-exercises','command-protocol','do-it','red-alert','get-off-my-ship','shields-up','punch-your-way-through'],Tuvok:['nerve-pinch','meditate','kolinar','combat-drill','measured-response','tactical-precision','final-calculation','return-fire','logical-outcome']};
let assetInstance=0;
function scopeSvgDefinitions(svg){
 const prefix='asset-'+(++assetInstance)+'-';
 const ids=new Map([...svg.querySelectorAll('defs [id]')].map(node=>[node.id,prefix+node.id]));
 svg.querySelectorAll('[id]').forEach(node=>{if(ids.has(node.id))node.id=ids.get(node.id)});
 const replaceUrls=value=>value.replace(/url\(\s*(["']?)#([^\s)"']+)\1\s*\)/g,(match,quote,id)=>ids.has(id)?'url(#'+ids.get(id)+')':match);
 svg.querySelectorAll('*').forEach(node=>{
  for(const attr of [...node.attributes]){
   let value=replaceUrls(attr.value);
   if(attr.localName==='href'&&value.startsWith('#')&&ids.has(value.slice(1)))value='#'+ids.get(value.slice(1));
   if(value!==attr.value)node.setAttributeNS(attr.namespaceURI,attr.name,value);
  }
  if(node.localName==='style')node.textContent=replaceUrls(node.textContent);
 });
}
async function inlineSvg(url,container,modify){try{const response=await fetch(url);if(!response.ok)throw Error('Asset '+response.status);const source=await response.text();const doc=new DOMParser().parseFromString(source,'image/svg+xml');const svg=doc.documentElement;if(svg.localName!=='svg')throw Error('Invalid SVG');svg.querySelectorAll('image').forEach(img=>{const href=img.getAttribute('href')||img.getAttribute('xlink:href');if(href&&!href.startsWith('data:')){const absolute=new URL(href,new URL(url,location.href)).pathname;img.setAttribute('href',absolute);img.setAttributeNS('http://www.w3.org/1999/xlink','href',absolute)}});svg.querySelectorAll('style').forEach(style=>{
 style.textContent=style.textContent.replace(/url\(\s*(["']?)(.*?)\1\s*\)/g,(match,quote,value)=>{
  const ref=value.trim();
  if(!ref||/^(#|data:|https?:|blob:|\/)/i.test(ref))return match;
  return 'url("'+new URL(ref,new URL(url,location.href)).href+'")';
 });
});scopeSvgDefinitions(svg);svg.removeAttribute('width');svg.removeAttribute('height');container.replaceChildren(document.importNode(svg,true));await document.fonts.ready;if(modify)modify(container.firstChild)}catch(err){container.textContent='Unable to load art: '+err.message;console.error(err)}}const $=s=>document.querySelector(s);
function title(s){return s.replaceAll('_',' ').replace(/\b\w/g,c=>c.toUpperCase())}
function img(card){return root+(card.hero==='Shared'?'Shared':'Heroes/'+card.hero)+'/cards/'+card.id+'.svg'}
function face(hero,n){return root+'Heroes/'+hero+'/icons/die_'+n+'.svg'}
function shuffle(a){a=[...a];for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
function newGame(hero){return {hero,dice:[1,2,3,4,5].map(()=>({value:1,locked:false})),deck:shuffle([...shared.map(id=>({id,hero:'Shared'})),...heroCards[hero].map(id=>({id,hero}))]),hand:[],discard:[],upgrades:{},health:50,cp:2,tokens:{...tokens[hero]},peek:0,view:'board'}}
let state;try{state=JSON.parse(localStorage.getItem('voyager-playtest-v1'))}catch{}if(!state||!HEROES.includes(state.hero))state=newGame('Janeway');
function save(){localStorage.setItem('voyager-playtest-v1',JSON.stringify(state))}
function action(fn){fn();save();render()}
function button(label,fn,cls=''){const b=document.createElement('button');b.textContent=label;b.className=cls;b.onclick=fn;return b}
function el(tag,cls,text){const x=document.createElement(tag);if(cls)x.className=cls;if(text!==undefined)x.textContent=text;return x}
function cardNode(c){const x=el('div','card');const pic=el('div','svg-art');x.append(pic);inlineSvg(img(c),pic);x.append(el('small','',title(c.id)));return x}
function render(){const app=$('#app');app.replaceChildren();const header=el('header');header.append(el('h1','','Voyager Dice Throne'));const sel=el('select');for(const h of HEROES){const o=el('option','',h);o.value=h;sel.append(o)}sel.value=state.hero;sel.onchange=()=>{if(confirm('Start a new '+sel.value+' session?'))action(()=>state=newGame(sel.value));else sel.value=state.hero};header.append(sel,button('View Leaflet',showLeaflet,'primary'),button('Inspect deck',()=>renderInspection()),button('Reset session',()=>{if(confirm('Reset all progress for '+state.hero+'?'))action(()=>state=newGame(state.hero))}));app.append(header);
const main=el('main','play-layout');app.append(main);for(const [name,draw] of [['resources-pane',renderResources],['dice-pane',renderDice],['board-pane',renderBoard],['cards-pane',renderCards]]){const pane=el('section','play-pane '+name);main.append(pane);draw(pane)}
}
function showLeaflet(){
 const overlay=el('div','card-overlay leaflet-overlay');
 overlay.setAttribute('role','dialog');overlay.setAttribute('aria-modal','true');
 overlay.setAttribute('aria-label',state.hero+' leaflet');
 const panel=el('div','leaflet-detail');
 const finish=()=>{overlay.remove();document.removeEventListener('keydown',onKeyDown)};
 const close=button('Close ×',finish,'detail-close');
 const picture=el('div','leaflet-svg');
 panel.append(close,picture);overlay.append(panel);
 inlineSvg(root+'Heroes/'+state.hero+'/leaflet.svg',picture);
 overlay.onclick=e=>{if(e.target===overlay)finish()};
 const onKeyDown=e=>{if(e.key==='Escape')finish()};
 document.addEventListener('keydown',onKeyDown);document.body.append(overlay);close.focus();
}
function renderInspection(){const app=$('#app');app.replaceChildren();const header=el('header','inspection-header');header.append(el('h1','','Deck inspection — '+state.hero),button('Back to play',render,'primary'));app.append(header);app.append(el('p','hint','Hero-specific card reference only (14 cards). Shared standard cards are excluded. Inspection does not change the game. Tap a card to enlarge it.'));const grid=el('div','inspection-grid');const all=heroCards[state.hero].map(id=>({id,hero:state.hero}));all.forEach(card=>{const tile=button('',()=>showCardDetail(card),'inspection-tile');tile.append(cardNode(card));grid.append(tile)});app.append(grid)}
function showCardDetail(card){const overlay=el('div','card-overlay');overlay.setAttribute('role','dialog');overlay.setAttribute('aria-modal','true');overlay.setAttribute('aria-label',title(card.id));const panel=el('div','card-detail');panel.append(button('Close ×',()=>overlay.remove(),'detail-close'));const pic=el('div','detail-svg');inlineSvg(img(card),pic);panel.append(pic,el('h3','',title(card.id)));overlay.append(panel);overlay.onclick=e=>{if(e.target===overlay)overlay.remove()};document.body.append(overlay)}
function renderDice(main){main.append(el('h2','','Dice tray'));const tray=el('div','dice-tray');state.dice.forEach((d,i)=>{const item=el('div','die '+(d.locked?'locked':''));const pic=el('div','die-face');inlineSvg(face(state.hero,d.value),pic);pic.onclick=()=>{const n=prompt('Set die '+(i+1)+' to a number (1–6)',d.value);if(n!==null&&Number.isInteger(+n)&&+n>=1&&+n<=6)action(()=>state.dice[i].value=+n)};item.append(pic,el('span','',String(d.value)),button(d.locked?'Unlock':'Keep',()=>action(()=>state.dice[i].locked=!d.locked)));tray.append(item)});main.append(tray);const controls=el('div','controls');controls.append(button('Roll unlocked dice',()=>action(()=>state.dice.forEach(d=>{if(!d.locked)d.value=1+Math.floor(Math.random()*6)}))),button('Unlock all',()=>action(()=>state.dice.forEach(d=>d.locked=false))));main.append(controls,el('p','hint','Tap any die face to set its number manually. The corresponding hero-specific icon changes with it.'))}
function renderResources(main){const area=el('section','resources');for(const [label,key] of [['Health','health'],['Combat points','cp']]){const item=el('div','resource');item.append(el('h3','',label));const art=el('div','dial-art');inlineSvg(root+'Heroes/'+state.hero+'/'+(key==='health'?'health_dial.svg':'cp_dial.svg'),art);const number=el('span','dial-value',String(state[key]));item.append(art);item.append(number);const controls=el('div','controls dial-controls');controls.append(button('−',()=>action(()=>state[key]=Math.max(0,state[key]-1))),button('+',()=>action(()=>state[key]++)));item.append(controls);area.append(item)}main.append(area)}
function showAbilityZoom(svg,id){
 const original=svg.querySelector('#panel-'+id);if(!original)return;
 const b=original.getBBox(),m=svg.getCTM().inverse().multiply(original.getCTM());
 const pts=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>({x:m.a*x+m.c*y+m.e,y:m.b*x+m.d*y+m.f}));
 const x=Math.min(...pts.map(p=>p.x)),y=Math.min(...pts.map(p=>p.y)),w=Math.max(...pts.map(p=>p.x))-x,h=Math.max(...pts.map(p=>p.y))-y;
 const overlay=el('div','card-overlay'),panel=el('div','card-detail ability-detail');
 overlay.setAttribute('role','dialog');overlay.setAttribute('aria-modal','true');
 panel.append(button('Close ×',()=>overlay.remove(),'detail-close'));
 const viewport=el('div','detail-svg ability-detail-svg'),copy=svg.cloneNode(true);
 copy.querySelectorAll('#layer-panels > [id^="panel-"]').forEach(g=>{if(g.id!=='panel-'+id)g.remove()});
 copy.setAttribute('viewBox',`${x-35} ${y-35} ${w+70} ${h+70}`);
 viewport.append(copy);panel.append(viewport,el('h3','',title(id.replaceAll('-','_'))));
 overlay.append(panel);overlay.onclick=e=>{if(e.target===overlay)overlay.remove()};document.body.append(overlay);
}
function renderBoard(main){
 main.append(el('h2','',state.hero+' ability panels'));
 const board=el('div','compact-board');main.append(board);
 inlineSvg(root+'Heroes/'+state.hero+'/hero_board.svg',board,svg=>{
  svg.querySelector('#layer-background')?.remove();
  svg.querySelector('#layer-janeway-name, #layer-tuvok-name')?.remove();
  const panels=boardSlots[state.hero].map(id=>svg.querySelector('#panel-'+id)).filter(Boolean);
  if(!panels.length)return;
  const bounds=panels.map(g=>{const b=g.getBBox(),m=svg.getCTM().inverse().multiply(g.getCTM()),p=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>({x:m.a*x+m.c*y+m.e,y:m.b*x+m.d*y+m.f}));return {x:Math.min(...p.map(v=>v.x)),y:Math.min(...p.map(v=>v.y)),r:Math.max(...p.map(v=>v.x)),b:Math.max(...p.map(v=>v.y))}});
  const l=Math.min(...bounds.map(b=>b.x)),t=Math.min(...bounds.map(b=>b.y)),r=Math.max(...bounds.map(b=>b.r)),bottom=Math.max(...bounds.map(b=>b.b));
  svg.setAttribute('viewBox',`${l-28} ${t-28} ${r-l+56} ${bottom-t+56}`);
  panels.forEach((g,i)=>{
   const slot=boardSlots[state.hero][i];
   const upgrade=state.upgrades[title(slot.replaceAll('-','_'))];
   g.classList.add('tappable-ability');
   if(upgrade){
    // Keep the original board panel's geometry; show the installed upgrade
    // as an SVG card in its place, scaled to fit the ability footprint.
    const b=g.getBBox(),cardFrame=document.createElementNS('http://www.w3.org/2000/svg','foreignObject');
    cardFrame.setAttribute('x',b.x);cardFrame.setAttribute('y',b.y);
    cardFrame.setAttribute('width',b.width);cardFrame.setAttribute('height',b.height);
    const holder=document.createElement('div');holder.setAttribute('xmlns','http://www.w3.org/1999/xhtml');
    holder.className='installed-ability';
    holder.style.cssText='width:100%;height:100%;display:flex;align-items:center;justify-content:center;overflow:hidden;background:#111b2d;border-radius:10px';
    const image=document.createElement('div');image.className='installed-upgrade-art';image.setAttribute('aria-label',title(upgrade.id));inlineSvg(img(upgrade),image);
    image.style.cssText='display:block;width:100%;height:100%;object-fit:contain';
    holder.append(image);cardFrame.append(holder);
    g.replaceChildren(cardFrame);
    g.addEventListener('click',()=>showCardDetail(upgrade));
   }else g.addEventListener('click',()=>showAbilityZoom(svg,slot));
  });
 });
 main.append(el('p','hint','Tap an ability panel to enlarge it. Installed upgrades replace their board panels for this session.'));
}
function renderCards(main){const counts=el('p','counts','Deck: '+state.deck.length+' · Hand: '+state.hand.length+' · Discard: '+state.discard.length);main.append(counts);const controls=el('div','controls');controls.append(button('Draw 1',()=>action(()=>{if(state.deck.length)state.hand.push(state.deck.shift())})),button('Draw 4',()=>action(()=>{for(let i=0;i<4&&state.deck.length;i++)state.hand.push(state.deck.shift())})),button('Peek',()=>{const n=prompt('How many cards to peek? (1, 2 or 3)','1');if(n!==null&&['1','2','3'].includes(n.trim()))action(()=>state.peek=Math.min(Number(n),state.deck.length))}),button('Shuffle discard into deck',()=>action(()=>{state.deck=shuffle([...state.deck,...state.discard]);state.discard=[];state.peek=0})));main.append(controls);
if(state.peek){main.append(el('h3','','Top '+state.peek+' cards (leftmost is next)'));const peek=el('div','cards');state.deck.slice(0,state.peek).forEach((c,i)=>{const box=cardNode(c);const moves=el('div','controls');moves.append(button('To top',()=>action(()=>{state.deck.splice(i,1);state.deck.unshift(c);state.peek=Math.min(state.peek,state.deck.length)})),button('To bottom',()=>action(()=>{state.deck.splice(i,1);state.deck.push(c);state.peek=Math.min(state.peek,state.deck.length)})));if(i>0)moves.append(button('Move earlier',()=>action(()=>{[state.deck[i-1],state.deck[i]]=[state.deck[i],state.deck[i-1]]})));if(i<state.peek-1)moves.append(button('Move later',()=>action(()=>{[state.deck[i+1],state.deck[i]]=[state.deck[i],state.deck[i+1]]})));box.append(moves);peek.append(box)});main.append(peek,button('Finish peeking',()=>action(()=>state.peek=0)))}
main.append(el('h3','','Hand'));const hand=el('div','cards');state.hand.forEach((c,i)=>{const box=cardNode(c);const actions=el('div','controls');const slot=upgrades[state.hero][c.id];if(slot){actions.append(button('Install on '+slot,()=>action(()=>{state.hand.splice(i,1);if(state.upgrades[slot])state.discard.push(state.upgrades[slot]);state.upgrades[slot]=c}),'primary'))}else actions.append(button('Play / discard',()=>action(()=>{state.discard.push(state.hand.splice(i,1)[0])}),'primary'));actions.append(button('Discard',()=>action(()=>{state.discard.push(state.hand.splice(i,1)[0])})));box.append(actions);hand.append(box)});main.append(hand);main.append(el('h3','','Discard pile'));const discard=el('div','cards');state.discard.slice().reverse().forEach(c=>discard.append(cardNode(c)));main.append(discard)}
function renderTokens(main){main.append(el('h2','','Resources and status tokens'));for(const [name,value] of [['Health',state.health],['CP',state.cp],...Object.entries(state.tokens)]){const line=el('div','counter');line.append(el('strong','',name),button('−',()=>action(()=>{if(name==='Health')state.health=Math.max(0,state.health-1);else if(name==='CP')state.cp=Math.max(0,state.cp-1);else state.tokens[name]=Math.max(0,state.tokens[name]-1)})),el('output','',String(value)),button('+',()=>action(()=>{if(name==='Health')state.health++;else if(name==='CP')state.cp++;else state.tokens[name]++})));main.append(line)}main.append(el('p','hint','Values are intentionally manual. Status effect stack limits and card costs are not enforced.'))}
async function start(){
 try{
  await Promise.all([
   document.fonts.load('400 50px "Gardablack"'),
   document.fonts.load('400 40px "Avenir Next Condensed"'),
   document.fonts.load('italic 400 40px "Avenir Next Condensed"'),
   document.fonts.load('600 40px "Avenir Next Condensed"'),
   document.fonts.load('italic 600 40px "Avenir Next Condensed"'),
   document.fonts.load('700 40px "Avenir Next Condensed"'),
   document.fonts.load('italic 700 40px "Avenir Next Condensed"')
  ]);
 }catch(error){console.error('Unable to load bundled asset fonts:',error)}
 render();
}
start();
