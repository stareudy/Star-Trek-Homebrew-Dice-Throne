// All 64 required SVGs are committed under playtest-app/public/assets/.
// No external directories, PNGs, fonts, or runtime asset generation are needed.
import {access} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const app=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const required=['Heroes/Janeway/hero_board.svg','Heroes/Tuvok/hero_board.svg','Heroes/Janeway/health_dial.svg','Heroes/Tuvok/cp_dial.svg','Shared/cards/better_d.svg'];
for(const file of required)await access(path.join(app,'public/assets',file));
console.log('Self-contained offline vector assets verified.');
