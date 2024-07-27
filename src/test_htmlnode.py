# type: ignore

import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_void_tag(self):
        node_img = LeafNode("img", "", {"class": "w-auto", "src": "./ping.png"})
        expected_img_tag = '<img class="w-auto" src="./ping.png" />'
        self.assertEqual(node_img.to_html(), expected_img_tag)

        node_break = LeafNode("br", "")
        self.assertEqual(node_break.to_html(), "<br />")


class TestParentNode(unittest.TestCase):
    def test_empty_tag(self):
        expected_exception = "ParentNode must have a tag"
        with self.assertRaises(ValueError) as context:
            parent_node = ParentNode(
                None, [LeafNode("p", "paragraph"), LeafNode("p", "another paragraph")]
            )
            parent_node.to_html()
        self.assertEqual(str(context.exception), expected_exception)

    def test_empty_children(self):
        expected_exception = "ParentNode must have children"

        test_cases = [("empty_list", []), ("None", None)]
        for case_name, params in test_cases:
            with self.subTest(case=case_name):
                with self.assertRaises(ValueError) as context:
                    parent_node = ParentNode("div", params)
                    parent_node.to_html()
                self.assertEqual(str(context.exception), expected_exception)

    def test_to_html_depth_1(self):
        expected = (
            "<div><p>this is a paragraph</p><p>this is another paragraph</p></div>"
        )
        parent_node = ParentNode(
            "div",
            [
                LeafNode("p", "this is a paragraph"),
                LeafNode("p", "this is another paragraph"),
            ],
        )

        self.assertEqual(parent_node.to_html(), expected)

    def test_to_html_depth_2(self):
        parent_node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "normal text"),
                        LeafNode("span", "this is a span"),
                        LeafNode("b", "bold text"),
                        LeafNode("i", "italic text"),
                    ],
                ),
                LeafNode("p", "this is a paragraph"),
                LeafNode("img", "", {"class": "w-auto", "src": "./ping.png"}),
            ],
        )

        expected = '<div><p>normal text<span>this is a span</span><b>bold text</b><i>italic text</i></p><p>this is a paragraph</p><img class="w-auto" src="./ping.png" /></div>'

        self.assertEqual(parent_node.to_html(), expected)

    def test_to_html_deep(self):
        parent_node = ParentNode(
            "main",
            [
                ParentNode(
                    "div",
                    [
                        ParentNode(
                            "div",
                            [
                                ParentNode(
                                    "p",
                                    [
                                        LeafNode(None, "hello, "),
                                        LeafNode("b", "world!"),
                                    ],
                                )
                            ],
                        )
                    ],
                )
            ],
        )
        expected = "<main><div><div><p>hello, <b>world!</b></p></div></div></main>"
        self.assertEqual(parent_node.to_html(), expected)

    def test_to_html_with_props(self):
        parent_node = ParentNode(
            "div", [LeafNode("p", "text")], {"id": "main", "class": "container"}
        )
        expected = '<div id="main" class="container"><p>text</p></div>'
        self.assertEqual(parent_node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()
