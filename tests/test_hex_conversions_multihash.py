from __future__ import (absolute_import, division, print_function)

import unittest
from datetime import datetime

import imagehash
from .utils import TestImageHash

class Test (TestImageHash):
    def setUp(self):
        self.image = self.get_data_image()

    def test_hex_to_multi_hash(self):
        generated_hash = imagehash.crop_resistant_hash(self.image,min_segment_size= 500,segmentation_image_size=1000)
        #options above are required such that it delivers a true multi image hash with multiple segments
        string = str(generated_hash)
        emsg = ('Stringified multihash did not match original hash')
        self.assertEqual(
            generated_hash,
            imagehash.hex_to_multihash(string),
            emsg
        )

if __name__ == '__main__':
    unittest.main()
