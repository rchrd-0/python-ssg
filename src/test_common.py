import unittest

import common
from textnode import TextNode, TextType, text_node_to_html


class TestSplitNodes(unittest.TestCase):
    def test_bold(self):
        node = TextNode("this contains **bold** text", TextType.text)
        split_nodes = common.split_nodes_delimiter([node], "**", TextType.bold)
        expected = [
            TextNode("this contains ", TextType.text),
            TextNode("bold", TextType.bold),
            TextNode(" text", TextType.text),
        ]

        self.assertListEqual(split_nodes, expected)

    def test_bold_multiple(self):
        node = TextNode("**bold 1**, **bold_2** and text", TextType.text)
        split_nodes = common.split_nodes_delimiter([node], "**", TextType.bold)
        expected = [
            TextNode("bold 1", TextType.bold),
            TextNode(", ", TextType.text),
            TextNode("bold_2", TextType.bold),
            TextNode(" and text", TextType.text),
        ]

        self.assertListEqual(split_nodes, expected)

    def test_leading_trailing(self):
        node = TextNode("**leading** and **trailing**", TextType.text)
        split_nodes = common.split_nodes_delimiter([node], "**", TextType.bold)
        expected = [
            TextNode("leading", TextType.bold),
            TextNode(" and ", TextType.text),
            TextNode("trailing", TextType.bold),
        ]

        self.assertListEqual(split_nodes, expected)

    def test_italic(self):
        node = TextNode("this contains *italic* text", TextType.text)
        split_nodes = common.split_nodes_delimiter([node], "*", TextType.italic)
        expected = [
            TextNode("this contains ", TextType.text),
            TextNode("italic", TextType.italic),
            TextNode(" text", TextType.text),
        ]

        self.assertListEqual(split_nodes, expected)

    def test_code(self):
        node = TextNode("this contains a `code` block", TextType.text)
        split_nodes = common.split_nodes_delimiter([node], "`", TextType.code)
        expected = [
            TextNode("this contains a ", TextType.text),
            TextNode("code", TextType.code),
            TextNode(" block", TextType.text),
        ]

        self.assertListEqual(split_nodes, expected)

    def test_multiple_call(self):
        node = TextNode(
            "this is **bold** text, while this is *italic* and then we have `code`",
            TextType.text,
        )
        bold_nodes = common.split_nodes_delimiter([node], "**", TextType.bold)
        italic_nodes = common.split_nodes_delimiter(bold_nodes, "*", TextType.italic)
        final_nodes = common.split_nodes_delimiter(italic_nodes, "`", TextType.code)
        expected = [
            TextNode("this is ", TextType.text),
            TextNode("bold", TextType.bold),
            TextNode(" text, while this is ", TextType.text),
            TextNode("italic", TextType.italic),
            TextNode(" and then we have ", TextType.text),
            TextNode("code", TextType.code),
        ]

        self.assertListEqual(expected, final_nodes)


class TestExtractMarkdownLinkImage(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is text with a link [to my portfolio](https://rchrd.co) and [to my GitHub](https://github.com/rchrd-0)"
        expected = [
            ("to my portfolio", "https://rchrd.co"),
            ("to my GitHub", "https://github.com/rchrd-0"),
        ]

        self.assertEqual(common.extract_markdown_links(text), expected)

    def test_extract_markdown_images(self):
        text = "here's a cute ![neovim logo](https://raw.githubusercontent.com/Aikoyori/ProgrammingVTuberLogos/main/Neovim/NeovimShadowed.png) and ![intellij](https://raw.githubusercontent.com/SAWARATSUKI/KawaiiLogos/main/IntelliJ%20IDEA/IntelliJ%20IDEA.png)"
        expected = [
            (
                "neovim logo",
                "https://raw.githubusercontent.com/Aikoyori/ProgrammingVTuberLogos/main/Neovim/NeovimShadowed.png",
            ),
            (
                "intellij",
                "https://raw.githubusercontent.com/SAWARATSUKI/KawaiiLogos/main/IntelliJ%20IDEA/IntelliJ%20IDEA.png",
            ),
        ]

        self.assertEqual(common.extract_markdown_links(text), expected)


if __name__ == "__main__":
    unittest.main()
