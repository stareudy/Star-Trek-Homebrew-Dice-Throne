// One-time cloud asset preparation. The print-quality originals remain untouched.
import sharp from 'sharp';
import {readdir,readFile,writeFile,mkdir,stat} from 'node:fs/promises';
import path from 'node:path';
const root=process.cwd(), out=path.join(root,'public/assets'), source=path.resolve(root,'..');
const svgPaths=[];
async function walk(dir){for(const e of await readdir(dir,{withFileTypes:true})){const p=path.join(dir,e.name);if(e.isDirectory())await walk(p);else if(e.name.endsWith('.svg'))svgPaths.push(p)}}
await walk(out);
const needed=new Map();
const bundledFontCss=await readFile(path.join(out,'Shared/fonts/fonts.css'),'utf8');
let rewritten=0;
for(const target of svgPaths){
 const relative=path.relative(out,target);
 const original=path.join(source,relative);
 let svg=await readFile(original,'utf8');
 svg=svg.replace(/@font-face\s*\{[^}]*Gardablack\.ttf[^}]*\}/g,'');
 if(/Avenir|Gardablack|Garda Black/.test(svg)){
  const fontBase=path.relative(path.dirname(target),path.join(out,'Shared/fonts')).split(path.sep).join('/')+'/';
  const fontCss=bundledFontCss.replace(/url\("([^"]+)"\)/g,(_,ref)=>'url("'+fontBase+ref+'")');
  svg=svg.replace(/(<svg\b[^>]*>)/,'$1<style id="bundled-asset-fonts" type="text/css">'+fontCss+'</style>');
 }

 const references=[...svg.matchAll(/(?:href|xlink:href)\s*=\s*["']([^"']+\.(?:png|jpe?g))["']|url\(\s*["']?([^"'()]+\.(?:png|jpe?g))["']?\s*\)/gi)];
 for(const match of references){
  const ref=match[1]||match[2];
  if(/^(?:data:|https?:|\/)/i.test(ref))continue;
  const absolute=path.resolve(path.dirname(original),ref);
  if(!absolute.startsWith(source+path.sep))throw Error('Image outside repository: '+ref);
  const rel=path.relative(source,absolute);
  needed.set(rel,absolute);
 }
 svg=svg.replace(/\.(png|jpe?g)(?=["')])/gi,'.webp');
 await writeFile(target,svg);
 rewritten++;
}
let input=0,output=0;
for(const [rel,original] of needed){
 const destination=path.join(out,rel.replace(/\.(png|jpe?g)$/i,'.webp'));
 await mkdir(path.dirname(destination),{recursive:true});
 const metadata=await sharp(original).metadata();
 // Source assets remain pristine; resize only images larger than their on-screen needs.
 const width=rel.includes('/cards/')?1400:rel.includes('board')?2000:1600;
 await sharp(original).rotate().resize({width,height:width,fit:'inside',withoutEnlargement:true})
   .webp({quality:88,effort:5,alphaQuality:95}).toFile(destination);
 input+=(await stat(original)).size;output+=(await stat(destination)).size;
}
console.log(JSON.stringify({svgFiles:rewritten,uniqueImages:needed.size,originalMiB:(input/1048576).toFixed(2),optimizedMiB:(output/1048576).toFixed(2)},null,2));
