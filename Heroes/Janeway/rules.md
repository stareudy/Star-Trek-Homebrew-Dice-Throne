# Janeway — Rules

<style>
@font-face { font-family:Gardablack; src:url('../../Shared/fonts/Gardablack/Gardablack.ttf') format('truetype'); }
.rule { background:#12151d; color:#F7F7F7; padding:20px 24px; max-width:760px; border-radius:10px; font-family:'Avenir Next Condensed','Arial Narrow',sans-serif; font-size:20px; font-weight:400; line-height:1.65; }
.rule-title { font-family:Gardablack,Impact,sans-serif; font-size:1.35em; font-weight:400; color:#F4FAFF; line-height:1.2; margin-bottom:.6em; }
.rule-line { margin:.35em 0; }
.icon { display:inline-block; position:relative; vertical-align:middle; margin:0 .035em; }
.dice-group { display:inline-flex; vertical-align:middle; gap:0; }
.dice-group .icon { margin:0; }
.icon img { display:block; width:100%; height:100%; border:0; }
.numbered::before { content:''; position:absolute; left:28.5%; top:22.5%; width:40%; height:53%; background:var(--face); }
.numbered b { position:absolute; left:48.7%; top:52%; transform:translate(-50%,-50%); font-family:Arial,Helvetica,sans-serif; font-size:.847em; line-height:1; font-weight:700; color:var(--number); text-shadow:none; }
.normal_damage { --face:#030304; --number:#FFFFFF; }
.undefendable_damage { --face:#C21B02; --number:#FFFFFF; }
.damage_prevention { --face:#1468B7; --number:#FFFFFF; }
.damage_prevention::before { left:26%; top:20%; width:46%; height:50%; }
.damage_prevention b { left:50%; top:47%; font-size:.798em; }
.cp { --face:#015768; --number:#FFFFFF; }
.cp::before { left:17%; top:32%; width:29%; height:34%; }
.cp b { left:31%; top:50%; font-size:.525em; }
.carddraw { --face:#FFFFFF; --number:#000000; }
.carddraw::before { left:18%; top:29%; width:39%; height:33%; }
.carddraw b { left:36.8%; top:47%; font-size:.609em; }
.healing { --face:#87DA87; --number:#000000; }
.healing::before { left:26%; top:23.5%; width:46%; height:50%; }
.healing b { left:48.6%; top:51%; font-size:.879em; }
</style>

Rules wording and values are retained from [rules.txt](rules.txt). Presentation was checked against fresh Chrome renders of the linked primary SVGs. SVG differences are noted separately; they do not change the rules below.

This file uses Markdown headings with HTML rule blocks for alignment, spacing, colors, and inline icons. Use a Markdown viewer that supports inline HTML and CSS. Viewers that sanitize styles, including GitHub, may simplify the appearance. Existing SVGs remain the reference for exact artwork, print dimensions, and layout.

The rule blocks use Avenir Next Condensed for rules and Gardablack for headings, scaled for screen reading. Observed SVG line breaks are followed where the wording matches; text absent from the SVG retains its source paragraph. Blue (`#336A9C`) and orange (`#EB943A`) text follow the observed SVG emphasis, including partial phase-name coloring. Icons link to the existing originals. Numbered icons keep their value editable in HTML.

## LEAFLET

### COFFEE

SVG reference: [leaflet.svg](leaflet.svg)

<!-- SVG presentation: left-aligned rules; Avenir Next Condensed Regular; observed local text size 46 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="COFFEE" data-leaflet-layout="token_panel_v1" style="text-align:left;">
<div class="rule-title">COFFEE</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Positive Status Effect | Stack limit: 5</div>
<div style="height:.55em;"></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Once per turn during your <span style="color:#336A9C">Main</span> <span style="color:#336A9C">Phase</span>, spend<br />these tokens for one of the following effects:</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Spend 1: Gain <span class="icon" data-icon="cp.svg" data-value="1" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 1" width="28" height="28" /></span>.</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Spend 2: Roll one <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span> and gain half the roll<br />value (rounded up) as <span class="icon" data-icon="cp.svg" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp" width="28" height="28" /></span>.</div>
</div>

### COMMAND CODES

SVG reference: [leaflet.svg](leaflet.svg)


<!-- SVG presentation: left-aligned rules; Avenir Next Condensed Regular; observed local text size 46 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="COMMAND CODES" data-leaflet-layout="token_panel_v1" style="text-align:left;">
<div class="rule-title">COMMAND CODES</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Positive Status Effect | Stack limit: 5</div>
<div style="height:.55em;"></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">During any <span style="color:#EB943A">Roll</span> <span style="color:#EB943A">Phase</span>, spend Command<br />Codes for one effect:</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Spend 1: Reroll any one of your own dice.</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Spend 4: Select one of your opponents dice to<br />force them to reroll it, or change any one of<br />your dice to any value except six.</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Spend 5: Change one of your dice to a six.</div>
</div>

### REPRIMAND

SVG reference: [leaflet.svg](leaflet.svg)


<!-- SVG presentation: left-aligned rules; Avenir Next Condensed Regular; observed local text size 46 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="REPRIMAND" data-leaflet-layout="token_panel_v1" style="text-align:left;">
<div class="rule-title">REPRIMAND</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Negative Status Effect | Stack limit: 2</div>
<div style="height:.55em;"></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">The next time a player with this token<br />would play a <span style="color:#EB943A">Roll</span> <span style="color:#EB943A">Phase</span> <span style="color:#EB943A">action</span> card,<br />they must pay one extra <span class="icon" data-icon="cp.svg" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp" width="28" height="28" /></span> for each<br />Reprimand token to play the card. Then<br />remove all Reprimand tokens.</div>
</div>

## HERO BOARD

### FIRE PHASERS

SVG reference: [hero_board.svg](hero_board.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="FIRE PHASERS" style="text-align:center;">
<div class="rule-title">FIRE PHASERS</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="4" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 4" width="28" height="28" /><b aria-hidden="true">4</b></span> dmg</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="5" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 5" width="28" height="28" /><b aria-hidden="true">5</b></span> dmg</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="6" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 6" width="28" height="28" /><b aria-hidden="true">6</b></span> dmg</div>
</div>

### SHORE LEAVE

SVG reference: [hero_board.svg](hero_board.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="SHORE LEAVE" style="text-align:center;">
<div class="rule-title">SHORE LEAVE</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="combadge_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> <span class="icon" data-icon="combadge_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> <span class="icon" data-icon="combadge_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Gain <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span> and <span class="icon" data-icon="command_codes.svg" style="width:1.400em;height:1.400em;"><img src="icons/command_codes.svg" alt="command codes" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Draw <span class="icon" data-icon="carddraw.svg" data-value="1" style="width:1.213em;height:1.400em;"><img src="../../Shared/icons/carddraw.svg" alt="carddraw 1" width="28" height="28" /></span></div>
</div>

### DO IT

SVG reference: [hero_board.svg](hero_board.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="DO IT" style="text-align:center;">
<div class="rule-title">DO IT</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="icon" data-icon="smallstraight.svg" style="width:4.348em;height:1.800em;"><img src="../../Shared/icons/smallstraight.svg" alt="smallstraight" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="7" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 7" width="28" height="28" /><b aria-hidden="true">7</b></span> dmg</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Inflict <span class="icon" data-icon="reprimand.svg" style="width:1.400em;height:1.400em;"><img src="icons/reprimand.svg" alt="reprimand" width="28" height="28" /></span></div>
</div>

### RED ALERT

SVG reference: [hero_board.svg](hero_board.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="RED ALERT" style="text-align:center;">
<div class="rule-title">RED ALERT</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="earth_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Gain <span class="icon" data-icon="command_codes.svg" style="width:1.400em;height:1.400em;"><img src="icons/command_codes.svg" alt="command codes" width="28" height="28" /></span> and <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Inflict <span class="icon" data-icon="reprimand.svg" style="width:1.400em;height:1.400em;"><img src="icons/reprimand.svg" alt="reprimand" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="7" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 7" width="28" height="28" /><b aria-hidden="true">7</b></span> dmg</div>
</div>

### TACTICAL EXERCISES

SVG reference: [hero_board.svg](hero_board.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="TACTICAL EXERCISES" style="text-align:center;">
<div class="rule-title">TACTICAL EXERCISES</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Roll 2 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span> for the following effects:</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">For each <span class="icon" data-icon="coffee_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="4" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 4" width="28" height="28" /><b aria-hidden="true">4</b></span> dmg</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="icon" data-icon="combadge_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> Gain 2 <span class="icon" data-icon="command_codes.svg" style="width:1.400em;height:1.400em;"><img src="icons/command_codes.svg" alt="command codes" width="28" height="28" /></span> and 1 <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="icon" data-icon="earth_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span> Draw <span class="icon" data-icon="carddraw.svg" data-value="1" style="width:1.213em;height:1.400em;"><img src="../../Shared/icons/carddraw.svg" alt="carddraw 1" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="dice-group"><span class="icon" data-icon="earth_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span></span> Begin a new<br /><span style="color:#EB943A">Offensive</span> <span style="color:#EB943A">Roll</span> <span style="color:#EB943A">Phase</span> targeting the<br />same opponent</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">You may spend 1 <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span> before rolling to<br />roll 3 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span> instead of 2</div>
</div>

### COMMAND PROTOCOL

SVG reference: [hero_board.svg](hero_board.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="COMMAND PROTOCOL" style="text-align:center;">
<div class="rule-title">COMMAND PROTOCOL</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="combadge_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> <span class="icon" data-icon="combadge_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="2" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 2" width="28" height="28" /><b aria-hidden="true">2</b></span> dmg. You may<br />spend up to 2 <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span> to add<br /><span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="4" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 4" width="28" height="28" /><b aria-hidden="true">4</b></span> dmg per <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span> spent</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">You may spend 3 <span class="icon" data-icon="command_codes.svg" style="width:1.400em;height:1.400em;"><img src="icons/command_codes.svg" alt="command codes" width="28" height="28" /></span><br />to make this attack undefendable</div>
</div>

### GET OFF MY SHIP!

SVG reference: [hero_board.svg](hero_board.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="GET OFF MY SHIP!" style="text-align:center;">
<div class="rule-title">GET OFF MY SHIP!</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="icon" data-icon="largestraight.svg" style="width:5.102em;height:1.800em;"><img src="../../Shared/icons/largestraight.svg" alt="largestraight" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="7" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 7" width="28" height="28" /><b aria-hidden="true">7</b></span> dmg, then roll 3 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">For each <span class="icon" data-icon="coffee_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> add <span class="icon" data-icon="normal_damage.svg" data-value="1" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 1" width="28" height="28" /></span> dmg</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="icon" data-icon="combadge_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> inflict <span class="icon" data-icon="reprimand.svg" style="width:1.400em;height:1.400em;"><img src="icons/reprimand.svg" alt="reprimand" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="icon" data-icon="earth_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span> gain <span class="icon" data-icon="command_codes.svg" style="width:1.400em;height:1.400em;"><img src="icons/command_codes.svg" alt="command codes" width="28" height="28" /></span> or <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="dice-group"><span class="icon" data-icon="coffee_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="combadge_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span></span> ignore the<br />previously mentioned effects and<br />instead add <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="3" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 3" width="28" height="28" /><b aria-hidden="true">3</b></span> dmg and make the<br />attack undefendable</div>
</div>

### SHIELDS UP

SVG reference: [hero_board.svg](hero_board.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="SHIELDS UP" style="text-align:center;">
<div class="rule-title">SHIELDS UP</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="icon" data-icon="defense_3_dice.svg" style="width:4.950em;height:1.650em;"><img src="../../Shared/icons/defense_3_dice.svg" alt="defense 3 dice" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Roll 3 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="icon" data-icon="coffee_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> prevent <span class="icon" data-icon="damage_prevention.svg" data-value="1" style="width:1.282em;height:1.400em;"><img src="../../Shared/icons/damage_prevention.svg" alt="damage prevention 1" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="icon" data-icon="combadge_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> prevent <span class="icon numbered damage_prevention" data-icon="damage_prevention.svg" data-value="2" style="width:1.282em;height:1.400em;"><img src="../../Shared/icons/damage_prevention.svg" alt="damage prevention 2" width="28" height="28" /><b aria-hidden="true">2</b></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="dice-group"><span class="icon" data-icon="combadge_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span></span> Inflict <span class="icon" data-icon="reprimand.svg" style="width:1.400em;height:1.400em;"><img src="icons/reprimand.svg" alt="reprimand" width="28" height="28" /></span></div>
</div>

### PUNCH YOUR WAY THROUGH (ULTIMATE)

SVG reference: [hero_board.svg](hero_board.svg)

<!-- Ultimate presentation: left-aligned, single-line effects at 49.95 effective SVG units; left-aligned disclaimer at 36.5 effective SVG units. Preserve source transforms and disclaimer breaks; do not apply regular-panel defaults. -->
<div class="rule ultimate-rule" data-rule="PUNCH YOUR WAY THROUGH (ULTIMATE)" style="text-align:left;" data-layout="ultimate" data-source-effective-rules-size="49.949999999999996" data-source-effective-disclaimer-size="36.5">
<div class="rule-title">PUNCH YOUR WAY THROUGH (ULTIMATE)</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;" data-ultimate-role="activation"><span class="dice-group"><span class="icon" data-icon="earth_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span></span></div>
<div class="rule-line ultimate-effects" data-source-line="rules" data-ultimate-role="effects" style="margin:.35em 0;text-align:left;white-space:nowrap;font-size:1.2em;">Gain 3 <span class="icon" data-icon="command_codes.svg" style="width:1.400em;height:1.400em;"><img src="icons/command_codes.svg" alt="command codes" width="28" height="28" /></span>, gain 3 <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span>, and inflict 2 <span class="icon" data-icon="reprimand.svg" style="width:1.400em;height:1.400em;"><img src="icons/reprimand.svg" alt="reprimand" width="28" height="28" /></span> Then deal <span class="icon numbered undefendable_damage" data-icon="undefendable_damage.svg" data-value="12" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/undefendable_damage.svg" alt="undefendable damage 12" width="28" height="28" /><b aria-hidden="true">12</b></span> dmg</div>
<div class="rule-line ultimate-disclaimer" data-source-line="rules" style="margin:.35em 0;text-align:left;font-size:0.876876877em;line-height:1.25;" data-ultimate-role="disclaimer">Dice may be altered to prevent an Ultimate. Otherwise, no action of any<br />kind may be performed by any opponent until the ability fully completes.</div>
</div>

## CARDS

The first 18 cards in Janeway's deck are standard Dice Throne cards and are omitted here. The cards below are Janeway-specific.

### DETERMINATION

SVG reference: [cards/determination.svg](cards/determination.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="DETERMINATION" style="text-align:center;">
<div class="rule-title">DETERMINATION</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#EB943A;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="2" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 2" width="28" height="28" /><b aria-hidden="true">2</b></span> | Roll Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">A chosen player may perform an<br />additional Roll Attempt of up to<br />three <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span> during their <span style="color:#EB943A">Offensive</span><br />or <span style="color:#EB943A">Defensive</span> <span style="color:#EB943A">Roll</span> <span style="color:#EB943A">Phase</span></div>
</div>

### SET TO KILL

SVG reference: [cards/set_to_kill.svg](cards/set_to_kill.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="SET TO KILL" style="text-align:center;">
<div class="rule-title">SET TO KILL</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#EB943A;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="3" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 3" width="28" height="28" /><b aria-hidden="true">3</b></span> | Roll Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">You may remove up to 2 <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span><br />to add <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="3" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 3" width="28" height="28" /><b aria-hidden="true">3</b></span> dmg per <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span> removed</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">You may remove 3 <span class="icon" data-icon="command_codes.svg" style="width:1.400em;height:1.400em;"><img src="icons/command_codes.svg" alt="command codes" width="28" height="28" /></span><br />to make this attack undefendable<br />(Attack modifier)</div>
</div>

### COUNTERPOINT

SVG reference: [cards/counterpoint.svg](cards/counterpoint.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="COUNTERPOINT" style="text-align:center;">
<div class="rule-title">COUNTERPOINT</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#EB943A;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="3" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 3" width="28" height="28" /><b aria-hidden="true">3</b></span> | Roll Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">(Play only after being attacked)</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Prevent <span class="icon numbered damage_prevention" data-icon="damage_prevention.svg" data-value="3" style="width:1.282em;height:1.400em;"><img src="../../Shared/icons/damage_prevention.svg" alt="damage prevention 3" width="28" height="28" /><b aria-hidden="true">3</b></span> incoming dmg, and<br />deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="3" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 3" width="28" height="28" /><b aria-hidden="true">3</b></span> dmg to the attacking player</div>
</div>

### THERE'S COFFEE IN THAT NEBULA

SVG reference: [cards/theres_coffee_in_that_nebula.svg](cards/theres_coffee_in_that_nebula.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="THERE&#x27;S COFFEE IN THAT NEBULA" style="text-align:center;">
<div class="rule-title">THERE&#x27;S COFFEE IN THAT NEBULA</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#336A9C;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="0" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 0" width="28" height="28" /><b aria-hidden="true">0</b></span> | Main Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Roll 1 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span> and gain half the value<br />(rounded up) in <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span></div>
</div>

### COMMAND TRAINING

SVG reference: [cards/command_training.svg](cards/command_training.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="COMMAND TRAINING" style="text-align:center;">
<div class="rule-title">COMMAND TRAINING</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#336A9C;margin-bottom:.7em;">Cost: <span class="icon" data-icon="cp.svg" data-value="1" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 1" width="28" height="28" /></span> | Main Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Gain <span class="icon" data-icon="command_codes.svg" style="width:1.400em;height:1.400em;"><img src="icons/command_codes.svg" alt="command codes" width="28" height="28" /></span>. You may spend an<br />additional <span class="icon numbered cp" data-icon="cp.svg" data-value="4" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 4" width="28" height="28" /><b aria-hidden="true">4</b></span> for an additional <span class="icon" data-icon="command_codes.svg" style="width:1.400em;height:1.400em;"><img src="icons/command_codes.svg" alt="command codes" width="28" height="28" /></span><br />per extra <span class="icon numbered cp" data-icon="cp.svg" data-value="2" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 2" width="28" height="28" /><b aria-hidden="true">2</b></span> spent</div>
</div>

### CAPTAIN'S PREROGATIVE

SVG reference: [cards/captains_prerogative.svg](cards/captains_prerogative.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="CAPTAIN&#x27;S PREROGATIVE" style="text-align:center;">
<div class="rule-title">CAPTAIN&#x27;S PREROGATIVE</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#336A9C;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="3" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 3" width="28" height="28" /><b aria-hidden="true">3</b></span> | Main Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Can only be played during your first<br /><span style="color:#336A9C">Main</span> <span style="color:#336A9C">Phase</span>. You may skip your<br /><span style="color:#EB943A">Offensive</span> <span style="color:#EB943A">Roll</span> <span style="color:#EB943A">Phase</span> and instead roll<br />1 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span> and heal the total roll<br />value</div>
</div>

### REPRIMANDED

SVG reference: [cards/reprimanded.svg](cards/reprimanded.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="REPRIMANDED" style="text-align:center;">
<div class="rule-title">REPRIMANDED</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="3" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 3" width="28" height="28" /><b aria-hidden="true">3</b></span> | Instant Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Inflict <span class="icon" data-icon="reprimand.svg" style="width:1.400em;height:1.400em;"><img src="icons/reprimand.svg" alt="reprimand" width="28" height="28" /></span> on two players.<br />(Can be two different players<br />or the same player twice)</div>
</div>

### RESOLVE

SVG reference: [cards/resolve.svg](cards/resolve.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 16 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="RESOLVE" style="text-align:center;">
<div class="rule-title">RESOLVE</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="3" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 3" width="28" height="28" /><b aria-hidden="true">3</b></span> | Instant Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Roll 3 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span> for the following effects:</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">For each <span class="icon" data-icon="coffee_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> Gain <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">For each <span class="icon" data-icon="combadge_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> Gain <span class="icon" data-icon="command_codes.svg" style="width:1.400em;height:1.400em;"><img src="icons/command_codes.svg" alt="command codes" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="icon" data-icon="earth_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span> <span class="icon numbered healing" data-icon="healing.svg" data-value="6" style="width:1.517em;height:1.400em;"><img src="../../Shared/icons/healing.svg" alt="healing 6" width="28" height="28" /><b aria-hidden="true">6</b></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="dice-group"><span class="icon" data-icon="earth_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span></span> Also gain <span class="icon" data-icon="command_codes.svg" style="width:1.400em;height:1.400em;"><img src="icons/command_codes.svg" alt="command codes" width="28" height="28" /></span> and <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span></div>
</div>

### FIRE PHASERS II

SVG reference: [cards/fire_phasers_ii.svg](cards/fire_phasers_ii.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="FIRE PHASERS II" style="text-align:center;">
<div class="rule-title">FIRE PHASERS II</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#336A9C;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="2" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 2" width="28" height="28" /><b aria-hidden="true">2</b></span> | Main Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="5" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 5" width="28" height="28" /><b aria-hidden="true">5</b></span> dmg</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="6" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 6" width="28" height="28" /><b aria-hidden="true">6</b></span> dmg</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="7" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 7" width="28" height="28" /><b aria-hidden="true">7</b></span> dmg</div>
</div>

### FIRE PHASERS III

SVG reference: [cards/fire_phasers_iii.svg](cards/fire_phasers_iii.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="FIRE PHASERS III" style="text-align:center;">
<div class="rule-title">FIRE PHASERS III</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#336A9C;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="3" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 3" width="28" height="28" /><b aria-hidden="true">3</b></span> | Main Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="6" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 6" width="28" height="28" /><b aria-hidden="true">6</b></span> dmg</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="7" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 7" width="28" height="28" /><b aria-hidden="true">7</b></span> dmg</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="8" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 8" width="28" height="28" /><b aria-hidden="true">8</b></span> dmg</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Inflict <span class="icon" data-icon="reprimand.svg" style="width:1.400em;height:1.400em;"><img src="icons/reprimand.svg" alt="reprimand" width="28" height="28" /></span></div>
</div>

### SHORE LEAVE II

SVG reference: [cards/shore_leave_ii.svg](cards/shore_leave_ii.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="SHORE LEAVE II" style="text-align:center;">
<div class="rule-title">SHORE LEAVE II</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#336A9C;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="2" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 2" width="28" height="28" /><b aria-hidden="true">2</b></span> | Main Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="combadge_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> <span class="icon" data-icon="combadge_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> <span class="icon" data-icon="combadge_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Gain 2 <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span> and 2 <span class="icon" data-icon="command_codes.svg" style="width:1.400em;height:1.400em;"><img src="icons/command_codes.svg" alt="command codes" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Draw <span class="icon" data-icon="carddraw.svg" data-value="1" style="width:1.213em;height:1.400em;"><img src="../../Shared/icons/carddraw.svg" alt="carddraw 1" width="28" height="28" /></span></div>
</div>

### TACTICAL EXERCISES II

SVG reference: [cards/tactical_exercises_ii.svg](cards/tactical_exercises_ii.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="TACTICAL EXERCISES II" style="text-align:center;">
<div class="rule-title">TACTICAL EXERCISES II</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#336A9C;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="3" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 3" width="28" height="28" /><b aria-hidden="true">3</b></span> | Main Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="coffee_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Roll 3 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span> for the following effects:</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">For each <span class="icon" data-icon="coffee_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="4" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 4" width="28" height="28" /><b aria-hidden="true">4</b></span> dmg</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="icon" data-icon="combadge_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> Gain 2 <span class="icon" data-icon="command_codes.svg" style="width:1.400em;height:1.400em;"><img src="icons/command_codes.svg" alt="command codes" width="28" height="28" /></span> and 1 <span class="icon" data-icon="coffee_token.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_token.svg" alt="coffee token" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="icon" data-icon="earth_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span> Draw <span class="icon" data-icon="carddraw.svg" data-value="1" style="width:1.213em;height:1.400em;"><img src="../../Shared/icons/carddraw.svg" alt="carddraw 1" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="dice-group"><span class="icon" data-icon="earth_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span></span> Begin a new<br /><span style="color:#EB943A">Offensive</span> <span style="color:#EB943A">Roll</span> <span style="color:#EB943A">Phase</span> targeting<br />the same opponent</div>
</div>

### SHIELDS UP II

SVG reference: [cards/shields_up_ii.svg](cards/shields_up_ii.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="SHIELDS UP II" style="text-align:center;">
<div class="rule-title">SHIELDS UP II</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#336A9C;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="3" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 3" width="28" height="28" /><b aria-hidden="true">3</b></span> | Main Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="icon" data-icon="defense_4_dice.svg" style="width:6.600em;height:1.650em;"><img src="../../Shared/icons/defense_4_dice.svg" alt="defense 4 dice" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Roll 4 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span>:</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">For each <span class="icon" data-icon="coffee_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> prevent <span class="icon" data-icon="damage_prevention.svg" data-value="1" style="width:1.282em;height:1.400em;"><img src="../../Shared/icons/damage_prevention.svg" alt="damage prevention 1" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="icon" data-icon="combadge_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> prevent <span class="icon numbered damage_prevention" data-icon="damage_prevention.svg" data-value="2" style="width:1.282em;height:1.400em;"><img src="../../Shared/icons/damage_prevention.svg" alt="damage prevention 2" width="28" height="28" /><b aria-hidden="true">2</b></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="dice-group"><span class="icon" data-icon="combadge_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span></span> Inflict <span class="icon" data-icon="reprimand.svg" style="width:1.400em;height:1.400em;"><img src="icons/reprimand.svg" alt="reprimand" width="28" height="28" /></span></div>
</div>

### SHIELDS UP III

SVG reference: [cards/shields_up_iii.svg](cards/shields_up_iii.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="SHIELDS UP III" style="text-align:center;">
<div class="rule-title">SHIELDS UP III</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#336A9C;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="4" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 4" width="28" height="28" /><b aria-hidden="true">4</b></span> | Main Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="icon" data-icon="defense_5_dice.svg" style="width:8.250em;height:1.650em;"><img src="../../Shared/icons/defense_5_dice.svg" alt="defense 5 dice" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Roll 5 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span>:</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">For each <span class="icon" data-icon="coffee_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/coffee_die.svg" alt="coffee die" width="28" height="28" /></span> prevent <span class="icon" data-icon="damage_prevention.svg" data-value="1" style="width:1.282em;height:1.400em;"><img src="../../Shared/icons/damage_prevention.svg" alt="damage prevention 1" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">For each <span class="icon" data-icon="combadge_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> prevent <span class="icon numbered damage_prevention" data-icon="damage_prevention.svg" data-value="2" style="width:1.282em;height:1.400em;"><img src="../../Shared/icons/damage_prevention.svg" alt="damage prevention 2" width="28" height="28" /><b aria-hidden="true">2</b></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="dice-group"><span class="icon" data-icon="combadge_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/combadge_die.svg" alt="combadge die" width="28" height="28" /></span> <span class="icon" data-icon="earth_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/earth_die.svg" alt="earth die" width="28" height="28" /></span></span> Inflict <span class="icon" data-icon="reprimand.svg" style="width:1.400em;height:1.400em;"><img src="icons/reprimand.svg" alt="reprimand" width="28" height="28" /></span></div>
</div>

<!-- stdt-icon-inventory:v1
{
  "schema_version": 1,
  "status": "current",
  "source": "rules.md",
  "content_sha256": "c597d9d63addb19772d798416d34a6be9e1dfe01f3861d3994bd68d706802d10",
  "counting": {
    "scope": "explicit gameplay icon references in rendered rules blocks",
    "excludes": [
      "CP cost/timing metadata",
      "titles",
      "design notes and brainstorming",
      "shared Standard Cards",
      "artwork-only icons"
    ],
    "number": "explicit data-value, or null for an unnumbered reference; excludes intrinsic die labels",
    "references": "occurrences, not quantities of tokens gained, dice rolled, or damage dealt",
    "asset_observations": "separate saved-artwork instances; never added to rules reference totals"
  },
  "coverage": {
    "leaflet": {
      "entries": 3,
      "references": 4
    },
    "hero_board": {
      "entries": 9,
      "references": 91
    },
    "cards": {
      "entries": 14,
      "references": 96
    }
  },
  "total_rules_references": 191,
  "entries": [
    {
      "section": "leaflet",
      "name": "COFFEE",
      "status": "written",
      "icons": [
        {
          "file": "cp.svg",
          "path": "../../Shared/icons/cp.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "cp.svg",
          "path": "../../Shared/icons/cp.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "leaflet",
      "name": "COMMAND CODES",
      "status": "written",
      "icons": []
    },
    {
      "section": "leaflet",
      "name": "REPRIMAND",
      "status": "written",
      "icons": [
        {
          "file": "cp.svg",
          "path": "../../Shared/icons/cp.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "FIRE PHASERS",
      "status": "written",
      "icons": [
        {
          "file": "coffee_die.svg",
          "path": "icons/coffee_die.svg",
          "number": null,
          "references": 12
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 4,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 5,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 6,
          "references": 1
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "SHORE LEAVE",
      "status": "written",
      "icons": [
        {
          "file": "carddraw.svg",
          "path": "../../Shared/icons/carddraw.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "coffee_token.svg",
          "path": "icons/coffee_token.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "combadge_die.svg",
          "path": "icons/combadge_die.svg",
          "number": null,
          "references": 3
        },
        {
          "file": "command_codes.svg",
          "path": "icons/command_codes.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "DO IT",
      "status": "written",
      "icons": [
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 7,
          "references": 1
        },
        {
          "file": "reprimand.svg",
          "path": "icons/reprimand.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "smallstraight.svg",
          "path": "../../Shared/icons/smallstraight.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "RED ALERT",
      "status": "written",
      "icons": [
        {
          "file": "coffee_token.svg",
          "path": "icons/coffee_token.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "command_codes.svg",
          "path": "icons/command_codes.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "earth_die.svg",
          "path": "icons/earth_die.svg",
          "number": null,
          "references": 4
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 7,
          "references": 1
        },
        {
          "file": "reprimand.svg",
          "path": "icons/reprimand.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "TACTICAL EXERCISES",
      "status": "written",
      "icons": [
        {
          "file": "carddraw.svg",
          "path": "../../Shared/icons/carddraw.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "coffee_die.svg",
          "path": "icons/coffee_die.svg",
          "number": null,
          "references": 5
        },
        {
          "file": "coffee_token.svg",
          "path": "icons/coffee_token.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "combadge_die.svg",
          "path": "icons/combadge_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "command_codes.svg",
          "path": "icons/command_codes.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "earth_die.svg",
          "path": "icons/earth_die.svg",
          "number": null,
          "references": 4
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 4,
          "references": 1
        },
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
          "number": null,
          "references": 2
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "COMMAND PROTOCOL",
      "status": "written",
      "icons": [
        {
          "file": "coffee_die.svg",
          "path": "icons/coffee_die.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "coffee_token.svg",
          "path": "icons/coffee_token.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "combadge_die.svg",
          "path": "icons/combadge_die.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "command_codes.svg",
          "path": "icons/command_codes.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "earth_die.svg",
          "path": "icons/earth_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 2,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 4,
          "references": 1
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "GET OFF MY SHIP!",
      "status": "written",
      "icons": [
        {
          "file": "coffee_die.svg",
          "path": "icons/coffee_die.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "coffee_token.svg",
          "path": "icons/coffee_token.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "combadge_die.svg",
          "path": "icons/combadge_die.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "command_codes.svg",
          "path": "icons/command_codes.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "earth_die.svg",
          "path": "icons/earth_die.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "largestraight.svg",
          "path": "../../Shared/icons/largestraight.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 3,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 7,
          "references": 1
        },
        {
          "file": "reprimand.svg",
          "path": "icons/reprimand.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "SHIELDS UP",
      "status": "written",
      "icons": [
        {
          "file": "coffee_die.svg",
          "path": "icons/coffee_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "combadge_die.svg",
          "path": "icons/combadge_die.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "damage_prevention.svg",
          "path": "../../Shared/icons/damage_prevention.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "damage_prevention.svg",
          "path": "../../Shared/icons/damage_prevention.svg",
          "number": 2,
          "references": 1
        },
        {
          "file": "defense_3_dice.svg",
          "path": "../../Shared/icons/defense_3_dice.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "earth_die.svg",
          "path": "icons/earth_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "reprimand.svg",
          "path": "icons/reprimand.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "PUNCH YOUR WAY THROUGH (ULTIMATE)",
      "status": "written",
      "icons": [
        {
          "file": "coffee_token.svg",
          "path": "icons/coffee_token.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "command_codes.svg",
          "path": "icons/command_codes.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "earth_die.svg",
          "path": "icons/earth_die.svg",
          "number": null,
          "references": 5
        },
        {
          "file": "reprimand.svg",
          "path": "icons/reprimand.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "undefendable_damage.svg",
          "path": "../../Shared/icons/undefendable_damage.svg",
          "number": 12,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "DETERMINATION",
      "status": "written",
      "icons": [
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "SET TO KILL",
      "status": "written",
      "icons": [
        {
          "file": "coffee_token.svg",
          "path": "icons/coffee_token.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "command_codes.svg",
          "path": "icons/command_codes.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 3,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "COUNTERPOINT",
      "status": "written",
      "icons": [
        {
          "file": "damage_prevention.svg",
          "path": "../../Shared/icons/damage_prevention.svg",
          "number": 3,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 3,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "THERE'S COFFEE IN THAT NEBULA",
      "status": "written",
      "icons": [
        {
          "file": "coffee_token.svg",
          "path": "icons/coffee_token.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "COMMAND TRAINING",
      "status": "written",
      "icons": [
        {
          "file": "command_codes.svg",
          "path": "icons/command_codes.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "cp.svg",
          "path": "../../Shared/icons/cp.svg",
          "number": 2,
          "references": 1
        },
        {
          "file": "cp.svg",
          "path": "../../Shared/icons/cp.svg",
          "number": 4,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "CAPTAIN'S PREROGATIVE",
      "status": "written",
      "icons": [
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "REPRIMANDED",
      "status": "written",
      "icons": [
        {
          "file": "reprimand.svg",
          "path": "icons/reprimand.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "RESOLVE",
      "status": "written",
      "icons": [
        {
          "file": "coffee_die.svg",
          "path": "icons/coffee_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "coffee_token.svg",
          "path": "icons/coffee_token.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "combadge_die.svg",
          "path": "icons/combadge_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "command_codes.svg",
          "path": "icons/command_codes.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "earth_die.svg",
          "path": "icons/earth_die.svg",
          "number": null,
          "references": 3
        },
        {
          "file": "healing.svg",
          "path": "../../Shared/icons/healing.svg",
          "number": 6,
          "references": 1
        },
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "FIRE PHASERS II",
      "status": "written",
      "icons": [
        {
          "file": "coffee_die.svg",
          "path": "icons/coffee_die.svg",
          "number": null,
          "references": 12
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 5,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 6,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 7,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "FIRE PHASERS III",
      "status": "written",
      "icons": [
        {
          "file": "coffee_die.svg",
          "path": "icons/coffee_die.svg",
          "number": null,
          "references": 12
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 6,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 7,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 8,
          "references": 1
        },
        {
          "file": "reprimand.svg",
          "path": "icons/reprimand.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "SHORE LEAVE II",
      "status": "written",
      "icons": [
        {
          "file": "carddraw.svg",
          "path": "../../Shared/icons/carddraw.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "coffee_token.svg",
          "path": "icons/coffee_token.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "combadge_die.svg",
          "path": "icons/combadge_die.svg",
          "number": null,
          "references": 3
        },
        {
          "file": "command_codes.svg",
          "path": "icons/command_codes.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "TACTICAL EXERCISES II",
      "status": "written",
      "icons": [
        {
          "file": "carddraw.svg",
          "path": "../../Shared/icons/carddraw.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "coffee_die.svg",
          "path": "icons/coffee_die.svg",
          "number": null,
          "references": 5
        },
        {
          "file": "coffee_token.svg",
          "path": "icons/coffee_token.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "combadge_die.svg",
          "path": "icons/combadge_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "command_codes.svg",
          "path": "icons/command_codes.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "earth_die.svg",
          "path": "icons/earth_die.svg",
          "number": null,
          "references": 4
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 4,
          "references": 1
        },
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "SHIELDS UP II",
      "status": "written",
      "icons": [
        {
          "file": "coffee_die.svg",
          "path": "icons/coffee_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "combadge_die.svg",
          "path": "icons/combadge_die.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "damage_prevention.svg",
          "path": "../../Shared/icons/damage_prevention.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "damage_prevention.svg",
          "path": "../../Shared/icons/damage_prevention.svg",
          "number": 2,
          "references": 1
        },
        {
          "file": "defense_4_dice.svg",
          "path": "../../Shared/icons/defense_4_dice.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "earth_die.svg",
          "path": "icons/earth_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "reprimand.svg",
          "path": "icons/reprimand.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "SHIELDS UP III",
      "status": "written",
      "icons": [
        {
          "file": "coffee_die.svg",
          "path": "icons/coffee_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "combadge_die.svg",
          "path": "icons/combadge_die.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "damage_prevention.svg",
          "path": "../../Shared/icons/damage_prevention.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "damage_prevention.svg",
          "path": "../../Shared/icons/damage_prevention.svg",
          "number": 2,
          "references": 1
        },
        {
          "file": "defense_5_dice.svg",
          "path": "../../Shared/icons/defense_5_dice.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "earth_die.svg",
          "path": "icons/earth_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "reprimand.svg",
          "path": "icons/reprimand.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
          "number": null,
          "references": 1
        }
      ]
    }
  ],
  "usage_by_icon": {
    "carddraw.svg": [
      {
        "section": "hero_board",
        "entry": "SHORE LEAVE",
        "number": 1,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "TACTICAL EXERCISES",
        "number": 1,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SHORE LEAVE II",
        "number": 1,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "TACTICAL EXERCISES II",
        "number": 1,
        "references": 1
      }
    ],
    "coffee_die.svg": [
      {
        "section": "hero_board",
        "entry": "FIRE PHASERS",
        "number": null,
        "references": 12
      },
      {
        "section": "hero_board",
        "entry": "TACTICAL EXERCISES",
        "number": null,
        "references": 5
      },
      {
        "section": "hero_board",
        "entry": "COMMAND PROTOCOL",
        "number": null,
        "references": 2
      },
      {
        "section": "hero_board",
        "entry": "GET OFF MY SHIP!",
        "number": null,
        "references": 2
      },
      {
        "section": "hero_board",
        "entry": "SHIELDS UP",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "RESOLVE",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "FIRE PHASERS II",
        "number": null,
        "references": 12
      },
      {
        "section": "cards",
        "entry": "FIRE PHASERS III",
        "number": null,
        "references": 12
      },
      {
        "section": "cards",
        "entry": "TACTICAL EXERCISES II",
        "number": null,
        "references": 5
      },
      {
        "section": "cards",
        "entry": "SHIELDS UP II",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SHIELDS UP III",
        "number": null,
        "references": 1
      }
    ],
    "coffee_token.svg": [
      {
        "section": "hero_board",
        "entry": "SHORE LEAVE",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "RED ALERT",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "TACTICAL EXERCISES",
        "number": null,
        "references": 2
      },
      {
        "section": "hero_board",
        "entry": "COMMAND PROTOCOL",
        "number": null,
        "references": 2
      },
      {
        "section": "hero_board",
        "entry": "GET OFF MY SHIP!",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "PUNCH YOUR WAY THROUGH (ULTIMATE)",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SET TO KILL",
        "number": null,
        "references": 2
      },
      {
        "section": "cards",
        "entry": "THERE'S COFFEE IN THAT NEBULA",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "RESOLVE",
        "number": null,
        "references": 2
      },
      {
        "section": "cards",
        "entry": "SHORE LEAVE II",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "TACTICAL EXERCISES II",
        "number": null,
        "references": 1
      }
    ],
    "combadge_die.svg": [
      {
        "section": "hero_board",
        "entry": "SHORE LEAVE",
        "number": null,
        "references": 3
      },
      {
        "section": "hero_board",
        "entry": "TACTICAL EXERCISES",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "COMMAND PROTOCOL",
        "number": null,
        "references": 2
      },
      {
        "section": "hero_board",
        "entry": "GET OFF MY SHIP!",
        "number": null,
        "references": 2
      },
      {
        "section": "hero_board",
        "entry": "SHIELDS UP",
        "number": null,
        "references": 2
      },
      {
        "section": "cards",
        "entry": "RESOLVE",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SHORE LEAVE II",
        "number": null,
        "references": 3
      },
      {
        "section": "cards",
        "entry": "TACTICAL EXERCISES II",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SHIELDS UP II",
        "number": null,
        "references": 2
      },
      {
        "section": "cards",
        "entry": "SHIELDS UP III",
        "number": null,
        "references": 2
      }
    ],
    "command_codes.svg": [
      {
        "section": "hero_board",
        "entry": "SHORE LEAVE",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "RED ALERT",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "TACTICAL EXERCISES",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "COMMAND PROTOCOL",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "GET OFF MY SHIP!",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "PUNCH YOUR WAY THROUGH (ULTIMATE)",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SET TO KILL",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "COMMAND TRAINING",
        "number": null,
        "references": 2
      },
      {
        "section": "cards",
        "entry": "RESOLVE",
        "number": null,
        "references": 2
      },
      {
        "section": "cards",
        "entry": "SHORE LEAVE II",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "TACTICAL EXERCISES II",
        "number": null,
        "references": 1
      }
    ],
    "cp.svg": [
      {
        "section": "leaflet",
        "entry": "COFFEE",
        "number": 1,
        "references": 1
      },
      {
        "section": "leaflet",
        "entry": "COFFEE",
        "number": null,
        "references": 1
      },
      {
        "section": "leaflet",
        "entry": "REPRIMAND",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "COMMAND TRAINING",
        "number": 2,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "COMMAND TRAINING",
        "number": 4,
        "references": 1
      }
    ],
    "damage_prevention.svg": [
      {
        "section": "hero_board",
        "entry": "SHIELDS UP",
        "number": 1,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "SHIELDS UP",
        "number": 2,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "COUNTERPOINT",
        "number": 3,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SHIELDS UP II",
        "number": 1,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SHIELDS UP II",
        "number": 2,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SHIELDS UP III",
        "number": 1,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SHIELDS UP III",
        "number": 2,
        "references": 1
      }
    ],
    "defense_3_dice.svg": [
      {
        "section": "hero_board",
        "entry": "SHIELDS UP",
        "number": null,
        "references": 1
      }
    ],
    "defense_4_dice.svg": [
      {
        "section": "cards",
        "entry": "SHIELDS UP II",
        "number": null,
        "references": 1
      }
    ],
    "defense_5_dice.svg": [
      {
        "section": "cards",
        "entry": "SHIELDS UP III",
        "number": null,
        "references": 1
      }
    ],
    "earth_die.svg": [
      {
        "section": "hero_board",
        "entry": "RED ALERT",
        "number": null,
        "references": 4
      },
      {
        "section": "hero_board",
        "entry": "TACTICAL EXERCISES",
        "number": null,
        "references": 4
      },
      {
        "section": "hero_board",
        "entry": "COMMAND PROTOCOL",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "GET OFF MY SHIP!",
        "number": null,
        "references": 2
      },
      {
        "section": "hero_board",
        "entry": "SHIELDS UP",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "PUNCH YOUR WAY THROUGH (ULTIMATE)",
        "number": null,
        "references": 5
      },
      {
        "section": "cards",
        "entry": "RESOLVE",
        "number": null,
        "references": 3
      },
      {
        "section": "cards",
        "entry": "TACTICAL EXERCISES II",
        "number": null,
        "references": 4
      },
      {
        "section": "cards",
        "entry": "SHIELDS UP II",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SHIELDS UP III",
        "number": null,
        "references": 1
      }
    ],
    "healing.svg": [
      {
        "section": "cards",
        "entry": "RESOLVE",
        "number": 6,
        "references": 1
      }
    ],
    "largestraight.svg": [
      {
        "section": "hero_board",
        "entry": "GET OFF MY SHIP!",
        "number": null,
        "references": 1
      }
    ],
    "normal_damage.svg": [
      {
        "section": "hero_board",
        "entry": "FIRE PHASERS",
        "number": 4,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "FIRE PHASERS",
        "number": 5,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "FIRE PHASERS",
        "number": 6,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "DO IT",
        "number": 7,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "RED ALERT",
        "number": 7,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "TACTICAL EXERCISES",
        "number": 4,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "COMMAND PROTOCOL",
        "number": 2,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "COMMAND PROTOCOL",
        "number": 4,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "GET OFF MY SHIP!",
        "number": 1,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "GET OFF MY SHIP!",
        "number": 3,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "GET OFF MY SHIP!",
        "number": 7,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SET TO KILL",
        "number": 3,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "COUNTERPOINT",
        "number": 3,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "FIRE PHASERS II",
        "number": 5,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "FIRE PHASERS II",
        "number": 6,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "FIRE PHASERS II",
        "number": 7,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "FIRE PHASERS III",
        "number": 6,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "FIRE PHASERS III",
        "number": 7,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "FIRE PHASERS III",
        "number": 8,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "TACTICAL EXERCISES II",
        "number": 4,
        "references": 1
      }
    ],
    "reprimand.svg": [
      {
        "section": "hero_board",
        "entry": "DO IT",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "RED ALERT",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "GET OFF MY SHIP!",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "SHIELDS UP",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "PUNCH YOUR WAY THROUGH (ULTIMATE)",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "REPRIMANDED",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "FIRE PHASERS III",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SHIELDS UP II",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SHIELDS UP III",
        "number": null,
        "references": 1
      }
    ],
    "roll_die.svg": [
      {
        "section": "leaflet",
        "entry": "COFFEE",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "TACTICAL EXERCISES",
        "number": null,
        "references": 2
      },
      {
        "section": "hero_board",
        "entry": "GET OFF MY SHIP!",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "SHIELDS UP",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "DETERMINATION",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "THERE'S COFFEE IN THAT NEBULA",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "CAPTAIN'S PREROGATIVE",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "RESOLVE",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "TACTICAL EXERCISES II",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SHIELDS UP II",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SHIELDS UP III",
        "number": null,
        "references": 1
      }
    ],
    "smallstraight.svg": [
      {
        "section": "hero_board",
        "entry": "DO IT",
        "number": null,
        "references": 1
      }
    ],
    "undefendable_damage.svg": [
      {
        "section": "hero_board",
        "entry": "PUNCH YOUR WAY THROUGH (ULTIMATE)",
        "number": 12,
        "references": 1
      }
    ]
  },
  "asset_observations": [
    {
      "file": "leaflet.svg",
      "status": "observed",
      "scope": "die_reference_legend",
      "sha256": "70c87ed0250aa2b14dfd4a9f3da3c5fa2edda20449e73435dbd4a21c70f2c2b4",
      "icons": [
        {
          "path": "icons/die_1.svg",
          "instances": 1
        },
        {
          "path": "icons/die_2.svg",
          "instances": 1
        },
        {
          "path": "icons/die_3.svg",
          "instances": 1
        },
        {
          "path": "icons/die_4.svg",
          "instances": 1
        },
        {
          "path": "icons/die_5.svg",
          "instances": 1
        },
        {
          "path": "icons/die_6.svg",
          "instances": 1
        }
      ]
    }
  ]
}
-->
