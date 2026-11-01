import unittest
from basic_power_layout import basic_text_start, set_basic_text_anchor, new_basic_row


class BasicPowerLayoutTests(unittest.TestCase):
    def test_leading_space_does_not_shift_visible_anchor(self):
        record=[{'text':' Deal ','baseline':235.5,'startX':333.409,'visibleStartX':340.254}]
        row={};set_basic_text_anchor(row,record,235.5)
        self.assertEqual(row['source_text_start_x'],340.254)

    def test_unmeasured_or_new_layout_requires_explicit_setting(self):
        with self.assertRaisesRegex(ValueError,'explicit approved'):
            basic_text_start([],235.5)
        with self.assertRaisesRegex(ValueError,'Refresh Chrome'):
            basic_text_start([{'text':'Deal','baseline':235.5,'startX':333.409}],235.5)

    def test_each_row_uses_its_own_anchor(self):
        records=[{'text':'Deal','baseline':y,'visibleStartX':x} for x,y in [(412,836),(440,929),(474,1021)]]
        self.assertEqual([basic_text_start(records,y) for y in [836,929,1021]],[412,440,474])


    def test_new_card_needs_no_original_and_preserves_gap(self):
        row=new_basic_row('upgrade_card',3)
        self.assertEqual(row['dice_top'],145)
        self.assertEqual(row['text_baseline'],192.25)
        self.assertAlmostEqual(row['text_start_x']-(row['dice_x'][-1]+row['dice_size']),16.667)
        self.assertTrue(all(abs(b-a-row['dice_size'])<1e-9 for a,b in zip(row['dice_x'],row['dice_x'][1:])))

    def test_new_board_uses_explicit_origin_and_uniform_scale_once(self):
        original=new_basic_row('hero_board',5)
        moved=new_basic_row('hero_board',5,origin=(100,200),scale=2)
        self.assertEqual(moved['dice_top'],200+original['dice_top']*2)
        self.assertEqual(moved['text_start_x'],100+original['text_start_x']*2)
        self.assertEqual(moved['text_gap'],original['text_gap']*2)

    def test_unsupported_new_layout_fails_closed(self):
        with self.assertRaises(ValueError):new_basic_row('upgrade_card',6)
        with self.assertRaises(ValueError):new_basic_row('action_card',3)


if __name__=='__main__':unittest.main()
