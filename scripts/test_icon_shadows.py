from pathlib import Path
import unittest
import xml.etree.ElementTree as ET
from icon_shadows import remove_shadow_filters


class ActivationShadowTests(unittest.TestCase):
    def test_master_surface_is_retained_but_instance_shadow_removed(self):
        path=Path(__file__).resolve().parents[1]/'Heroes/Janeway/icons/coffee_die.svg'
        original=path.read_bytes();icon=ET.fromstring(original)
        shapes=[(e.tag,e.get('d'),e.get('fill'),e.get('stroke')) for e in icon.iter() if e.tag.rsplit('}',1)[-1] in {'path','rect','polygon'}]
        self.assertTrue(any(e.get('filter') for e in icon.iter()))
        remove_shadow_filters(icon)
        self.assertFalse(any(e.get('filter') for e in icon.iter()))
        self.assertEqual(shapes,[(e.tag,e.get('d'),e.get('fill'),e.get('stroke')) for e in icon.iter() if e.tag.rsplit('}',1)[-1] in {'path','rect','polygon'}])
        self.assertEqual(path.read_bytes(),original)


if __name__=='__main__':unittest.main()
