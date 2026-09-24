import unittest

from clinic_no_show_model.models import Record
from clinic_no_show_model.scoring import score_record


class DepthCheck8(unittest.TestCase):
    def test_008_field_validation(self):
        record = Record(id="appointment-008", exposure=83148, signal=0.590, urgency=4)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
