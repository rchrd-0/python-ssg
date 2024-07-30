import unittest

import inline_markdown
from textnode import TextNode, TextType


class TestSplitNodes(unittest.TestCase):
    def test_bold(self):
        node = TextNode("this contains **bold** text", TextType.text)
        split_nodes = inline_markdown.split_nodes_delimiter([node], "**", TextType.bold)
        expected = [
            TextNode("this contains ", TextType.text),
            TextNode("bold", TextType.bold),
            TextNode(" text", TextType.text),
        ]

        self.assertListEqual(split_nodes, expected)

    def test_bold_multiple(self):
        node = TextNode("**bold 1**, **bold_2** and text", TextType.text)
        split_nodes = inline_markdown.split_nodes_delimiter([node], "**", TextType.bold)
        expected = [
            TextNode("bold 1", TextType.bold),
            TextNode(", ", TextType.text),
            TextNode("bold_2", TextType.bold),
            TextNode(" and text", TextType.text),
        ]

        self.assertListEqual(split_nodes, expected)

    def test_leading_trailing(self):
        node = TextNode("**leading** and **trailing**", TextType.text)
        split_nodes = inline_markdown.split_nodes_delimiter([node], "**", TextType.bold)
        expected = [
            TextNode("leading", TextType.bold),
            TextNode(" and ", TextType.text),
            TextNode("trailing", TextType.bold),
        ]

        self.assertListEqual(split_nodes, expected)

    def test_italic(self):
        node = TextNode("this contains *italic* text", TextType.text)
        split_nodes = inline_markdown.split_nodes_delimiter(
            [node], "*", TextType.italic
        )
        expected = [
            TextNode("this contains ", TextType.text),
            TextNode("italic", TextType.italic),
            TextNode(" text", TextType.text),
        ]

        self.assertListEqual(split_nodes, expected)

    def test_code(self):
        node = TextNode("this contains a `code` block", TextType.text)
        split_nodes = inline_markdown.split_nodes_delimiter([node], "`", TextType.code)
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
        bold_nodes = inline_markdown.split_nodes_delimiter([node], "**", TextType.bold)
        italic_nodes = inline_markdown.split_nodes_delimiter(
            bold_nodes, "*", TextType.italic
        )
        final_nodes = inline_markdown.split_nodes_delimiter(
            italic_nodes, "`", TextType.code
        )
        expected = [
            TextNode("this is ", TextType.text),
            TextNode("bold", TextType.bold),
            TextNode(" text, while this is ", TextType.text),
            TextNode("italic", TextType.italic),
            TextNode(" and then we have ", TextType.text),
            TextNode("code", TextType.code),
        ]

        self.assertListEqual(expected, final_nodes)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to my portfolio](https://rchrd.co) and [to my GitHub](https://github.com/rchrd-0)",
            TextType.text,
        )
        expected = [
            TextNode("This is text with a link ", TextType.text),
            TextNode("to my portfolio", TextType.link, "https://rchrd.co"),
            TextNode(" and ", TextType.text),
            TextNode("to my GitHub", TextType.link, "https://github.com/rchrd-0"),
        ]

        # self.assertListEqual(inline_markdown.split_nodes_link([node]), expected)
        self.assertListEqual(inline_markdown.split_nodes_image_links([node]), expected)

    def test_split_nodes_link_single(self):
        node = TextNode("[my portfolio](https://rchrd.co)", TextType.text)
        expected = [TextNode("my portfolio", TextType.link, "https://rchrd.co")]

        # self.assertListEqual(inline_markdown.split_nodes_link([node]), expected)
        self.assertListEqual(inline_markdown.split_nodes_image_links([node]), expected)

    def test_split_nodes_image(self):
        node = TextNode(
            "here's a cute ![neovim logo](https://raw.githubusercontent.com/Aikoyori/ProgrammingVTuberLogos/main/Neovim/NeovimShadowed.png) and ![intellij](https://raw.githubusercontent.com/SAWARATSUKI/KawaiiLogos/main/IntelliJ%20IDEA/IntelliJ%20IDEA.png)",
            TextType.text,
        )
        expected = [
            TextNode("here's a cute ", TextType.text),
            TextNode(
                "neovim logo",
                TextType.image,
                "https://raw.githubusercontent.com/Aikoyori/ProgrammingVTuberLogos/main/Neovim/NeovimShadowed.png",
            ),
            TextNode(" and ", TextType.text),
            TextNode(
                "intellij",
                TextType.image,
                "https://raw.githubusercontent.com/SAWARATSUKI/KawaiiLogos/main/IntelliJ%20IDEA/IntelliJ%20IDEA.png",
            ),
        ]

        # self.assertListEqual(inline_markdown.split_nodes_image([node]), expected)
        self.assertListEqual(inline_markdown.split_nodes_image_links([node]), expected)

    def test_split_nodes_image_single(self):
        node = TextNode(
            "![neovim logo](https://raw.githubusercontent.com/Aikoyori/ProgrammingVTuberLogos/main/Neovim/NeovimShadowed.png)",
            TextType.text,
        )
        expected = [
            TextNode(
                "neovim logo",
                TextType.image,
                "https://raw.githubusercontent.com/Aikoyori/ProgrammingVTuberLogos/main/Neovim/NeovimShadowed.png",
            )
        ]

        # self.assertListEqual(inline_markdown.split_nodes_image([node]), expected)
        self.assertListEqual(inline_markdown.split_nodes_image_links([node]), expected)

    def test_split_nodes_image_and_link(self):
        node = TextNode(
            "![neovim logo](https://raw.githubusercontent.com/Aikoyori/ProgrammingVTuberLogos/main/Neovim/NeovimShadowed.png) and my [portfolio](https://rchrd.co)",
            TextType.text,
        )
        expected = [
            TextNode(
                "neovim logo",
                TextType.image,
                "https://raw.githubusercontent.com/Aikoyori/ProgrammingVTuberLogos/main/Neovim/NeovimShadowed.png",
            ),
            TextNode(" and my ", TextType.text),
            TextNode("portfolio", TextType.link, "https://rchrd.co"),
        ]

        self.assertListEqual(inline_markdown.split_nodes_image_links([node]), expected)

    def test_split_nodes_link_first_then_image(self):
        node = TextNode(
            "have a look at my [portfolio](https://rchrd.co) and this cute ![neovim logo](https://raw.githubusercontent.com/Aikoyori/ProgrammingVTuberLogos/main/Neovim/NeovimShadowed.png)",
            TextType.text,
        )
        expected = [
            TextNode("have a look at my ", TextType.text),
            TextNode("portfolio", TextType.link, "https://rchrd.co"),
            TextNode(" and this cute ", TextType.text),
            TextNode(
                "neovim logo",
                TextType.image,
                "https://raw.githubusercontent.com/Aikoyori/ProgrammingVTuberLogos/main/Neovim/NeovimShadowed.png",
            ),
        ]

        self.assertListEqual(inline_markdown.split_nodes_image_links([node]), expected)


class TestExtractMarkdownLinkImage(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is text with a link [to my portfolio](https://rchrd.co) and [to my GitHub](https://github.com/rchrd-0)"
        expected = [
            ("to my portfolio", "https://rchrd.co"),
            ("to my GitHub", "https://github.com/rchrd-0"),
        ]

        self.assertEqual(inline_markdown.extract_markdown_links(text), expected)

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

        self.assertEqual(inline_markdown.extract_markdown_links(text), expected)


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.text),
            TextNode("text", TextType.bold),
            TextNode(" with an ", TextType.text),
            TextNode("italic", TextType.italic),
            TextNode(" word and a ", TextType.text),
            TextNode("code block", TextType.code),
            TextNode(" and an ", TextType.text),
            TextNode(
                "obi wan image", TextType.image, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.text),
            TextNode("link", TextType.link, "https://boot.dev"),
        ]

        self.assertListEqual(inline_markdown.text_to_textnodes(text), expected)


if __name__ == "__main__":
    unittest.main()
