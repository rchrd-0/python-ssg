# type: ignore
import unittest

from textnode import TextNode, TextType, text_node_to_html


class TestTextNode(unittest.TestCase):
    SAMPLE_TEXT = "Foobar"

    def test_eq(self):
        node_0 = TextNode(self.SAMPLE_TEXT, TextType.bold)
        node_1 = TextNode("Foobar", TextType.bold)
        self.assertEqual(node_0, node_1)

    def test_not_eq(self):
        node_0 = TextNode(self.SAMPLE_TEXT, TextType.bold)
        node_1 = TextNode(self.SAMPLE_TEXT, TextType.italic)
        self.assertNotEqual(node_0, node_1)

    def test_default_url(self):
        node = TextNode(self.SAMPLE_TEXT, TextType.bold)
        self.assertIsNone(node.url)

    def test_custom_url(self):
        custom_url = "https://rchrd.co"
        node = TextNode(self.SAMPLE_TEXT, TextType.bold, custom_url)
        self.assertIsNotNone(node.url)
        self.assertEqual(node.url, "https://rchrd.co")

    def test_invalid_text_type_int(self):
        with self.assertRaises(TypeError):
            TextNode(self.SAMPLE_TEXT, 1)

    def test_invalid_text_type_str(self):
        with self.assertRaises(TypeError):
            TextNode(self.SAMPLE_TEXT, "foo")

    def test_invalid_text_type_attribute(self):
        with self.assertRaises(AttributeError):
            TextNode(self.SAMPLE_TEXT, TextType.fail)

    def test_repr(self):
        expected = "TextNode(Foobar, italic, https://rchrd.co)"
        node_0 = TextNode(self.SAMPLE_TEXT, TextType.italic, "https://rchrd.co")
        self.assertEqual(repr(node_0), expected)


class TestTextNodeToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("this is a text node", TextType.text)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "this is a text node")

    def test_bold(self):
        node = TextNode("this is a bold node", TextType.bold)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "this is a bold node")

    def test_italic(self):
        node = TextNode("this is an italic node", TextType.italic)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "this is an italic node")

    def test_code(self):
        node = TextNode("this is a code node", TextType.code)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "this is a code node")

    def test_link(self):
        node = TextNode("this is a link", TextType.link, "https://rchrd.co")
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "this is a link")
        self.assertEqual(html_node.props, {"href": "https://rchrd.co"})

    def test_image(self):
        node = TextNode(
            "this is an image", TextType.image, "https://rchrd.co/static/ping.png"
        )
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://rchrd.co/static/ping.png", "alt": "this is an image"},
        )


if __name__ == "__main__":
    unittest.main()
