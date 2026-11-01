import unittest
from rules_punctuation import remove_dice_commas


class DiceCommaTests(unittest.TestCase):
    def block(self, text):
        return '<div data-source-line="rules">'+text+'</div>'

    def icon(self,name):
        return '<span data-icon="'+name+'"><img src="icons/'+name+'" /></span>'

    def test_grouped_dice_and_styled_comma(self):
        text=self.block('<span class="dice-group">'+self.icon('earth_die.svg')+' '+self.icon('earth_die.svg')+'</span><span>,</span> Gain.')
        result,count=remove_dice_commas(text)
        self.assertEqual(count,1)
        self.assertIn('<span></span> Gain.',result)

    def test_status_commas_and_other_punctuation_remain(self):
        text=self.block(self.icon('coffee_token.svg')+', gain '+self.icon('coffee_die.svg')+': Deal 4, then draw.')
        self.assertEqual(remove_dice_commas(text),(text,0))

    def test_roll_die_comma_is_removed(self):
        text=self.block(self.icon('roll_die.svg')+' , gain.')
        result,count=remove_dice_commas(text)
        self.assertEqual(count,1)
        self.assertTrue(result.endswith('  gain.</div>'))

    def test_metadata_is_not_gameplay_rules(self):
        text='<div data-source-line="metadata">'+self.icon('coffee_die.svg')+', cost</div>'
        self.assertEqual(remove_dice_commas(text),(text,0))


if __name__=='__main__':unittest.main()
