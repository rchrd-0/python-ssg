# type: ignore

import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    SAMPLE_PROPS = {
        "href": "https://rchrd.co",
        "target": "_blank"
    }

    def test_values(self):
        node = HTMLNode("p", "foobar")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "foobar")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_to_html(self):
        node = HTMLNode(props=self.SAMPLE_PROPS)
        expected = ' href="https://rchrd.co" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_to_html_leading_whitespace(self):
        node = HTMLNode(props=self.SAMPLE_PROPS)
        self.assertNotEqual(node.props_to_html(), 'href="https://rchrd.co" target="_blank"')

    def test_to_html_empty(self):
        node = HTMLNode()
        self.assertIs(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("p", "paragraph value", props=self.SAMPLE_PROPS)
        expected = "HTMLNode(p, paragraph value, None, {'href': 'https://rchrd.co', 'target': '_blank'})"
        self.assertEqual(repr(node), expected)


if __name__ == '__main__':
    unittest.main()
