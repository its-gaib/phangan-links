import copy
import unittest

from scripts.verification import shared_check_date, verification_summary, verification_text


class VerificationTests(unittest.TestCase):
    def test_mixed_dates_and_missing_checks_are_distinguished(self):
        entries = [
            {'id': 'older', 'checkedAt': '2026-11-03'},
            {'id': 'newer', 'checkedAt': '2026-11-09'},
            {'id': 'unknown'},
        ]
        original = copy.deepcopy(entries)
        summary = verification_summary(entries)
        self.assertEqual(summary, {
            'totalCount': 3, 'checkedCount': 2, 'missingCheckCount': 1,
            'earliestCheckedAt': '2026-11-03', 'latestCheckedAt': '2026-11-09',
        })
        self.assertIsNone(shared_check_date(summary))
        self.assertEqual(verification_text(summary), 'Recorded checks: 2 of 3 links, dated 2026-11-03 to 2026-11-09. 1 link has no recorded check date.')
        self.assertEqual(entries, original)

    def test_all_missing_dates_do_not_claim_a_check(self):
        summary = verification_summary([{'id': 'unknown'}, {'id': 'null', 'checkedAt': None}])
        self.assertEqual(summary['checkedCount'], 0)
        self.assertEqual(summary['missingCheckCount'], 2)
        self.assertIsNone(summary['earliestCheckedAt'])
        self.assertIsNone(summary['latestCheckedAt'])
        self.assertIsNone(shared_check_date(summary))
        self.assertEqual(verification_text(summary), 'No check dates are recorded for the 2 links.')

    def test_uniform_complete_checks_retain_legacy_shared_date(self):
        summary = verification_summary([{'id': str(i), 'checkedAt': '2026-11-03'} for i in range(3)])
        self.assertEqual(shared_check_date(summary), '2026-11-03')
        self.assertEqual(verification_text(summary), 'Recorded checks: 3 of 3 links, dated 2026-11-03.')

    def test_uniform_partial_checks_do_not_claim_all_links_checked(self):
        summary = verification_summary([{'id': 'checked', 'checkedAt': '2026-11-03'}, {'id': 'missing'}])
        self.assertIsNone(shared_check_date(summary))

    def test_empty_directory_has_no_shared_date(self):
        summary = verification_summary([])
        self.assertIsNone(shared_check_date(summary))
        self.assertEqual(summary['totalCount'], 0)

    def test_invalid_recorded_dates_fail_instead_of_becoming_verified(self):
        for value in ['2026-1-03', '2026-02-30', '2026-11-09T12:00:00Z', '<script>', 42, False]:
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, 'Invalid checkedAt date for entry: broken'):
                verification_summary([{'id': 'broken', 'checkedAt': value}])


if __name__ == '__main__':
    unittest.main()
