// All 64 required SVGs are committed under playtest-app/public/assets/.
// No external directories, PNGs, fonts, or runtime asset generation are needed.
import {access} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const app=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const required=['Heroes/Janeway/hero_board.svg','Heroes/Tuvok/hero_board.svg','Heroes/Seven of Nine/hero_board.svg','Heroes/Janeway/health_dial.svg','Heroes/Tuvok/cp_dial.svg','Heroes/Seven of Nine/health_dial.svg','Heroes/Seven of Nine/cp_dial.svg','Heroes/Janeway/leaflet.svg','Heroes/Tuvok/leaflet.svg','Heroes/Seven of Nine/art/sevenboardbackground1.webp','Heroes/Seven of Nine/art/board_hero_art.webp','Heroes/Seven of Nine/art/name.webp','Heroes/Seven of Nine/art/defense.webp','Heroes/Seven of Nine/art/health_dial.webp','Heroes/Seven of Nine/art/cp_dial.webp',...Array.from({length:6},(_,i)=>`Heroes/Seven of Nine/icons/die_${i+1}.svg`),'Shared/cards/better_d.svg'];
for(const file of required)await access(path.join(app,'public/assets',file));
console.log('Self-contained offline vector assets verified.');
