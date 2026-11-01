"""Regression checks for hero-specific Ultimate layouts; never writes assets."""
import copy
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

from ultimate_rules import parse_ultimates, rebuild_ultimate, source_layout
from icon_shadows import strip_ultimate_activation_shadows

ROOT=Path(__file__).resolve().parents[1]
HEROES={'Janeway':('PUNCH YOUR WAY THROUGH (ULTIMATE)',36.5),'Tuvok':('LOGICAL OUTCOME (ULTIMATE)',30.375)}


class UltimateTests(unittest.TestCase):
    def sample(self,hero):
        folder=ROOT/'Heroes'/hero
        root=ET.parse(folder/'hero_board.svg').getroot();markdown=(folder/'rules.md').read_text()
        title,disclaimer=HEROES[hero];layout=source_layout(root,title)
        values=[' ']
        for item in parse_ultimates(markdown)[title]['effects']:
            if item['kind']=='text':values.extend(re.findall(r'\S+',item['text']))
        for text in layout['texts']:values.extend(re.findall(r'\S+',''.join(text.itertext())))
        # Layout regression uses deterministic narrow synthetic advances. Real
        # conversions require exact Chrome measurements, not these test values.
        widths={'normal':{value:len(value)*.1 for value in values}}
        return root,markdown,title,layout,widths,disclaimer

    def test_each_hero_preserves_effective_size_single_line_and_disclaimer(self):
        for hero in HEROES:
            with self.subTest(hero=hero):
                root,md,title,before,widths,note_size=self.sample(hero)
                untouched=copy.deepcopy(before['panel'])
                disclaimer=[ET.tostring(e) for e in before['disclaimers']]
                rebuild_ultimate(root,md,title,widths)
                after=source_layout(root,title)
                self.assertAlmostEqual(after['effective_size'],49.95,places=4)
                self.assertTrue(all(abs(s-note_size)<.00001 for s in after['disclaimer_sizes']))
                self.assertEqual(disclaimer,[ET.tostring(e) for e in after['disclaimers']])
                self.assertEqual(len({e.get('y') for e in after['texts']}),1)
                self.assertTrue(all(e.get('text-anchor')=='start' for e in after['texts']))
                self.assertEqual(after['first'].get('x'),before['first'].get('x'))
                strip_ultimate_activation_shadows(untouched,title)
                changed=copy.deepcopy(after['panel'])
                source_layout(untouched,title)['body'].clear()
                source_layout(changed,title)['body'].clear()
                self.assertEqual(ET.tostring(untouched),ET.tostring(changed))

    def test_forced_effects_break_is_rejected(self):
        _,md,_,_,_,_=self.sample('Janeway')
        md=md.replace('>Gain 3 ', '>Gain<br />3 ',1)
        with self.assertRaisesRegex(ValueError,'one line'):
            parse_ultimates(md)

    def test_overflow_is_reported_instead_of_wrapping_or_shrinking(self):
        root,md,title,_,widths,_=self.sample('Tuvok')
        md=md.replace('>Increase Logic', '>'+('Increase '*500)+'Logic',1)
        with self.assertRaisesRegex(ValueError,'layout review'):
            rebuild_ultimate(root,md,title,widths)


if __name__=='__main__':
    unittest.main()
