import sharp from 'sharp';
import {mkdir,writeFile} from 'node:fs/promises';
import {join} from 'node:path';
const svg='public/app-icon.svg';
const platform=process.argv[2];
if(!['ios','android','macos'].includes(platform))throw Error('Usage: npm run generate-icons -- ios|android|macos');
async function png(file,size){await mkdir(join(file,'..'),{recursive:true});await sharp(svg,{density:300}).resize(size,size).png().toFile(file)}
if(platform==='ios'){
 const dir='ios/App/App/Assets.xcassets/AppIcon.appiconset';
 await mkdir(dir,{recursive:true});
 await png(join(dir,'AppIcon-512@2x.png'),1024);
 await writeFile(join(dir,'Contents.json'),JSON.stringify({images:[{filename:'AppIcon-512@2x.png',idiom:'universal',platform:'ios',size:'1024x1024'}],info:{author:'xcode',version:1}},null,2));
}
if(platform==='android'){
 for(const [density,size] of Object.entries({'mdpi':48,'hdpi':72,'xhdpi':96,'xxhdpi':144,'xxxhdpi':192})){
  const dir='android/app/src/main/res/mipmap-'+density;
  for(const file of ['ic_launcher.png','ic_launcher_round.png','ic_launcher_foreground.png'])await png(join(dir,file),size);
 }
 // Capacitor templates may reference adaptive XML icons; their foreground layer is supplied above.
}
if(platform==='macos'){
 const dir='src-tauri/icons';await mkdir(dir,{recursive:true});
 for(const [name,size] of [['icon.png',512],['32x32.png',32],['128x128.png',128],['128x128@2x.png',256]])await png(join(dir,name),size);
}
console.log('Generated '+platform+' app icons from Janeway combadge.');
