import unittest

from mdtable import to_markdown


class ToMarkdown(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(
            to_markdown("a,b\n1,2\n"),
            "| a | b |\n| --- | --- |\n| 1 | 2 |\n",
        )

    def test_short_rows_are_padded(self):
        self.assertIn("| 1 |  |", to_markdown("a,b\n1\n"))

    def test_pipes_are_escaped(self):
        self.assertIn("x \\| y", to_markdown("h\nx | y\n"))

    def test_alignment(self):
        self.assertIn("| :--- | ---: |", to_markdown("a,b\n1,2\n", align="lr"))

    def test_tabs(self):
        self.assertEqual(to_markdown("a\tb\n", delimiter="\t"), "| a | b |\n| --- | --- |\n")

    def test_empty(self):
        self.assertEqual(to_markdown(""), "")


if __name__ == "__main__":
    unittest.main()
