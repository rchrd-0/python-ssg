from textnode import TextNode, TextType, text_node_to_html
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    text_node = TextNode("text", TextType.italic)
    print(text_node)


main()
