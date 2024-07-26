from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode


def main():
    # text_node_0 = TextNode("text", TextType.bold)
    # print(text_node_0)
    leaf_node_0 = LeafNode("p", "This is a paragraph of text.")
    leaf_node_1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    print(leaf_node_0.to_html())
    print(leaf_node_1.to_html())
    # html_node_0 = HTMLNode("p", "paragraph value", props={
    #     "href": "https://rchrd.co",
    #     "target": "_blank"
    # })
    # print(html_node_0)


main()
