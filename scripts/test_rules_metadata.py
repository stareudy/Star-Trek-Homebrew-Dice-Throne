"""Regression checks for rules-file inventory maintenance (no artwork changes)."""
from pathlib import Path
import tempfile
import unittest

from rules_metadata import build_inventory, refresh, split_metadata


class RulesMetadataTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'rules.md'
        for name in ['die.svg', 'other.svg', 'cp.svg']:
            (self.path.parent / name).write_text('<svg/>')

    def rules(self, content):
        return ('# Hero\n\n## HERO BOARD\n\n'
                '<div data-rule="ABILITY">'
                '<div data-source-line="metadata"><span data-icon="cp.svg"><img src="cp.svg"/></span></div>'
                '<div data-source-line="rules">' + content + '</div></div>\n')

    def icon(self, name='die.svg', value=None):
        numbered = f' data-value="{value}"' if value is not None else ''
        label = f'<b>{value}</b>' if value is not None else ''
        return f'<span data-icon="{name}"{numbered}><img src="{name}"/>{label}</span>'

    def test_counts_values_and_cost_exclusion(self):
        body = self.rules(self.icon(value=4) + self.icon(value=4) + self.icon('cp.svg'))
        inventory = build_inventory(self.path, body)
        self.assertEqual(inventory['total_rules_references'], 3)
        self.assertEqual(inventory['usage_by_icon']['die.svg'][0]['references'], 2)
        self.assertEqual(inventory['usage_by_icon']['die.svg'][0]['number'], 4)
        self.assertEqual(inventory['usage_by_icon']['cp.svg'][0]['references'], 1)

    def test_added_changed_removed_icons_replace_current_metadata(self):
        self.path.write_text(self.rules(self.icon(value=4)))
        refresh(self.path)
        body, _ = split_metadata(self.path.read_text())
        self.path.write_text(body.replace('die.svg', 'other.svg').replace('"4"', '"7"').replace('>4<', '>7<'))
        with self.assertRaises(ValueError):
            refresh(self.path, check=True)
        current = refresh(self.path)
        self.assertEqual(set(current['usage_by_icon']), {'other.svg'})
        self.assertEqual(current['usage_by_icon']['other.svg'][0]['number'], 7)
        saved = self.path.read_bytes()
        refresh(self.path)
        self.assertEqual(self.path.read_bytes(), saved)
        self.path.write_text(self.rules('No icons.'))
        current = refresh(self.path)
        self.assertEqual(current['usage_by_icon'], {})
        self.assertEqual(current['total_rules_references'], 0)
        self.assertEqual(self.path.read_text().count('<!-- stdt-icon-inventory:v1'), 1)
        refresh(self.path, check=True)

    def test_displayed_number_must_match_metadata(self):
        with self.assertRaisesRegex(ValueError, 'numeral disagrees'):
            build_inventory(self.path, self.rules(self.icon(value=4).replace('>4<', '>9<')))

    def test_placeholders_do_not_infer_icons_from_brainstorming(self):
        body = '# Hero\n\n## HERO BOARD\n\n### Ability 1\nRules: TBD\n\n## BRAINSTORMING\n\n### Idea\nSomething with dice.\n'
        inventory = build_inventory(self.path, body)
        self.assertEqual(inventory['status'], 'placeholders')
        self.assertEqual(len(inventory['entries']), 1)
        self.assertEqual(inventory['total_rules_references'], 0)


if __name__ == '__main__':
    unittest.main()
