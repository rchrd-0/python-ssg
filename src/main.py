import common
from textnode import TextNode, TextType, text_node_to_html
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    # text_node = TextNode("text", TextType.italic)
    # print(text_node)

    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

    print(common.text_to_textnodes(text))


main()
