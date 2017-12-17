import unittest

from day9 import get_solutions

class Day9Part1Test(unittest.TestCase):

    def test_empty_group(self):
        score, _ = get_solutions(r"{}")
        self.assertEqual(1, score, msg="Score should be 1")

    def test_nested_groups_simple(self):
        score, _ = get_solutions(r"{{{}}}")
        self.assertEqual(6, score, msg="Score should be 6")

    def test_nested_two_subgroups(self):
        score, _ = get_solutions(r"{{},{}}")
        self.assertEqual(5, score, msg="Score should be 5")

    def test_nested_groups_complex(self):
        score, _ = get_solutions(r"{{{},{},{{}}}}")
        self.assertEqual(16, score, msg="Score should be 16")

    def test_group_with_one_garbage(self):
        score, _ = get_solutions(r"{<{},{},{{}}>}")
        self.assertEqual(1, score, msg="Score should be 1 (other groups are in garbage)")

    def test_group_with_multiple_garbages_simple(self):
        score, _ = get_solutions(r"{<a>,<a>,<a>,<a>}")
        self.assertEqual(1, score, msg="Score should be 1")

    def test_group_with_garbage_in_subgroup(self):
        score, _ = get_solutions(r"{{<a>},{<a>},{<a>},{<a>}}")
        self.assertEqual(9, score, msg="Score should be 9")

    def test_group_with_garbage_cancellation(self):
        score, _ = get_solutions(r"{{<!>},{<!>},{<!>},{<a>}}")
        self.assertEqual(3, score, msg="Score should be 3")

    def test_special_case1(self):
        score, _ = get_solutions(r"{<{ <}!>!>>}")
        self.assertEqual(1, score, msg="Score should be 1")

if __name__ == '__main__':
    unittest.main()
