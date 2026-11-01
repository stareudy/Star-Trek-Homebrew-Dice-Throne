# Tuvok — Rules

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

### MIND MELD

SVG reference: [leaflet.svg](leaflet.svg)

<!-- SVG presentation: left-aligned rules; Avenir Next Condensed Regular; observed local text size 39 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="MIND MELD" style="text-align:left;">
<div class="rule-title">MIND MELD</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Unique Status Effect | Stack limit: 1</div>
<div style="height:.55em;"></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Spend this token during your <span style="color:#336A9C">Main</span> Phase or<br />an opponent&#x27;s <span style="color:#EB943A">Offensive</span> <span style="color:#EB943A">Roll</span> Phase.</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">During your <span style="color:#336A9C">Main</span> Phase: choose an opponent.<br />They must reveal their hand to you.</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">During an opponent&#x27;s <span style="color:#EB943A">Offensive</span> <span style="color:#EB943A">Roll</span> Phase: spend this<br />before their first reroll. You can control their first<br />reroll attempt or force them to skip it.</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;font-style:italic;font-size:.88em;"><span style="font-style:italic">(</span><span style="font-style:italic">This</span> <span style="font-style:italic">token</span> <span style="font-style:italic">may</span> <span style="font-style:italic">not</span> <span style="font-style:italic">be</span> <span style="font-style:italic">removed</span> <span style="font-style:italic">or</span> <span style="font-style:italic">transferred</span> <span style="font-style:italic">by</span> <span style="font-style:italic">any</span> <span style="font-style:italic">means</span><span style="font-style:italic">.</span><span style="font-style:italic">)</span></div>
</div>

### LOGIC

SVG reference: [leaflet.svg](leaflet.svg)

<!-- SVG presentation: left-aligned rules; Avenir Next Condensed Regular; observed local text size 37 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="LOGIC" style="text-align:left;">
<div class="rule-title">LOGIC</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Positive Status Effect | Stack limit: 5</div>
<div style="height:.55em;"></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">You may activate one of these effects per turn.</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Spend x: During any Roll Phase add x<span class="icon" data-icon="normal_damage.svg" data-value="1" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 1" width="28" height="28" /></span> or prevent x<span class="icon" data-icon="damage_prevention.svg" data-value="1" style="width:1.282em;height:1.400em;"><img src="../../Shared/icons/damage_prevention.svg" alt="damage prevention 1" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Spend 2: During Upkeep Phase look at the top card<br />of your deck. Put it back on top or bottom</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Spend 3: During Upkeep Phase gain <span class="icon" data-icon="cp.svg" data-value="1" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 1" width="28" height="28" /></span> or draw <span class="icon" data-icon="carddraw.svg" data-value="1" style="width:1.213em;height:1.400em;"><img src="../../Shared/icons/carddraw.svg" alt="carddraw 1" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Spend 4: During Main Phase gain <span class="icon" data-icon="protect.svg" style="width:1.400em;height:1.400em;"><img src="icons/protect.svg" alt="protect" width="28" height="28" /></span> or inflict <span class="icon" data-icon="targeted.svg" style="width:1.400em;height:1.400em;"><img src="icons/targeted.svg" alt="targeted" width="28" height="28" /></span></div>
</div>

### TARGETED

SVG reference: [leaflet.svg](leaflet.svg)

<!-- SVG presentation: left-aligned rules; Avenir Next Condensed Regular; observed local text size 38 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="TARGETED" style="text-align:left;">
<div class="rule-title">TARGETED</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Negative Status Effect | Stack limit: 1</div>
<div style="height:.55em;"></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">When a player afflicted with this token is attacked by<br />an opponent, the attacker increases their damage by 2.<br />This is an Attack Modifier and persists until removed.</div>
</div>

### PROTECT

SVG reference: [leaflet.svg](leaflet.svg)

<!-- SVG presentation: left-aligned rules; Avenir Next Condensed Regular; observed local text size 38 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="PROTECT" style="text-align:left;">
<div class="rule-title">PROTECT</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Positive Status Effect | Stack limit: 1</div>
<div style="height:.55em;"></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">A player with this token may spend it at any time to<br />prevent half of their incoming damage, rounded up. If<br />two Protect tokens are spent against the same attack,<br />both independently halve the damage. Protect gained<br />from a Defensive Ability may be spent immediately.</div>
</div>

## HERO BOARD

### NERVE PINCH

SVG reference: [hero_board.svg](hero_board.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 41.625 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="NERVE PINCH" data-basic-layout="touching_deal_v1" style="text-align:center;">
<div class="rule-title">NERVE PINCH</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="5" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 5" width="28" height="28" /><b aria-hidden="true">5</b></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="6" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 6" width="28" height="28" /><b aria-hidden="true">6</b></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="7" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 7" width="28" height="28" /><b aria-hidden="true">7</b></span></div>
</div>

### MEDITATE

SVG reference: [hero_board.svg](hero_board.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 41.625 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="MEDITATE" style="text-align:center;">
<div class="rule-title">MEDITATE</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="salute_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/salute_die.svg" alt="salute die" width="28" height="28" /></span><span class="icon" data-icon="salute_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/salute_die.svg" alt="salute die" width="28" height="28" /></span><span class="icon" data-icon="salute_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/salute_die.svg" alt="salute die" width="28" height="28" /></span></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Roll 4 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span>:</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">For each <span class="icon" data-icon="phaser_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span> gain <span class="icon" data-icon="logic.svg" style="width:1.400em;height:1.400em;"><img src="icons/logic.svg" alt="logic" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="dice-group"><span class="icon" data-icon="idic_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span></span> gain <span class="icon" data-icon="protect.svg" style="width:1.400em;height:1.400em;"><img src="icons/protect.svg" alt="protect" width="28" height="28" /></span></div>
</div>

### MEASURED RESPONSE

SVG reference: [hero_board.svg](hero_board.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 41.625 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="MEASURED RESPONSE" style="text-align:center;">
<div class="rule-title">MEASURED RESPONSE</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="icon" data-icon="smallstraight.svg" style="width:4.348em;height:1.800em;"><img src="../../Shared/icons/smallstraight.svg" alt="smallstraight" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Roll 3 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span>:</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Gain <span class="icon" data-icon="phaser_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span>x<span class="icon" data-icon="logic.svg" style="width:1.400em;height:1.400em;"><img src="icons/logic.svg" alt="logic" width="28" height="28" /></span> and deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="6" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 6" width="28" height="28" /><b aria-hidden="true">6</b></span></div>
</div>

### TACTICAL PRECISION

SVG reference: [hero_board.svg](hero_board.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 41.625 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="TACTICAL PRECISION" style="text-align:center;">
<div class="rule-title">TACTICAL PRECISION</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Gain 2 <span class="icon" data-icon="logic.svg" style="width:1.400em;height:1.400em;"><img src="icons/logic.svg" alt="logic" width="28" height="28" /></span>, inflict <span class="icon" data-icon="targeted.svg" style="width:1.400em;height:1.400em;"><img src="icons/targeted.svg" alt="targeted" width="28" height="28" /></span>,</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">then deal <span class="icon numbered undefendable_damage" data-icon="undefendable_damage.svg" data-value="8" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/undefendable_damage.svg" alt="undefendable damage 8" width="28" height="28" /><b aria-hidden="true">8</b></span></div>
</div>

### COMBAT DRILL

SVG reference: [hero_board.svg](hero_board.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 41.625 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="COMBAT DRILL" style="text-align:center;">
<div class="rule-title">COMBAT DRILL</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="salute_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/salute_die.svg" alt="salute die" width="28" height="28" /></span><span class="icon" data-icon="salute_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/salute_die.svg" alt="salute die" width="28" height="28" /></span></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="4" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 4" width="28" height="28" /><b aria-hidden="true">4</b></span></div>
<div style="height:.55em;"></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Up to 3 <span class="icon" data-icon="logic.svg" style="width:1.400em;height:1.400em;"><img src="icons/logic.svg" alt="logic" width="28" height="28" /></span> may be spent<br />to add <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="2" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 2" width="28" height="28" /><b aria-hidden="true">2</b></span> each.<br />Additional <span class="icon" data-icon="logic.svg" style="width:1.400em;height:1.400em;"><img src="icons/logic.svg" alt="logic" width="28" height="28" /></span> may be spent<br />to add the standard <span class="icon" data-icon="normal_damage.svg" data-value="1" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 1" width="28" height="28" /></span></div>
</div>

### FINAL CALCULATION

SVG reference: [hero_board.svg](hero_board.svg)

> **SVG difference:** rules.txt specifies 8 initial damage; the saved SVG shows 6. This document retains 8.

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 41.625 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="FINAL CALCULATION" style="text-align:center;">
<div class="rule-title">FINAL CALCULATION</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="icon" data-icon="largestraight.svg" style="width:5.102em;height:1.800em;"><img src="../../Shared/icons/largestraight.svg" alt="largestraight" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="8" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 8" width="28" height="28" /><b aria-hidden="true">8</b></span>, then roll 2 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="icon" data-icon="phaser_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span> add <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="2" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 2" width="28" height="28" /><b aria-hidden="true">2</b></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="icon" data-icon="salute_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/salute_die.svg" alt="salute die" width="28" height="28" /></span> add <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="3" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 3" width="28" height="28" /><b aria-hidden="true">3</b></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="icon" data-icon="idic_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span> add <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="4" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 4" width="28" height="28" /><b aria-hidden="true">4</b></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="dice-group"><span class="icon" data-icon="idic_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span></span> make this attack<br />undefendable</div>
</div>

### KOLINAR (PASSIVE)

SVG reference: [hero_board.svg](hero_board.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 41.625 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="KOLINAR (PASSIVE)" data-passive-layout="title_rules_v1" style="text-align:center;">
<div class="rule-title">KOLINAR (PASSIVE)</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">During your Upkeep Phase,<br />gain <span class="icon" data-icon="logic.svg" style="width:1.400em;height:1.400em;"><img src="icons/logic.svg" alt="logic" width="28" height="28" /></span></div>
</div>

### RETURN FIRE

SVG reference: [hero_board.svg](hero_board.svg)

> **SVG difference:** The saved SVG includes an additional Salute result dealing 2 damage back and uses “back” after the Phaser damage. Those additions are absent from rules.txt and have not been added here.

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 41.625 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="RETURN FIRE" style="text-align:center;">
<div class="rule-title">RETURN FIRE</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="icon" data-icon="defense_3_dice.svg" style="width:4.950em;height:1.650em;"><img src="../../Shared/icons/defense_3_dice.svg" alt="defense 3 dice" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Roll 3 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span>:</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">For each <span class="icon" data-icon="phaser_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span> deal <span class="icon" data-icon="normal_damage.svg" data-value="1" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 1" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="dice-group"><span class="icon" data-icon="idic_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span></span> gain <span class="icon" data-icon="protect.svg" style="width:1.400em;height:1.400em;"><img src="icons/protect.svg" alt="protect" width="28" height="28" /></span></div>
</div>

### LOGICAL OUTCOME (ULTIMATE)

SVG reference: [hero_board.svg](hero_board.svg)

> **SVG difference:** rules.txt grants 4 Logic; the saved SVG shows 2. This document retains 4. The original SVG’s standard Ultimate restriction note is displayed separately as an asset note; it is not added to gameplay rules.

<!-- Ultimate presentation: left-aligned, single-line effects at 49.95 effective SVG units; left-aligned disclaimer at 30.375 effective SVG units. Preserve source transforms and disclaimer breaks; do not apply regular-panel defaults. -->
<div class="rule ultimate-rule" data-rule="LOGICAL OUTCOME (ULTIMATE)" style="text-align:left;" data-layout="ultimate" data-source-effective-rules-size="49.950002" data-source-effective-disclaimer-size="30.375">
<div class="rule-title">LOGICAL OUTCOME (ULTIMATE)</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;" data-ultimate-role="activation"><span class="dice-group"><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span></span></div>
<div class="rule-line ultimate-effects" data-source-line="rules" data-ultimate-role="effects" style="margin:.35em 0;text-align:left;white-space:nowrap;font-size:1.2em;">Increase Logic stack limit by 1, gain <span class="icon" data-icon="mind_meld.svg" style="width:1.400em;height:1.400em;"><img src="icons/mind_meld.svg" alt="mind meld" width="28" height="28" /></span> and 4 <span class="icon" data-icon="logic.svg" style="width:1.400em;height:1.400em;"><img src="icons/logic.svg" alt="logic" width="28" height="28" /></span>, then deal <span class="icon numbered undefendable_damage" data-icon="undefendable_damage.svg" data-value="12" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/undefendable_damage.svg" alt="undefendable damage 12" width="28" height="28" /><b aria-hidden="true">12</b></span></div>
<div class="rule-line ultimate-disclaimer" data-source-line="asset-note" data-ultimate-role="disclaimer" style="margin:.35em 0;text-align:left;font-size:0.729729730em;line-height:1.25;">Dice may be altered to prevent an Ultimate. Otherwise, no action<br />of any kind may be performed by an opponent until the ability fully completes.</div>
</div>

## CARDS

The first 18 cards in Tuvok's deck are standard Dice Throne cards and are omitted here. The cards below are Tuvok-specific.

### TACTICAL RECALIBRATION

SVG reference: [cards/tactical_recalibration.svg](cards/tactical_recalibration.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="TACTICAL RECALIBRATION" style="text-align:center;">
<div class="rule-title">TACTICAL RECALIBRATION</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#EB943A;margin-bottom:.7em;">Cost: <span class="icon" data-icon="cp.svg" data-value="1" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 1" width="28" height="28" /></span> | Roll Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">During your <span style="color:#EB943A">Offensive</span> <span style="color:#EB943A">Roll</span> <span style="color:#EB943A">Phase</span>,<br />after a roll attempt, reroll one die.</div>
</div>

### VULCAN COMPOSURE

SVG reference: [cards/vulcan_composure.svg](cards/vulcan_composure.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="VULCAN COMPOSURE" style="text-align:center;">
<div class="rule-title">VULCAN COMPOSURE</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#EB943A;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="2" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 2" width="28" height="28" /><b aria-hidden="true">2</b></span> | Roll Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">During your <span style="color:#EB943A">Defensive</span> <span style="color:#EB943A">Roll</span> <span style="color:#EB943A">Phase</span>,<br />prevent <span class="icon numbered damage_prevention" data-icon="damage_prevention.svg" data-value="2" style="width:1.282em;height:1.400em;"><img src="../../Shared/icons/damage_prevention.svg" alt="damage prevention 2" width="28" height="28" /><b aria-hidden="true">2</b></span>.</div>
</div>

### CALCULATED OPENING

SVG reference: [cards/calculated_opening.svg](cards/calculated_opening.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="CALCULATED OPENING" style="text-align:center;">
<div class="rule-title">CALCULATED OPENING</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#EB943A;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="2" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 2" width="28" height="28" /><b aria-hidden="true">2</b></span> | Roll Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">During your <span style="color:#EB943A">Offensive</span> <span style="color:#EB943A">Roll</span> <span style="color:#EB943A">Phase</span>,<br />gain <span class="icon" data-icon="logic.svg" style="width:1.400em;height:1.400em;"><img src="icons/logic.svg" alt="logic" width="28" height="28" /></span>.</div>
</div>

### KAL-TOH

SVG reference: [cards/kal_toh.svg](cards/kal_toh.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="KAL-TOH" style="text-align:center;">
<div class="rule-title">KAL-TOH</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#336A9C;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="2" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 2" width="28" height="28" /><b aria-hidden="true">2</b></span> | Main Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Look at the top 3 cards of your deck.<br />Put one on the bottom of your deck<br />and return the others to the top<br />in any order.</div>
</div>

### SECURITY PROTOCOLS

SVG reference: [cards/security_protocols.svg](cards/security_protocols.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="SECURITY PROTOCOLS" style="text-align:center;">
<div class="rule-title">SECURITY PROTOCOLS</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#336A9C;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="2" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 2" width="28" height="28" /><b aria-hidden="true">2</b></span> | Main Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Gain <span class="icon" data-icon="protect.svg" style="width:1.400em;height:1.400em;"><img src="icons/protect.svg" alt="protect" width="28" height="28" /></span>, or give <span class="icon" data-icon="protect.svg" style="width:1.400em;height:1.400em;"><img src="icons/protect.svg" alt="protect" width="28" height="28" /></span> to a teammate.</div>
</div>

### KOLINAHR DISCIPLINE

SVG reference: [cards/kolinahr_discipline.svg](cards/kolinahr_discipline.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="KOLINAHR DISCIPLINE" style="text-align:center;">
<div class="rule-title">KOLINAHR DISCIPLINE</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#336A9C;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="2" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 2" width="28" height="28" /><b aria-hidden="true">2</b></span> | Main Phase Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Gain 2 <span class="icon" data-icon="logic.svg" style="width:1.400em;height:1.400em;"><img src="icons/logic.svg" alt="logic" width="28" height="28" /></span>.</div>
</div>

### MY MIND TO YOUR MIND

SVG reference: [cards/my_mind_to_your_mind.svg](cards/my_mind_to_your_mind.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="MY MIND TO YOUR MIND" style="text-align:center;">
<div class="rule-title">MY MIND TO YOUR MIND</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="4" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 4" width="28" height="28" /><b aria-hidden="true">4</b></span> | Instant Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Gain <span class="icon" data-icon="mind_meld.svg" style="width:1.400em;height:1.400em;"><img src="icons/mind_meld.svg" alt="mind meld" width="28" height="28" /></span> and spend it while being<br />targeted by an opponent.</div>
</div>

### MY THOUGHTS TO YOUR THOUGHTS

SVG reference: [cards/my_thoughts_to_your_thoughts.svg](cards/my_thoughts_to_your_thoughts.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="MY THOUGHTS TO YOUR THOUGHTS" style="text-align:center;">
<div class="rule-title">MY THOUGHTS TO YOUR THOUGHTS</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="2" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 2" width="28" height="28" /><b aria-hidden="true">2</b></span> | Instant Action</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Force an opponent to reveal to you two<br />cards from their hand at random. Or, if<br />spent at the same time as My Mind To<br />Your Mind, activate both effects of Mind<br />Meld at the same time regardless<br />of current phase.</div>
</div>

### NERVE PINCH II

SVG reference: [cards/nerve_pinch_ii.svg](cards/nerve_pinch_ii.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="NERVE PINCH II" data-basic-layout="touching_deal_v1" style="text-align:center;">
<div class="rule-title">NERVE PINCH II</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="2" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 2" width="28" height="28" /><b aria-hidden="true">2</b></span> | Upgrade Card</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="6" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 6" width="28" height="28" /><b aria-hidden="true">6</b></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="7" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 7" width="28" height="28" /><b aria-hidden="true">7</b></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="8" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 8" width="28" height="28" /><b aria-hidden="true">8</b></span></div>
</div>

### NERVE PINCH III

SVG reference: [cards/nerve_pinch_iii.svg](cards/nerve_pinch_iii.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="NERVE PINCH III" data-basic-layout="touching_deal_v1" style="text-align:center;">
<div class="rule-title">NERVE PINCH III</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="4" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 4" width="28" height="28" /><b aria-hidden="true">4</b></span> | Upgrade Card</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="7" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 7" width="28" height="28" /><b aria-hidden="true">7</b></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="8" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 8" width="28" height="28" /><b aria-hidden="true">8</b></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span><span class="icon" data-icon="phaser_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span></span> Deal <span class="icon numbered normal_damage" data-icon="normal_damage.svg" data-value="9" style="width:1.650em;height:1.650em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 9" width="28" height="28" /><b aria-hidden="true">9</b></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On 4 of a kind, make this<br />attack undefendable.</div>
</div>

### KOLINAR II

SVG reference: [cards/kolinar_ii.svg](cards/kolinar_ii.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="KOLINAR II" data-passive-layout="title_rules_v1" style="text-align:center;">
<div class="rule-title">KOLINAR II</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="2" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 2" width="28" height="28" /><b aria-hidden="true">2</b></span> | Upgrade Card</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">During your Upkeep<br />Phase, roll 1 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span>.<br />On <span class="icon" data-icon="phaser_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span> gain <span class="icon" data-icon="logic.svg" style="width:1.400em;height:1.400em;"><img src="icons/logic.svg" alt="logic" width="28" height="28" /></span>.<br />On <span class="icon" data-icon="salute_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/salute_die.svg" alt="salute die" width="28" height="28" /></span> or <span class="icon" data-icon="idic_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span> gain 2 <span class="icon" data-icon="logic.svg" style="width:1.400em;height:1.400em;"><img src="icons/logic.svg" alt="logic" width="28" height="28" /></span>.</div>
</div>

### TACTICAL PRECISION II

SVG reference: [cards/tactical_precision_ii.svg](cards/tactical_precision_ii.svg)

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="TACTICAL PRECISION II" style="text-align:center;">
<div class="rule-title">TACTICAL PRECISION II</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="3" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 3" width="28" height="28" /><b aria-hidden="true">3</b></span> | Upgrade Card</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;font-weight:700;margin-top:1em;">Top panel: TACTICAL PRECISION II</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Gain 2 <span class="icon" data-icon="logic.svg" style="width:1.400em;height:1.400em;"><img src="icons/logic.svg" alt="logic" width="28" height="28" /></span>, inflict <span class="icon" data-icon="targeted.svg" style="width:1.400em;height:1.400em;"><img src="icons/targeted.svg" alt="targeted" width="28" height="28" /></span>,</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">then deal <span class="icon numbered undefendable_damage" data-icon="undefendable_damage.svg" data-value="9" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/undefendable_damage.svg" alt="undefendable damage 9" width="28" height="28" /><b aria-hidden="true">9</b></span></div>
<div style="height:.55em;"></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;font-weight:700;margin-top:1em;">Bottom panel — Targeting Lock:</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;"><span class="dice-group"><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.650em;height:1.650em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Inflict <span class="icon" data-icon="targeted.svg" style="width:1.400em;height:1.400em;"><img src="icons/targeted.svg" alt="targeted" width="28" height="28" /></span> and gain 3 <span class="icon" data-icon="logic.svg" style="width:1.400em;height:1.400em;"><img src="icons/logic.svg" alt="logic" width="28" height="28" /></span></div>
</div>

### RETURN FIRE II

SVG reference: [cards/return_fire_ii.svg](cards/return_fire_ii.svg)

> **SVG difference:** rules.txt specifies Roll 4 and 1 damage per Phaser; the saved SVG shows Roll 3 and 2 damage per Phaser, plus an additional Salute result dealing 2 damage back. This document retains the rules.txt values and effects.

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="RETURN FIRE II" style="text-align:center;">
<div class="rule-title">RETURN FIRE II</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="3" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 3" width="28" height="28" /><b aria-hidden="true">3</b></span> | Upgrade Card</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Roll 4 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span>:</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">For each <span class="icon" data-icon="phaser_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span> deal <span class="icon" data-icon="normal_damage.svg" data-value="1" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 1" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="dice-group"><span class="icon" data-icon="idic_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span></span> gain <span class="icon" data-icon="protect.svg" style="width:1.400em;height:1.400em;"><img src="icons/protect.svg" alt="protect" width="28" height="28" /></span></div>
</div>

### RETURN FIRE III

SVG reference: [cards/return_fire_iii.svg](cards/return_fire_iii.svg)

> **SVG difference:** rules.txt specifies Roll 5 and 1 damage per Phaser; the saved SVG shows Roll 4 and 2 damage per Phaser, plus an additional Salute result dealing 2 damage back. This document retains the rules.txt values and effects.

<!-- SVG presentation: center-aligned rules; Avenir Next Condensed Regular; observed local text size 37.5 SVG units (before group transforms). HTML uses a readable 20px scale. -->
<div class="rule" data-rule="RETURN FIRE III" style="text-align:center;">
<div class="rule-title">RETURN FIRE III</div>
<div data-source-line="metadata" style="font-size:.95em;font-weight:700;color:#F4F6F9;margin-bottom:.7em;">Cost: <span class="icon numbered cp" data-icon="cp.svg" data-value="5" style="width:1.312em;height:1.400em;"><img src="../../Shared/icons/cp.svg" alt="cp 5" width="28" height="28" /><b aria-hidden="true">5</b></span> | Upgrade Card</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">Roll 5 <span class="icon" data-icon="roll_die.svg" style="width:1.326em;height:1.400em;"><img src="../../Shared/icons/roll_die.svg" alt="roll die" width="28" height="28" /></span>:</div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">For each <span class="icon" data-icon="phaser_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/phaser_die.svg" alt="phaser die" width="28" height="28" /></span> deal <span class="icon" data-icon="normal_damage.svg" data-value="1" style="width:1.400em;height:1.400em;"><img src="../../Shared/icons/normal_damage.svg" alt="normal damage 1" width="28" height="28" /></span></div>
<div class="rule-line" data-source-line="rules" style="margin:.35em 0;">On <span class="dice-group"><span class="icon" data-icon="idic_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span><span class="icon" data-icon="idic_die.svg" style="width:1.400em;height:1.400em;"><img src="icons/idic_die.svg" alt="idic die" width="28" height="28" /></span></span> gain <span class="icon" data-icon="protect.svg" style="width:1.400em;height:1.400em;"><img src="icons/protect.svg" alt="protect" width="28" height="28" /></span></div>
</div>

<!-- stdt-icon-inventory:v1
{
  "schema_version": 1,
  "status": "current",
  "source": "rules.md",
  "content_sha256": "54fb57b2f144af44ee2f2f7052da08012b4c67fea49f8cbac6dd550c743c98d3",
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
      "entries": 4,
      "references": 6
    },
    "hero_board": {
      "entries": 9,
      "references": 73
    },
    "cards": {
      "entries": 14,
      "references": 66
    }
  },
  "total_rules_references": 145,
  "entries": [
    {
      "section": "leaflet",
      "name": "MIND MELD",
      "status": "written",
      "icons": []
    },
    {
      "section": "leaflet",
      "name": "LOGIC",
      "status": "written",
      "icons": [
        {
          "file": "carddraw.svg",
          "path": "../../Shared/icons/carddraw.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "cp.svg",
          "path": "../../Shared/icons/cp.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "damage_prevention.svg",
          "path": "../../Shared/icons/damage_prevention.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "protect.svg",
          "path": "icons/protect.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "targeted.svg",
          "path": "icons/targeted.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "leaflet",
      "name": "TARGETED",
      "status": "written",
      "icons": []
    },
    {
      "section": "leaflet",
      "name": "PROTECT",
      "status": "written",
      "icons": []
    },
    {
      "section": "hero_board",
      "name": "NERVE PINCH",
      "status": "written",
      "icons": [
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
        },
        {
          "file": "phaser_die.svg",
          "path": "icons/phaser_die.svg",
          "number": null,
          "references": 12
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "MEDITATE",
      "status": "written",
      "icons": [
        {
          "file": "idic_die.svg",
          "path": "icons/idic_die.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "logic.svg",
          "path": "icons/logic.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "phaser_die.svg",
          "path": "icons/phaser_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "protect.svg",
          "path": "icons/protect.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "salute_die.svg",
          "path": "icons/salute_die.svg",
          "number": null,
          "references": 3
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "MEASURED RESPONSE",
      "status": "written",
      "icons": [
        {
          "file": "logic.svg",
          "path": "icons/logic.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 6,
          "references": 1
        },
        {
          "file": "phaser_die.svg",
          "path": "icons/phaser_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
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
      "name": "TACTICAL PRECISION",
      "status": "written",
      "icons": [
        {
          "file": "idic_die.svg",
          "path": "icons/idic_die.svg",
          "number": null,
          "references": 4
        },
        {
          "file": "logic.svg",
          "path": "icons/logic.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "targeted.svg",
          "path": "icons/targeted.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "undefendable_damage.svg",
          "path": "../../Shared/icons/undefendable_damage.svg",
          "number": 8,
          "references": 1
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "COMBAT DRILL",
      "status": "written",
      "icons": [
        {
          "file": "logic.svg",
          "path": "icons/logic.svg",
          "number": null,
          "references": 2
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
          "number": 2,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 4,
          "references": 1
        },
        {
          "file": "phaser_die.svg",
          "path": "icons/phaser_die.svg",
          "number": null,
          "references": 3
        },
        {
          "file": "salute_die.svg",
          "path": "icons/salute_die.svg",
          "number": null,
          "references": 2
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "FINAL CALCULATION",
      "status": "written",
      "icons": [
        {
          "file": "idic_die.svg",
          "path": "icons/idic_die.svg",
          "number": null,
          "references": 3
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
          "number": 2,
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
          "number": 4,
          "references": 1
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 8,
          "references": 1
        },
        {
          "file": "phaser_die.svg",
          "path": "icons/phaser_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "salute_die.svg",
          "path": "icons/salute_die.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "KOLINAR (PASSIVE)",
      "status": "written",
      "icons": [
        {
          "file": "logic.svg",
          "path": "icons/logic.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "hero_board",
      "name": "RETURN FIRE",
      "status": "written",
      "icons": [
        {
          "file": "defense_3_dice.svg",
          "path": "../../Shared/icons/defense_3_dice.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "idic_die.svg",
          "path": "icons/idic_die.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "phaser_die.svg",
          "path": "icons/phaser_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "protect.svg",
          "path": "icons/protect.svg",
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
      "name": "LOGICAL OUTCOME (ULTIMATE)",
      "status": "written",
      "icons": [
        {
          "file": "idic_die.svg",
          "path": "icons/idic_die.svg",
          "number": null,
          "references": 5
        },
        {
          "file": "logic.svg",
          "path": "icons/logic.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "mind_meld.svg",
          "path": "icons/mind_meld.svg",
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
      "name": "TACTICAL RECALIBRATION",
      "status": "written",
      "icons": []
    },
    {
      "section": "cards",
      "name": "VULCAN COMPOSURE",
      "status": "written",
      "icons": [
        {
          "file": "damage_prevention.svg",
          "path": "../../Shared/icons/damage_prevention.svg",
          "number": 2,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "CALCULATED OPENING",
      "status": "written",
      "icons": [
        {
          "file": "logic.svg",
          "path": "icons/logic.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "KAL-TOH",
      "status": "written",
      "icons": []
    },
    {
      "section": "cards",
      "name": "SECURITY PROTOCOLS",
      "status": "written",
      "icons": [
        {
          "file": "protect.svg",
          "path": "icons/protect.svg",
          "number": null,
          "references": 2
        }
      ]
    },
    {
      "section": "cards",
      "name": "KOLINAHR DISCIPLINE",
      "status": "written",
      "icons": [
        {
          "file": "logic.svg",
          "path": "icons/logic.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "MY MIND TO YOUR MIND",
      "status": "written",
      "icons": [
        {
          "file": "mind_meld.svg",
          "path": "icons/mind_meld.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "MY THOUGHTS TO YOUR THOUGHTS",
      "status": "written",
      "icons": []
    },
    {
      "section": "cards",
      "name": "NERVE PINCH II",
      "status": "written",
      "icons": [
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
          "file": "phaser_die.svg",
          "path": "icons/phaser_die.svg",
          "number": null,
          "references": 12
        }
      ]
    },
    {
      "section": "cards",
      "name": "NERVE PINCH III",
      "status": "written",
      "icons": [
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
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 9,
          "references": 1
        },
        {
          "file": "phaser_die.svg",
          "path": "icons/phaser_die.svg",
          "number": null,
          "references": 12
        }
      ]
    },
    {
      "section": "cards",
      "name": "KOLINAR II",
      "status": "written",
      "icons": [
        {
          "file": "idic_die.svg",
          "path": "icons/idic_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "logic.svg",
          "path": "icons/logic.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "phaser_die.svg",
          "path": "icons/phaser_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "roll_die.svg",
          "path": "../../Shared/icons/roll_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "salute_die.svg",
          "path": "icons/salute_die.svg",
          "number": null,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "TACTICAL PRECISION II",
      "status": "written",
      "icons": [
        {
          "file": "idic_die.svg",
          "path": "icons/idic_die.svg",
          "number": null,
          "references": 7
        },
        {
          "file": "logic.svg",
          "path": "icons/logic.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "targeted.svg",
          "path": "icons/targeted.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "undefendable_damage.svg",
          "path": "../../Shared/icons/undefendable_damage.svg",
          "number": 9,
          "references": 1
        }
      ]
    },
    {
      "section": "cards",
      "name": "RETURN FIRE II",
      "status": "written",
      "icons": [
        {
          "file": "idic_die.svg",
          "path": "icons/idic_die.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "phaser_die.svg",
          "path": "icons/phaser_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "protect.svg",
          "path": "icons/protect.svg",
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
      "name": "RETURN FIRE III",
      "status": "written",
      "icons": [
        {
          "file": "idic_die.svg",
          "path": "icons/idic_die.svg",
          "number": null,
          "references": 2
        },
        {
          "file": "normal_damage.svg",
          "path": "../../Shared/icons/normal_damage.svg",
          "number": 1,
          "references": 1
        },
        {
          "file": "phaser_die.svg",
          "path": "icons/phaser_die.svg",
          "number": null,
          "references": 1
        },
        {
          "file": "protect.svg",
          "path": "icons/protect.svg",
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
        "section": "leaflet",
        "entry": "LOGIC",
        "number": 1,
        "references": 1
      }
    ],
    "cp.svg": [
      {
        "section": "leaflet",
        "entry": "LOGIC",
        "number": 1,
        "references": 1
      }
    ],
    "damage_prevention.svg": [
      {
        "section": "leaflet",
        "entry": "LOGIC",
        "number": 1,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "VULCAN COMPOSURE",
        "number": 2,
        "references": 1
      }
    ],
    "defense_3_dice.svg": [
      {
        "section": "hero_board",
        "entry": "RETURN FIRE",
        "number": null,
        "references": 1
      }
    ],
    "idic_die.svg": [
      {
        "section": "hero_board",
        "entry": "MEDITATE",
        "number": null,
        "references": 2
      },
      {
        "section": "hero_board",
        "entry": "TACTICAL PRECISION",
        "number": null,
        "references": 4
      },
      {
        "section": "hero_board",
        "entry": "FINAL CALCULATION",
        "number": null,
        "references": 3
      },
      {
        "section": "hero_board",
        "entry": "RETURN FIRE",
        "number": null,
        "references": 2
      },
      {
        "section": "hero_board",
        "entry": "LOGICAL OUTCOME (ULTIMATE)",
        "number": null,
        "references": 5
      },
      {
        "section": "cards",
        "entry": "KOLINAR II",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "TACTICAL PRECISION II",
        "number": null,
        "references": 7
      },
      {
        "section": "cards",
        "entry": "RETURN FIRE II",
        "number": null,
        "references": 2
      },
      {
        "section": "cards",
        "entry": "RETURN FIRE III",
        "number": null,
        "references": 2
      }
    ],
    "largestraight.svg": [
      {
        "section": "hero_board",
        "entry": "FINAL CALCULATION",
        "number": null,
        "references": 1
      }
    ],
    "logic.svg": [
      {
        "section": "hero_board",
        "entry": "MEDITATE",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "MEASURED RESPONSE",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "TACTICAL PRECISION",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "COMBAT DRILL",
        "number": null,
        "references": 2
      },
      {
        "section": "hero_board",
        "entry": "KOLINAR (PASSIVE)",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "LOGICAL OUTCOME (ULTIMATE)",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "CALCULATED OPENING",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "KOLINAHR DISCIPLINE",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "KOLINAR II",
        "number": null,
        "references": 2
      },
      {
        "section": "cards",
        "entry": "TACTICAL PRECISION II",
        "number": null,
        "references": 2
      }
    ],
    "mind_meld.svg": [
      {
        "section": "hero_board",
        "entry": "LOGICAL OUTCOME (ULTIMATE)",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "MY MIND TO YOUR MIND",
        "number": null,
        "references": 1
      }
    ],
    "normal_damage.svg": [
      {
        "section": "leaflet",
        "entry": "LOGIC",
        "number": 1,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "NERVE PINCH",
        "number": 5,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "NERVE PINCH",
        "number": 6,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "NERVE PINCH",
        "number": 7,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "MEASURED RESPONSE",
        "number": 6,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "COMBAT DRILL",
        "number": 1,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "COMBAT DRILL",
        "number": 2,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "COMBAT DRILL",
        "number": 4,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "FINAL CALCULATION",
        "number": 2,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "FINAL CALCULATION",
        "number": 3,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "FINAL CALCULATION",
        "number": 4,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "FINAL CALCULATION",
        "number": 8,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "RETURN FIRE",
        "number": 1,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "NERVE PINCH II",
        "number": 6,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "NERVE PINCH II",
        "number": 7,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "NERVE PINCH II",
        "number": 8,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "NERVE PINCH III",
        "number": 7,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "NERVE PINCH III",
        "number": 8,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "NERVE PINCH III",
        "number": 9,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "RETURN FIRE II",
        "number": 1,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "RETURN FIRE III",
        "number": 1,
        "references": 1
      }
    ],
    "phaser_die.svg": [
      {
        "section": "hero_board",
        "entry": "NERVE PINCH",
        "number": null,
        "references": 12
      },
      {
        "section": "hero_board",
        "entry": "MEDITATE",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "MEASURED RESPONSE",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "COMBAT DRILL",
        "number": null,
        "references": 3
      },
      {
        "section": "hero_board",
        "entry": "FINAL CALCULATION",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "RETURN FIRE",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "NERVE PINCH II",
        "number": null,
        "references": 12
      },
      {
        "section": "cards",
        "entry": "NERVE PINCH III",
        "number": null,
        "references": 12
      },
      {
        "section": "cards",
        "entry": "KOLINAR II",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "RETURN FIRE II",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "RETURN FIRE III",
        "number": null,
        "references": 1
      }
    ],
    "protect.svg": [
      {
        "section": "leaflet",
        "entry": "LOGIC",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "MEDITATE",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "RETURN FIRE",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "SECURITY PROTOCOLS",
        "number": null,
        "references": 2
      },
      {
        "section": "cards",
        "entry": "RETURN FIRE II",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "RETURN FIRE III",
        "number": null,
        "references": 1
      }
    ],
    "roll_die.svg": [
      {
        "section": "hero_board",
        "entry": "MEDITATE",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "MEASURED RESPONSE",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "FINAL CALCULATION",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "RETURN FIRE",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "KOLINAR II",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "RETURN FIRE II",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "RETURN FIRE III",
        "number": null,
        "references": 1
      }
    ],
    "salute_die.svg": [
      {
        "section": "hero_board",
        "entry": "MEDITATE",
        "number": null,
        "references": 3
      },
      {
        "section": "hero_board",
        "entry": "COMBAT DRILL",
        "number": null,
        "references": 2
      },
      {
        "section": "hero_board",
        "entry": "FINAL CALCULATION",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "KOLINAR II",
        "number": null,
        "references": 1
      }
    ],
    "smallstraight.svg": [
      {
        "section": "hero_board",
        "entry": "MEASURED RESPONSE",
        "number": null,
        "references": 1
      }
    ],
    "targeted.svg": [
      {
        "section": "leaflet",
        "entry": "LOGIC",
        "number": null,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "TACTICAL PRECISION",
        "number": null,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "TACTICAL PRECISION II",
        "number": null,
        "references": 2
      }
    ],
    "undefendable_damage.svg": [
      {
        "section": "hero_board",
        "entry": "TACTICAL PRECISION",
        "number": 8,
        "references": 1
      },
      {
        "section": "hero_board",
        "entry": "LOGICAL OUTCOME (ULTIMATE)",
        "number": 12,
        "references": 1
      },
      {
        "section": "cards",
        "entry": "TACTICAL PRECISION II",
        "number": 9,
        "references": 1
      }
    ]
  },
  "asset_observations": [
    {
      "file": "leaflet.svg",
      "status": "observed",
      "scope": "die_reference_legend",
      "sha256": "edc2b1b4662268c98693919ca013944dfbdd46fe8826c011ae89c5be3b656b83",
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
