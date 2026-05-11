import unittest
from grade_calculator import calculate_average, get_grade_letter, get_remarks


class TestGradeCalculator(unittest.TestCase):

    # --- calculate_average ---
    def test_average_normal(self):
        self.assertAlmostEqual(calculate_average([80, 90, 70]), 80.0)

    def test_average_single(self):
        self.assertEqual(calculate_average([100]), 100.0)

    def test_average_empty(self):
        self.assertEqual(calculate_average([]), 0)

    # --- get_grade_letter ---
    def test_grade_A(self):
        self.assertEqual(get_grade_letter(95), "A")

    def test_grade_B(self):
        self.assertEqual(get_grade_letter(85), "B")

    def test_grade_C(self):
        self.assertEqual(get_grade_letter(75), "C")

    def test_grade_D(self):
        self.assertEqual(get_grade_letter(65), "D")

    def test_grade_F(self):
        self.assertEqual(get_grade_letter(50), "F")

    def test_grade_boundary_90(self):
        self.assertEqual(get_grade_letter(90), "A")

    def test_grade_boundary_80(self):
        self.assertEqual(get_grade_letter(80), "B")

    # --- get_remarks ---
    def test_remarks_excellent(self):
        self.assertIn("Excellent", get_remarks(92))

    def test_remarks_failing(self):
        self.assertIn("Failing", get_remarks(40))


if __name__ == "__main__":
    unittest.main()
