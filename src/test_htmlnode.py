# type: ignore

import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    SAMPLE_PROPS = {"href": "https://rchrd.co", "target": "_blank"}

    def test_values(self):
        node = HTMLNode("p", "foobar")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "foobar")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props_to_html(self):
        node = HTMLNode(props=self.SAMPLE_PROPS)
        expected = ' href="https://rchrd.co" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_to_html_leading_whitespace(self):
        node = HTMLNode(props=self.SAMPLE_PROPS)
        self.assertNotEqual(
            node.props_to_html(), 'href="https://rchrd.co" target="_blank"'
        )

    def test_to_html_empty(self):
        node = HTMLNode()
        self.assertIs(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("p", "paragraph value", props=self.SAMPLE_PROPS)
        expected = "HTMLNode(p, paragraph value, None, {'href': 'https://rchrd.co', 'target': '_blank'})"
        self.assertEqual(repr(node), expected)


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node_0 = LeafNode("p", "This is a paragraph of text.")
        node_1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(node_0.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(
            node_1.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_repr(self):
        node_0 = LeafNode("p", "This is a paragraph of text.")
        node_1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            repr(node_0), "LeafNode(p, This is a paragraph of text., None, None)"
        )
        self.assertEqual(
            repr(node_1),
            "LeafNode(a, Click me!, None, {'href': 'https://www.google.com'})",
        )

    def test_no_tag(self):
        node_0 = LeafNode(None, "This has no tag")
        self.assertEqual(node_0.to_html(), "This has no tag")

    def test_none_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()


if __name__ == "__main__":
    unittest.main()
