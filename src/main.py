from textnode import TextNode, TextType, text_node_to_html
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    pass
    # html_node_0 = HTMLNode("p", "paragraph value", props={
    #     "href": "https://rchrd.co",
    #     "target": "_blank"
    # })
    # print(html_node_0)

    # leaf_node_0 = LeafNode("p", "This is a paragraph of text.")
    # leaf_node_1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    #
    # print(leaf_node_0.to_html())
    # print(leaf_node_1.to_html())

    # parent_node_0 = ParentNode(
    #     "div",
    #     [
    #         ParentNode(
    #             "p",
    #             [
    #                 LeafNode(None, "normal text"),
    #                 LeafNode("span", "this is a span"),
    #                 LeafNode("b", "bold text"),
    #                 LeafNode("i", "italic text"),
    #             ],
    #         ),
    #         LeafNode("p", "this is a paragraph"),
    #         LeafNode("img", "", {"class": "w-auto", "src": "./ping.png"}),
    #     ],
    # )
    # print(parent_node_0.to_html())

    # pass


main()
