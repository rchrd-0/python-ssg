import unittest

import block_markdown


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]

        self.assertListEqual(block_markdown.markdown_to_blocks(text), expected)

    def test_markdown_to_blocks_multiple_empty(self):
        text = """

# This is a heading


This is a paragraph of text. It has some **bold** and *italic* words inside of it.


* This is the first list item in a list block
* This is a list item
* This is another list item



"""

        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]

        self.assertListEqual(block_markdown.markdown_to_blocks(text), expected)

    def test_markdown_to_blocks_trailing_leading(self):
        text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]

        self.assertListEqual(block_markdown.markdown_to_blocks(text), expected)

    def test_block_to_block_type_heading(self):
        heading_1 = "# heading 1"
        heading_2 = "## heading 2"
        heading_3 = "### heading 3"
        heading_6 = "###### heading 6"
        heading_7 = "####### heading 7"

        expected = (["heading"] * 4) + ["paragraph"]

        self.assertListEqual(
            [
                block_markdown.block_to_block_type(heading_1),
                block_markdown.block_to_block_type(heading_2),
                block_markdown.block_to_block_type(heading_3),
                block_markdown.block_to_block_type(heading_6),
                block_markdown.block_to_block_type(heading_7),
            ],
            expected,
        )

    def test_block_to_block_type_code(self):
        code_block = "```\nthis is a code block\n```"

        self.assertEqual(block_markdown.block_to_block_type(code_block), "code")

    def test_block_to_block_type_quote(self):
        quote_block = "> this is a quote"
        quotes_block = "> this is quote 1\n> this is quote 2"

        self.assertEqual(block_markdown.block_to_block_type(quote_block), "quote")
        self.assertEqual(block_markdown.block_to_block_type(quotes_block), "quote")

    def test_block_to_block_type_unordered_list(self):
        unordered_list_asterisk = "* item 1\n* item 2"
        unordered_list_dash = "- item 1\n- item 2"

        self.assertEqual(
            block_markdown.block_to_block_type(unordered_list_asterisk),
            "unordered_list",
        )
        self.assertEqual(
            block_markdown.block_to_block_type(unordered_list_dash), "unordered_list"
        )

    def test_block_to_block_type_ordered_list(self):
        correct_order = "1. first item\n2. second item\n3. third item"
        incorrect_order = "1. first item\n3. second item\n4. third item"

        self.assertEqual(
            block_markdown.block_to_block_type(correct_order), "ordered_list"
        )
        self.assertNotEqual(
            block_markdown.block_to_block_type(incorrect_order), "ordered_list"
        )
