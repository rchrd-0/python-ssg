# type: ignore
import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
