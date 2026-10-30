import {mkdir,readdir,rm,readFile,writeFile} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

// All generated app assets stay inside playtest-app/public/assets.
// Original hero and shared source files are read-only.
const here=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(here,'../../');
const dest=path.resolve(here,'../public/assets');
await rm(dest,{recursive:true,force:true});

function lightenSvg(svg){
  // Remove external font dependencies and substitute portable font stacks.
  svg=svg.replace(/<style\b[^>]*>[\s\S]*?<\/style>/gi,block=>block.replace(/@font-face\s*\{[^}]*\}/gi,''));
  svg=svg.replace(/Gardablack|Garda\s*Black/gi,'Arial Black, Arial, sans-serif');
  svg=svg.replace(/Avenir Next Condensed/gi,'Arial Narrow, Arial, sans-serif');
  svg=svg.replace(/Wremena/gi,'Georgia, serif');
  // Replace each raster image with an opaque black vector rectangle.
  // Preserve every pre-existing vector path, group, and editable text node.
  svg=svg.replace(/<image\b[^>]*\/?\s*>/gi,tag=>{
    const attr=n=>{const m=tag.match(new RegExp('\\b'+n+'="([^"]*)"','i'));return m?m[1]:null};
    const x=attr('x')||'0',y=attr('y')||'0',w=attr('width'),h=attr('height');
    if(!w||!h)return '';
    const transform=attr('transform');
    return '<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="#000000"'+(transform?' transform="'+transform+'"':'')+'/>';
  });
  // Name artwork is gone; restore editable name labels instead.
  svg=svg.replace(/(<text\b[^>]*\bid="(?:janeway|tuvok)-name-label"[^>]*)(>)/gi,(full,tag,end)=>tag.replace(/\s(?:display|opacity)="[^"]*"/gi,'')+end);
  return svg;
}
async function copySvgs(from,to){
  await mkdir(to,{recursive:true});
  for(const entry of await readdir(from,{withFileTypes:true})){
    const src=path.join(from,entry.name),dst=path.join(to,entry.name);
    if(entry.isDirectory())await copySvgs(src,dst);
    else if(entry.isFile()&&entry.name.toLowerCase().endsWith('.svg')){
      await writeFile(dst,lightenSvg(await readFile(src,'utf8')),'utf8');
    }
  }
}
for(const hero of ['Janeway','Tuvok'])await copySvgs(path.join(root,'Heroes',hero),path.join(dest,'Heroes',hero));
await copySvgs(path.join(root,'Shared'),path.join(dest,'Shared'));
console.log('Offline vector-only assets generated (no PNGs or font files).');
